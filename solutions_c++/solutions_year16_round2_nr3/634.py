/*
 *************************
 Id  : Matrix.code
 Task:
 Date: 2016-04-30

 **************************
 */

#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define forn(i,n)               for( int i=0 ; i < n ; i++ )
#define mp(i,j)                 make_pair(i,j)
#define pb(a)                   push_back((a))
#define SZ(a)                   (int) a.size()
#define all(x)                  (x).begin(),(x).end()
#define gc                      getchar_unlocked
#define PI                      acos(-1.0)
#define EPS                     1e-9
#define xx                      first
#define yy                      second
#define lc                      ((n)<<1)
#define rc                      ((n)<<1|1)
#define db(x)                   cout << #x << " -> " << x << endl;
#define Di(x)                   int x;scanf("%d",&x)
#define min(a,b)                ((a)>(b) ? (b) : (a) )
#define max(a,b)                ((a)>(b) ? (a):(b))
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))

/*************************** END OF TEMPLATE ****************************/

const int N = 1005;
int x[N],y[N];
map<string,int> F,S;
int get(string s,map<string,int> & Map)
{
    if(Map.count(s)) return Map[s];
    int k = Map.size();
    Map[s] = k;
    return k;
}
vector<int> G[N];
int match[N];
bool vis[N];
int rig[N];

bool dfs(int u)
{
    if(vis[u]) return 0;
    vis[u] = 1;
    for(int i = 0; i < G[u].size(); i ++ ) {
        int v = G[u][i];
        if(match[v]==-1 || dfs(match[v])) {
            match[v] = u;
            rig[u] = v;
            return 1;
        }
    }
    return 0;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=0, n ;
    string s1,s2;
    scanf("%d",&t);
    while(t--) {
        scanf("%d",&n);
        for(int i = 0; i < n; i ++ ) {
            cin >> s1>>s2;
            x[i] = get(s1,F);
            y[i] = get(s2,S);
            G[x[i]].push_back(y[i]);
        }
        int cnt = 0;
        ms(match,-1);
        ms(rig,-1);
        for(int i = 0; i < F.size(); i ++) {
            ms(vis,0);
            if(dfs(i)) cnt ++;
        }
        int ho = cnt;
        for(int i = 0; i < F.size(); i ++) {
            if(rig[i] == -1) ho ++;
        }
        for(int i = 0; i < S.size(); i ++) {
            if(match[i] ==-1 ) ho ++;
        }


        printf("Case #%d: %d\n",++cs,n - ho);
        F.clear();
        S.clear();
        for(int i = 0;i < N; i ++) G[i].clear();
    }
    return 0;
}
