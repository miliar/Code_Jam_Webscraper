void findPath(const PMap &map, Pos start, Pos dest, const std::vector<Pos> &blocks, std::vector<Pos> &path)
{
    //cout << "start = " << start.x << " " << start.y << endl;
    //path = std::vector <Pos> {Pos(21,15), Pos(21,16), Pos(21,17), Pos(21,18), Pos(21,19), Pos(21,20), Pos(22,20), Pos(23,20), Pos(24,20)};
    //path = std::vector <Pos> {Pos(21,15), Pos(22,16), Pos(23,17), Pos(24,18), Pos(24,19), Pos(24,20), Pos(24,21)};
    //path = std::vector <Pos> {Pos(21,15), Pos(21,16), Pos(22,16), Pos(22,17), Pos(23,17), Pos(23,18), Pos(24,18), Pos(24,19), Pos(24,20)};
    //cout << "length = " << length(path) << endl;
    
    struct Node
    {
        int x, y;
        int level;
        int priority;
        
        Node() : x(0), y(0), level(0), priority(0) {}
        Node(int xp, int yp, int d, int p) : x(xp), y(yp), level(d), priority(p) {}
        void updatePriority(int xDest, int yDest)
        {
            priority = level + estimate(xDest, yDest);
        }
        void nextLevel()
        {
            level += 100;
        }
        int estimate(const int &xDest, const int &yDest) const
        {
            int xd = xDest - x, yd = yDest - y;
            //return static_cast <int> (sqrt(1.0 * xd * xd + 1.0 * yd * yd));
            
            return static_cast <int> (10.0 * (sqrt(2.0) * std::min(xd, yd) + 1.0 * std::abs(xd - yd)));
        }
        bool operator < (const Node &b) const
        {
            return priority > b.priority;
        }
    };
    
    const int dx[] = {1, 0, -1, 0};
    const int dy[] = {0, 1, 0, -1};
    static int open_nodes_map[MAP_SIZE][MAP_SIZE];
    static unsigned char closed_nodes_map[MAP_SIZE][MAP_SIZE];
    static unsigned char dir_map[MAP_SIZE][MAP_SIZE];
    std::priority_queue <Node> pq[2];
    int pqi;
    int i, j, x, y, xdx, ydy;
    
    memset(closed_nodes_map, 0, sizeof(closed_nodes_map));
    memset(open_nodes_map, 0, sizeof(open_nodes_map));
    
    if (start == dest) return;
    
    for (size_t i = 0; i < blocks.size(); i++)
    {
        if (blocks[i].x >= 0 && blocks[i].x < MAP_SIZE && blocks[i].y >= 0 && blocks[i].y < MAP_SIZE)
        {
            closed_nodes_map[blocks[i].x][blocks[i].y] = 1;
        }
    }
    if (closed_nodes_map[dest.x][dest.y] == 1)
    {
        xdx = start.x < dest.x ? -1 : 1;
        ydy = start.y < dest.y ? -1 : 1;
        x = dest.x;
        y = dest.y;
        while (closed_nodes_map[x][y] == 1)
        {
            if (checkOnLine(start, dest, Pos(x + xdx, y)))
            {
                x += xdx;
            }
            else
            {
                y += ydy;
            }
        }
        dest = Pos(x, y);
    }
    
    Node n0(start.x, start.y, 0, 0);
    n0.updatePriority(dest.x, dest.y);
    pqi = 0;
    pq[pqi].push(n0);
    open_nodes_map[start.x][start.y] = n0.priority;
    while (!pq[pqi].empty())
    {
        n0 = pq[pqi].top();
        pq[pqi].pop();
        x = n0.x;
        y = n0.y;
        open_nodes_map[x][y] = 0;
        closed_nodes_map[x][y] = 1;
        if (x == dest.x && y == dest.y)
        {
            while(!(x == start.x && y == start.y))
            {
                j = dir_map[x][y];
                path.push_back(Pos(x, y));
                x += dx[j];
                y += dy[j];
            }
            path.push_back(start);
            reverse(path.begin(), path.end());
            /*for (int i = 0; i < path.size(); i++)
             {
             cout << "(" << path[i].x << "," << path[i].y << ")";
             }
             cout << endl;*/
            return;
        }
        for (i = 0; i < 4; i++)
        {
            xdx = x + dx[i];
            ydy = y + dy[i];
            if (!(xdx < 0 || xdx >= MAP_SIZE || ydy < 0 || ydy >= MAP_SIZE || map.getHeight(xdx, ydy) - map.getHeight(x, y) > 1
                  || map.getHeight(xdx, ydy) - map.getHeight(x, y) < -1 || closed_nodes_map[xdx][ydy] == 1))
            {
                Node m0(n0);
                m0.x = xdx;
                m0.y = ydy;
                m0.nextLevel();
                m0.updatePriority(dest.x, dest.y);
                if (open_nodes_map[xdx][ydy] == 0)
                {
                    open_nodes_map[xdx][ydy] = m0.priority;
                    pq[pqi].push(m0);
                    dir_map[xdx][ydy] = (i + 2) % 4;
                }
                else if (open_nodes_map[xdx][ydy] > m0.priority)
                {
                    open_nodes_map[xdx][ydy] = m0.priority;
                    dir_map[xdx][ydy] = (i + 2) % 4;
                    while (!(pq[pqi].top().x == xdx && pq[pqi].top().y == ydy))
                    {
                        pq[1 - pqi].push(pq[pqi].top());
                        pq[pqi].pop();
                    }
                    pq[pqi].pop();
                    if (pq[pqi].size() > pq[1 - pqi].size())
                    {
                        pqi = 1 - pqi;
                    }
                    while (!pq[pqi].empty())
                    {
                        pq[1 - pqi].push(pq[pqi].top());
                        pq[pqi].pop();
                    }
                    pqi = 1 - pqi;
                    pq[pqi].push(m0);
                }
            }
        }
    }
}