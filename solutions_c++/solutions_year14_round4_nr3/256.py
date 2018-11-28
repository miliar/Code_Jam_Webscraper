#include<iostream>
#include<queue>
#include<map>
#include<cstring>
using namespace std;
typedef pair<int, int> MP;
const int INF = 1<<30;
const int BUF = 505;
const int NODE = 100005;

int W, H;
bool b[BUF][BUF];

void read() {
    for (int i = 0; i < BUF; ++i)
        for (int j = 0; j < BUF; ++j)
            b[i][j] = true;

    int nB;
    cin >> W >> H >> nB;

    for (int i = 0; i < nB; ++i) {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;

        for (int yy = y0; yy <= y1; ++yy)
            for (int xx = x0; xx <= x1; ++xx)
                b[yy][xx] = false;
    }
}

int nNode, SRC, DST;
vector<int> adj[NODE];
map<MP, int> cap;

int rc2id(int r, int c, bool isIn) {
    return (isIn ? 0 : H * W) + (r * W + c);
}

void buildGraph() {
    const int dr[] = {-1, 0, 1, 0};
    const int dc[] = {0, 1, 0, -1};

    cap.clear();
    for (int i = 0; i < NODE; ++i) adj[i].clear();

    SRC = H * W * 2;
    DST = H * W * 2 + 1;
    nNode = H * W * 2 + 2;

    for (int r = 0; r < H; ++r)
        for (int c = 0; c < W; ++c) {
            if (!b[r][c]) continue;
            
            cap[MP(rc2id(r, c, 1),rc2id(r, c, 0))] = 1;
            cap[MP(rc2id(r, c, 0),rc2id(r, c, 1))] = 0;
            adj[rc2id(r, c, 1)].push_back(rc2id(r, c, 0));
            adj[rc2id(r, c, 0)].push_back(rc2id(r, c, 1));

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                
                if (!(0 <= nr && nr < H && 0 <= nc && nc < W))
                    continue;
                
                if (!b[nr][nc])
                    continue;

                cap[MP(rc2id(r, c, 0),rc2id(nr, nc, 1))] = INF;
                cap[MP(rc2id(nr, nc, 1),rc2id(r, c, 0))] = 0;
                adj[rc2id(r, c, 0)].push_back(rc2id(nr, nc, 1));
                adj[rc2id(nr, nc, 1)].push_back(rc2id(r, c, 0));
            }
        }

    for (int c = 0; c < W; ++c) {
        cap[MP(SRC,rc2id(0, c, 1))] = 1;
        adj[SRC].push_back(rc2id(0, c, 1));
    }

    for (int c = 0; c < W; ++c) {
        cap[MP(rc2id(H - 1, c, 0), DST)] = 1;
        adj[rc2id(H - 1, c, 0)].push_back(DST);
    }
}


bool augment(int pi[]) {
    queue<int> Q;
  
    for (int i = 0; i < nNode; ++i)
        pi[i] = -1;
    pi[SRC] = -2;
    Q.push(SRC);
  
    while(!Q.empty() && pi[DST]==-1){
        int curr = Q.front();
        Q.pop();
    
        for(int i = 0; i < adj[curr].size(); ++i) {
            int nex = adj[curr][i];
            if(pi[nex]!=-1 || !cap.count(MP(curr,nex)) || cap[MP(curr,nex)]<=0) continue;
            pi[nex] = curr;
            Q.push(nex);
        }
    }
  
    return pi[DST]!=-1;
}


int maxFlow() {
    int sum = 0, pi[NODE];
  
    while(augment(pi)){
        int flow = INF;
        for(int cur=DST;pi[cur]>=0;cur=pi[cur])
            flow = min(flow,cap[MP(pi[cur],cur)]);

        for(int cur=DST;pi[cur]>=0;cur=pi[cur]){
            cap[MP(pi[cur],cur)] -= flow;
            cap[MP(cur,pi[cur])] += flow;
        }
    
        sum += flow;
    }
  
    return sum;
}


void work(int cases) {
    buildGraph();
    cout << "Case #" << cases << ": " << maxFlow() << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
