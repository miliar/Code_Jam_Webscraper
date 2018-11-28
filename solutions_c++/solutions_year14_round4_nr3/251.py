#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <climits>

using namespace std;

struct flow_graph{
    int MAX_V,E,s,t;
    int *cap,*to,*next,*last;
    bool *visited;
    
    flow_graph(){}
    
    flow_graph(int V, int MAX_E){
        MAX_V = V; E = 0;
        cap = new int[2*MAX_E], to = new int[2*MAX_E], next = new int[2*MAX_E];
        last = new int[MAX_V], visited = new bool[MAX_V];
        fill(last,last+MAX_V,-1);
    }
    
    void clear(){
        fill(last,last+MAX_V,-1);
        E = 0;
    }
    
    void add_edge(int u, int v, int uv, int vu = 0){
        to[E] = v, cap[E] = uv, next[E] = last[u]; last[u] = E++;
        to[E] = u, cap[E] = vu, next[E] = last[v]; last[v] = E++;
    }
    
    int dfs(int v, int f){
        if(v==t || f<=0) return f;
        if(visited[v]) return 0;
        visited[v] = true;
        
        for(int e = last[v];e!=-1;e = next[e]){
            int ret = dfs(to[e],min(f,cap[e]));
            
            if(ret>0){
                cap[e] -= ret;
                cap[e^1] += ret;
                return ret;
            }
        }
        
        return 0;
    }
    
    int max_flow(int source, int sink){
        s = source, t = sink;
        int f = 0,x;
        
        while(true){
            fill(visited,visited+MAX_V,false);
            x = dfs(s,INT_MAX);
            if(x==0) break;
            f += x;
        }
        
        return f;
    }
}G(2 + 2 * 100 * 500,2 * 100 + 5 * 100 * 500);

int dr[] = {-1,1,0,0};
int dc[] = {0,0,-1,1};

int main(){
    ios::sync_with_stdio(0);
    
    int TC;
    int W,H,B;
    bool ok[500][100];
    
    cin >> TC;
    
    for(int tc = 1;tc <= TC;++tc){
        cin >> W >> H >> B;
        G.clear();
        
        memset(ok,true,sizeof ok);
        
        for(int i = 0,X0,Y0,X1,Y1;i < B;++i){
            cin >> X0 >> Y0 >> X1 >> Y1;
            
            for(int j = X0;j <= X1;++j)
                for(int k = Y0;k <= Y1;++k)
                    ok[k][j] = false;
        }
        
        for(int i = 0;i < W;++i)
            if(ok[0][i]) G.add_edge(0,2 * (0 * W + i) + 2,1);
        for(int i = 0;i < W;++i)
            if(ok[H - 1][i]) G.add_edge(2 * ((H - 1) * W + i) + 3,1,1);
        
        for(int i = 0;i < H * W;++i)
            G.add_edge(2 * i + 2,2 * i + 3,1);
        
        for(int i = 0;i < H;++i)
            for(int j = 0;j < W;++j){
                if(ok[i][j]){
                    for(int k = 0;k < 4;++k){
                        int r = i + dr[k],c = j + dc[k];
                        
                        if(r >= 0 && r < H && c >= 0 && c < W && ok[r][c]){
                            G.add_edge(2 * (i * W + j) + 3,2 * (r * W + c) + 2,1);
                        }
                    }
                }
            }
        
        cout << "Case #" << tc << ": " << G.max_flow(0,1) << '\n';
    }
    
    return 0;
}
