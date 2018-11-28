#include <bits/stdc++.h>
#define reset(arr,j) memset(arr,j,sizeof(arr));
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define vec vector<LL>
#define LL long long
#define fa(i,n) for(int i=0;i<n;i++)
#define fb(i,n) for(int i=1;i<=n;i++)
#define take(vec,n) for(int i=0;i<n;i++){int a; cin >> a; vec.pb(a);};
#define print(arr,n) fa(i,n) cout << arr[i] << " "; cout << endl;
#define mod(n,m) (n % m + m) % m;
#define fd(i,n) for(int i=n-1;i>=0;i--)
#define vpair vector < pair <int ,int> >
#define Vec(name,size) vector<int> name(size);
#define matrix vector<vector<LL> >
#define initmatrix(m,a,b,x) fa(i,a){ vector<LL> c; m.pb(c); fa(j,b) m[i].pb(x);};
#define printmatrix(M) fa(i,M.size()){ fa(j,M[i].size()) cout << M[i][j].f <<" "; cout << endl;}
#define O4 10005
#define O5 100006
#define O6 1000005
#define O7 10000007
int dx[] = {0,1,-1,0,1,-1,1,-1,-2,2,0,0},dy[] = {1,0,0,-1,-1,1,1,-1,0,0,-2,2};
using namespace std;
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
vector<pair<int,int> > g;
LL N;
LL getReversed(int x){
    stringstream ss;
    ss << x;
    string str = ss.str();
    reverse(str.begin(),str.end());
    stringstream ss2(str);
    LL next;
    ss2 >> next;
    return next;
}
bool visited[1000001];
int bfs(int start){
    reset(visited,0);
    queue<pair<int,int> > q;
    q.push(mp(start,1));
    visited[start] = 1;
    while(q.size()){
        pair<int,int> cur = q.front(); q.pop();
        //cout << cur.f << endl;
        if(cur.f == N)
            return cur.s;
        if(!visited[g[cur.f].f]){
            q.push(mp(g[cur.f].f,cur.s+1));
            visited[g[cur.f].f] = 1;
        }
        if(!visited[g[cur.f].s]){
            q.push(mp(g[cur.f].s,cur.s+1));
            visited[g[cur.f].s] = 1;
        }
    }
    return -1;
}
main(){
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    g.pb(mp(0,0));
    for(int i =1;i <= 1000000;i++){
        g.pb(mp(i+1,getReversed(i)));
    }
    int T;
    cin >> T;
    for(int t = 1;t <= T;t++){
        cin >> N;
        int ans = bfs(1);
        printf("Case #%d: ",t);
        cout << ans << endl;
    }
}
