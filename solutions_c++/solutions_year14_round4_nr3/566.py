#include <map> 
#include <set> 
#include <list> 
#include <cmath> 
#include <ctime> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <cstdio> 
#include <string> 
#include <bitset> 
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <algorithm> 
#define sqr(x) ((x)*(x)) 
#define ABS(x) ((x<0)?(-(x)):(x)) 
#define eps (1e-9) 
#define mp make_pair 
#define pb push_back 
#define Pair pair<int,int> 
#define xx first 
#define yy second 
#define equal(a,b) (ABS(a-b)<eps) 
using namespace std; 
 
template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();} 
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; } 
 
int dx[8]={0, 0, 1,-1, 1, 1,-1,-1}; 
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1}; 
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2}; 
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1}; 
 
/////////////////////////////////////////////////////////////////////////////////////////////////////

// FAST
#define MAXV 111111
#define MAXE 1111111

int adj[2*MAXE],prev[2*MAXE],last[MAXV],cap[2*MAXE],now[MAXV],q[MAXV];
int d[MAXV];
class flowGraph{
    public:
        int s,t,ind;
        flowGraph(){
            ind=0;
            memset(last,-1,sizeof(last));
            memset(prev,-1,sizeof(prev));
        }
        void addedge(int a,int b,int c,int revc){
            adj[ind]=b; cap[ind]=c; prev[ind]=last[a]; last[a]=ind++;
            adj[ind]=a; cap[ind]=revc; prev[ind]=last[b]; last[b]=ind++;
        }
        int dfs(int v,int cur){
            if (v==t) return cur;
            for (int &i=now[v];i!=-1;i=prev[i]){
                int y=adj[i],x=v;
                if (cap[i]&&d[x]==d[y]+1){
                    int f=dfs(y,min(cap[i],cur));
                    if (f){
                        cap[i]-=f;
                        cap[i^1]+=f;
                        return f;
                    }
                }
            }
            return 0;
        }
        long long maxflow(int n,int s,int t){
            this->s=s; this->t=t;
            long long flow=0;
            while(1){
                memset(d,-1,sizeof(d));
                int a=0,b=0;
                d[t]=0;
                q[0]=t;
                while(a<=b){
                    int x=q[a++];
                    for (int i=last[x];i!=-1;i=prev[i]){
                        int y=adj[i];
                        if (d[y]==-1&&cap[i^1]){
                            d[y]=d[x]+1;
                            q[++b]=y;
                        }
                    }
                }
                if (d[s]==-1) return flow;
                for (int i=0;i<n;i++) now[i]=last[i];
                int f;
                do{
                    f=dfs(s,1<<30);
                    flow+=f;
                }while(f);
            }
        }
};

string testprefix = "C-small-attempt1";
int m, n, b;
int a[1000][1000];

int in(int x, int y) {
    return (x * m + y) * 2;
}

int out(int x, int y) {
    return (x * m + y) * 2 + 1;
}

void solveTest() {
    scanf("%d%d%d", &m, &n, &b);
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) a[i][j] = 1;

    // n is big
    for (int i = 0; i < b; i++) {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
        for (int x = x1; x <= x2; x++)
            for (int y = y1; y <= y2; y++)
                a[x][y] = 0;
    }

    flowGraph f;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 0) continue;
            f.addedge(in(i, j), out(i, j), 1, 0);
            int ni, nj;
            for (int k = 0; k < 4; k++) {
                ni = i + dx[k];
                nj = j + dy[k];
                if (ni >= 0 && ni < n && nj >= 0 && nj < m && a[ni][nj] == 1) {
                    f.addedge(out(i, j), in(ni, nj), 1, 0);
                }
            }
        }
    int source = n * m * 2, sink = n * m * 2 + 1;
    for (int i = 0; i < m; i++) {
        if (a[0][i] == 1) f.addedge(source, in(0, i), 1, 0);
        if (a[n - 1][i] == 1) f.addedge(out(n - 1, i), sink, 1, 0);
    }

    printf("%d\n", (int)f.maxflow(sink + 1, source, sink));
    fflush(stdout);
}

int main() {
    freopen((testprefix + ".in").c_str(), "r", stdin);
    freopen((testprefix + ".out").c_str(), "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solveTest();
    }
    return 0;
}
