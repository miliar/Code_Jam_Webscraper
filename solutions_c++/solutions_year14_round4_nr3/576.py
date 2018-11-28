#include <iostream>
#include <vector>
#include <map>
#include <stack>

using namespace std;

vector<vector<int>> adj;
map<pair<int,int>,int> capacity;
int source, sink;
int N, W, H, B; ;

void outputNode(int node) {
    if (node == sink) {cout << "[sink]"; return;}
    if (node == source) {cout << "[source]"; return;} 
    bool in = node % 2; node /= 2;
    cout << "(" << (node % W) << ", " << (node / W) << ", " << (in ? "in" : "out") << ")";
}

void augment(int from, int to) {
    // cout << "augment(";
    // outputNode(from); cout << ", "; outputNode(to); cout << ")" << endl;
    capacity[{from,to}] --;
    capacity[{to,from}] ++;
}
void addEdge(int from, int to) {
    // cout << "add Edge"; outputNode(from); cout << " "; outputNode(to); cout << endl;
    adj[from].push_back(to);
    adj[to].push_back(from);
    capacity[{from,to}]++;
}

bool findAndAugment() {
    // cout << "Augmenting" << endl;
    vector<int> parent(N, -1);
    stack<int> dfs; dfs.push(source);
    parent[source] = source;
    
    while(!dfs.empty() && parent[sink] == -1) {
        // cout << "exploring: "; outputNode(dfs.top()); cout << endl;
        int node = dfs.top(); dfs.pop();
        
        for(int neighbour: adj[node]) {
            if (parent[neighbour] == -1 && capacity[{node, neighbour}]) {
                parent[neighbour] = node;
                dfs.push(neighbour);
            }
        }
    }
    
    if (parent[sink] != -1) {
        // cout << "path found" << endl;
        int curr = sink;
        while(curr != source) {
            augment(parent[curr], curr);
            curr = parent[curr];
        }
        
        return true;
    }
    
    return false;
}

int getNodeID(int x, int y, bool in) {
    return 2*(y * W + x) + in;
}

int main() {
    int T; cin >> T;
    for(int t = 1; t <= T; ++t) {
        cin >> W >> H >> B;
        vector<vector<bool>> occ(W, vector<bool>(H));
        
        while(B--) {
            int x0, y0, x1, y1;
            cin >> x0 >> y0 >> x1 >> y1;
            
            for(int x = x0; x <= x1; ++x) {
                for(int y = y0; y <= y1; ++y) {
                    occ[x][y] = true;
                }
            }
        }
        
        //graphs contains one node + source + sink
        N = W * H * 2; //in and out
        source = N, sink = N + 1;
        N += 2;
        
        adj      = vector<vector<int>>(N);
        capacity.clear();
        //create edges
        for(int y = 0; y < H; ++y) {
            for(int x = 0; x < W; ++x) {
                int p = getNodeID(x,y,false);
                if (!occ[x][y]) {
                    if (y < H-1 && !occ[x  ][y+1]) { addEdge(p, getNodeID(x,y+1,true)); }
                    if (x < W-1 && !occ[x+1][y  ]) { addEdge(p, getNodeID(x+1,y,true)); }
                    if (x > 0   && !occ[x-1][y  ]) { addEdge(p, getNodeID(x-1,y,true)); }
                    if (y > 0   && !occ[x  ][y-1]) { addEdge(p, getNodeID(x,y-1,true)); }
                    
                    //in to out:
                    addEdge(p + 1, p);
                }
            }
        }
        //source and sink:
        for(int x = 0; x < W; ++x) {
            if (!occ[x][0  ]) { addEdge(source, getNodeID(x,0,   true )); }
            if (!occ[x][H-1]) { addEdge(getNodeID(x,H-1, false), sink); }
        }
        
        // cout << "Graph built" << endl;
        int flow = 0;
        while(findAndAugment()) flow++;
        cout << "Case #" << t << ": " << flow << endl;
    }
}