#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>

#include <vector>
#include <queue>

using namespace std;

struct TVertex
{
    bool m_empty;
    int m_index;

    TVertex()
        : m_empty(true)
        , m_index(-1)
    {
    }
};

typedef vector<TVertex> TLine;
typedef vector<TLine> TMatrix;

struct TNode
{
    int m_vertex;
    int m_value;

    TNode()
    {
    }

    TNode(int vertex, int value)
        : m_vertex(vertex)
        , m_value(value)
    {
    }
};

typedef vector<TNode> TNodeVector;
typedef vector<TNodeVector> TGraph;

typedef vector<bool> TBoolVector;

typedef vector<int> TIntVector;

bool bfs(const TGraph& rGraph, int s, int t, TIntVector& parent, TBoolVector& visited)
{
    // Create a visited array and mark all vertices as not visited
    for (size_t i = 0; i < visited.size(); ++i)
    {
        visited[i] = false;
    }
 
    // Create a queue, enqueue source vertex and mark source vertex
    // as visited
    queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;
 
    // Standard BFS Loop
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
 
        for (size_t i = 0; i < rGraph[u].size(); ++i)
        {
            int v = rGraph[u][i].m_vertex;
            if (!visited[v] && rGraph[u][i].m_value > 0)
            {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }
 
    // If we reached sink in BFS starting from source, then return
    // true, else false
    return visited[t];
}
 
// Returns tne maximum flow from s to t in the given graph
int fordFulkerson(TGraph& graph, int s, int t)
{
    int u, v;
 
    TIntVector parent(graph.size());  // This array is filled by BFS and to store path
    TBoolVector visited(graph.size());
 
    int max_flow = 0;  // There is no flow initially
 
    // Augment the flow while tere is path from source to sink
    while (bfs(graph, s, t, parent, visited))
    {
        // Find minimum residual capacity of the edhes along the
        // path filled by BFS. Or we can say find the maximum flow
        // through the path found.
        int path_flow = INT_MAX;
        for (v = t; v != s; v = parent[v])
        {
            u = parent[v];
            int index = 0;
            while (graph[u][index].m_vertex != v)
                ++index;
            path_flow = std::min(path_flow, graph[u][index].m_value);
        }
 
        // update residual capacities of the edges and reverse edges
        // along the path
        for (v = t; v != s; v=parent[v])
        {
            u = parent[v];

            int index = 0;
            while (graph[u][index].m_vertex != v)
                ++index;


            graph[u][index].m_value -= path_flow;
            
            index = 0;
            while (graph[v][index].m_vertex != u)
                ++index;

            graph[v][index].m_value += path_flow;
        }
 
        // Add path flow to overall flow
        max_flow += path_flow;
    }
 
    // Return the overall flow
    return max_flow;
}

int main()
{
    freopen("C-small-attempt0 (1).in", "r", stdin);
    freopen("C-small-attempt0 (1).out", "w", stdout);

    int nCases;
    scanf("%d", &nCases);
    for (int iTest = 0; iTest < nCases; ++iTest)
    {
        int w;
        int h;
        int b;
        scanf("%d%d%d", &w, &h, &b);
        TLine line(w);
        TMatrix matrix(h, line);
        for (int i = 0; i < b; ++i)
        {
            int x0;
            int y0;
            int x1;
            int y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            for (int j = x0; j <= x1; ++j)
            {
                for (int k = y0; k <= y1; ++k)
                {
                    matrix[k][j].m_empty = false;
                }
            }
        }

        int index = 1;
        for (int i = 0; i < matrix.size(); ++i)
        {
            for (int j = 0; j < matrix[i].size(); ++j)
            {
                if (matrix[i][j].m_empty)
                {
                    matrix[i][j].m_index = index;
                    index += 2;
                }
            }
        }

        TGraph graph(index + 1);
        for (int i = 0; i < matrix[0].size(); ++i)
        {
            if (matrix[0][i].m_empty)
            {
                graph[0].push_back( TNode(matrix[0][i].m_index, 1) );
                graph[matrix[0][i].m_index].push_back( TNode(0, 0) );
            }
        }
        for (int i = 0; i < matrix.size(); ++i)
        {
            for (int j = 0; j < matrix[i].size(); ++j)
                if (matrix[i][j].m_empty)
                {
                    graph[matrix[i][j].m_index + 1].push_back( TNode(matrix[i][j].m_index, 0) );
                    graph[matrix[i][j].m_index].push_back( TNode(matrix[i][j].m_index + 1, 1) );
                    
                    static const int DIRS[] = {1, 0, -1, 0, 0, 1, 0, -1};
                    for (int k = 0; k < 4; ++k)
                    {
                        int x = i + DIRS[2*k];
                        int y = j + DIRS[2*k + 1];
                        if (x >= 0 && x < matrix.size())
                            if (y >= 0 && y < matrix[x].size())
                                if (matrix[x][y].m_empty)
                                {
                                    graph[matrix[i][j].m_index + 1].push_back( TNode(matrix[x][y].m_index, 1) );
                                    graph[matrix[x][y].m_index].push_back( TNode(matrix[i][j].m_index + 1, 0) );
                                }
                    }
                }
        }
        for (int i = 0; i < matrix[0].size(); ++i)
        {
            if (matrix[matrix.size() - 1][i].m_empty)
            {
                graph[index].push_back( TNode(matrix[matrix.size() - 1][i].m_index + 1, 0) );
                graph[ matrix[matrix.size() - 1][i].m_index + 1].push_back( TNode(index, 1) );
            }
        }        

        int maxFlow = fordFulkerson(graph, 0, index);

        printf("Case #%d: %d\n", iTest + 1, maxFlow);
    }
    
    return 0;
}   