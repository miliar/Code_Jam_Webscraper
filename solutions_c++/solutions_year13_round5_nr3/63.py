#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;


static const int MAXN = 1000;
static const int MAXM = 2000;

struct Edge {
    int dest;
    unsigned w;
};

struct FullEdge {
    int src, dest;
    unsigned w0, w1;
};


int N, M, P;
vector<Edge> G[MAXN];
unsigned W[MAXN];
FullEdge FE[MAXM];
int PIX[MAXM];



void addEdge(int src, int dest, unsigned w) {
    
//     cout<<(src+1)<<"->"<<(dest+1)<<"  "<<w<<endl;
    Edge e;
    e.dest = dest;
    e.w = w;
    G[src].push_back(e);
    
//     for (int i=0; i<M; i++) cout<<W[i]<<" ";
//     cout<<endl;
}


void clearGraph() {
    for (int i=0; i<N; i++)
        G[i].clear();
    fill(W, W+N, 0x7fffffff);
}


void findShortestPaths(int v0) {
    W[v0] = 0;
    set<pair<unsigned, int> > queue;
    for (int i=0; i<int(G[v0].size()); i++)
        queue.insert(pair<unsigned, int>(G[v0][i].w, G[v0][i].dest));

    while (!queue.empty()) {
        pair<unsigned, int> p = *queue.begin();
        queue.erase(queue.begin());
        if (p.first >= W[p.second])
            continue;
        W[p.second] = p.first;
        for (int i=0; i<int(G[p.second].size()); i++)
            queue.insert(pair<unsigned, int>(p.first+G[p.second][i].w, G[p.second][i].dest));
    }
    
//     for (int i=0; i<N; i++)
//         cout<<W[i]<<" ";
//     cout<<endl;
}


int main() {
    ios_base::sync_with_stdio(false);
    
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        
        cin>>N>>M>>P;
        
        for (int i=0; i<M; i++) {
            cin>>FE[i].src>>FE[i].dest>>FE[i].w0>>FE[i].w1;
            FE[i].src--, FE[i].dest--;
        }
        
        for (int i=0; i<P; i++)
            cin>>PIX[i], PIX[i]--;
        
        int longestGood = 0;
        for (unsigned sit=0; sit<(1<<M); sit++) {
            
            clearGraph();
            
            for (int i=0; i<M; i++)
                if ((sit & (1<<i)) == 0)
                    addEdge(FE[i].dest, FE[i].src, FE[i].w0);
                else
                    addEdge(FE[i].dest, FE[i].src, FE[i].w1);
            
            findShortestPaths(1);
            
            for (int p=0; p<P; p++) {
                int src = FE[PIX[p]].src, dest = FE[PIX[p]].dest;
                if (W[dest] + FE[PIX[p]].w0 != W[src])
                    break;
                else
                    longestGood = max(longestGood, p+1);
            }
        }
        
        if (longestGood<P)
            cout<<"Case #"<<t<<": "<<(PIX[longestGood]+1)<<"\n";
        else
            cout<<"Case #"<<t<<": Looks Good To Me\n";
        
       
//         try {
//             for (int p=0; p<P; p++) {
//                 int src = FE[PIX[p]].src, dest = FE[PIX[p]].dest;
//                 if (W[src] < W[dest]+FE[PIX[p]].w0)
//                     throw PIX[p]+1;
//             }
//             
//             cout<<"Case #"<<t<<": Looks Good To Me\n";
//         }
//         catch (int p) {
//             cout<<"Case #"<<t<<": "<<p<<"\n";
//         }
        
    }
    
    return 0;
}
