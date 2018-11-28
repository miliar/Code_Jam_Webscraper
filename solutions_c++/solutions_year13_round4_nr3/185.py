// Erdős–Szekeres / mrozik

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

static const int MAXN = 2000;
int A[MAXN], B[MAXN];
vector<int> AL[MAXN+1], BL[MAXN+1];

vector<int> G[MAXN];
int IN[MAXN];
int R[MAXN];

int N;

void addEdge(int i, int j) {
    if (!(i<N && i>=0)) return;
    if (!(j<N && j>=0)) return;
    G[i].push_back(j);
    IN[j]++;
}


int main() {
    ios_base::sync_with_stdio(false);
    
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        
        cin>>N;
        for (int i=0; i<=N; i++)
            AL[i].clear(), BL[i].clear();
        for (int i=0; i<N; i++)
            G[i].clear(), IN[i]=0;
        
        for (int i=0; i<N; i++) {
            cin>>A[i];
            AL[A[i]].push_back(i);
        }
        
        for (int i=0; i<N; i++) {
            cin>>B[i];
            BL[B[i]].push_back(i);
        }
        
        for (int i=1; i<=N; i++)
            for (int j=int(AL[i].size())-2; j>=0; j--)
                addEdge(AL[i][j+1], AL[i][j]);

        for (int i=1; i<=N; i++)
            for (int j=0; j+1<int(BL[i].size()); j++)
                addEdge(BL[i][j], BL[i][j+1]);
            
        
        for (int j=0; j<N; j++) {
            int i=j-1;
            while (i>=0 && A[i]+1!=A[j]) i--;
            addEdge(i, j);
        }
            
        for (int j=0; j<N; j++) {
            int i=j+1;
            while (i<N && B[j]!=B[i]+1)
                i++;
            addEdge(i, j);
        }
            
        
        for (int ix=1; ix<=N; ix++) {
            int n=0;
            while (IN[n]!=0) {
                n++;
                assert(n<N);
            }
            IN[n] = -1;
            for (int i=0; i<int(G[n].size()); i++) {
                IN[G[n][i]] --;
            }
            
            R[n] = ix;
        }
        
        cout<<"Case #"<<t<<": ";
        for (int i=0; i<N; i++)
            cout<<R[i]<<" ";
        cout<<endl;
    }
    
    return 0;    
}
