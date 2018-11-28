/*#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
#define mxn 10010
#define mxe 200010
typedef pair<int,int> fuck;
int fst[mxn],nxt[mxe],to[mxe],cost[mxe],e;
bool vis[mxn];
int n,k,t;
void init(){
    e=0;
    memset(fst,-1,sizeof fst);
    memset(cost,0,sizeof cost);
}
void add(int u,int v,int c){
    to[e]=v,nxt[e]=fst[u],cost[e]=c,fst[u]=e++;
}
queue <fuck> que;
bool bfs(int m){
    while(!que.empty()) que.pop();
    memset(vis,false,sizeof vis);
    vis[1]=true;
    que.push(fuck(1,0));
    while(!que.empty()){
        fuck x=que.front(); que.pop();
        if(x.second>=k) return false;
        for(int i=fst[x.first]; ~i; i=nxt[i]){
            if(cost[i]>m) continue;
            if(to[i]==t) return true;
            if(!vis[to[i]]){
                vis[to[i]]=true;
                que.push(fuck(to[i],x.second+1));
            }
        }
    }
    return false;
}
int main(){
    int m;
    while(~scanf("%d%d%d%d",&n,&m,&k,&t)){
        init();
        int a,b,c;
        for(int i=0; i<m; i++){
            scanf("%d%d%d",&a,&b,&c);
            add(a,b,c);
            add(b,a,c);
        }
        int l=1,r=1000000;
        int ans=0;
        while( l < r ){
            int mid=( l + r ) >> 1;
            if(bfs(mid)){
                r = mid;
                ans = mid;
            }
            else l=mid+1;
        }
        printf("%d\n",ans);
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define mod 1000000009
int dp[10002][11][11];
bool prime[11][11][11],pri[1002];
void is_prime(){
    memset(pri,true,sizeof pri);
    memset(prime,false,sizeof prime);
    pri[1]=false;
    for(int i=1; i<=1000; i++)
        if(pri[i]){
            for(int j=i<<1; j<=1000; j+=i) pri[j]=false;
            if(i>100) prime[i/100][i/10%10][i%10]=true;
        }
}
int main(){
    is_prime();
    memset(dp,0,sizeof dp);
    for(int i=1; i<10; i++)
        for(int j=0; j<10; j++)
            for(int k=0; k<10; k++)
                if(prime[i][j][k]) dp[3][i][j]++;
    for(int i=4; i<=10000; i++)
        for(int j=1; j<10; j++)
            for(int k=0; k<10; k++)
                for(int l=0; l<10; l++)
                    if(prime[j][k][l])
                       dp[i][j][k]=(dp[i][j][k]+dp[i-1][k][l])%mod;
    int n;
    while(cin>>n){
        int ans=0;
        for(int i=1; i<10; i++)
            for(int j=0; j<10; j++){
                ans+=dp[n][i][j];
                ans%=mod;
            }
        cout<<ans<<endl;
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int dx[]={ -2, -2, -1, -1, 1, 1, 2, 2},dy[]={ -1, 1, -2, 2, -2, 2, -1, 1};
bool vis[27][27];
int N,M;
typedef pair<int,int> P;
P path[900];
int now;
bool flag;
void dfs(int x,int y,int now){
    path[now].first=x;
    path[now].second=y;
    if(now+1==N*M){
        flag=true;
        return ;
    }
    for(int i=0; i<8; i++){
        int nx=x+dx[i],ny=y+dy[i];
        if(nx>=0 && nx<N && ny>=0 && ny<M && vis[nx][ny]==false && flag==false){
        vis[nx][ny]=true;
        dfs(nx,ny,now+1);
        vis[nx][ny]=false;
        }
    }
}
void Output(){
    if(flag){
    for(int i=0; i<N*M-1; i++)
        printf("%c%d",path[i].first+65,path[i].second+1);
    printf("%c%d\n",path[N*M-1].first+65,path[N*M-1].second+1);
    }
    else printf("impossible\n");
}
int main(){
    int T,num=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d %d",&M,&N);
        memset(vis,false,sizeof(vis));
        vis[0][0]=true;
        flag=false;
        dfs(0,0,0);
        ++num;
        printf("Scenario #%d:\n",num);
        Output();
        if(T!=0) cout<<endl;
    }
}

#include <iostream>
#include <cstdio>
using namespace std;
#define mxn 510
#define inf 10000000000
int d[mxn],cost[mxn][mxn];
bool vis[mxn];
int V,E;
void dijkstra(){
    for(int i=0; i<mxn; i++) d[i]=inf;
    memset(vis,false,sizeof(vis));
    d[1]=0;
    while(1){
        int v=-1;
        for(int i=1; i<=V; i++)
            if(!vis[i] && (v==-1 || d[i]<d[v])) v=i;
            if(v==-1) break;
            vis[v]=true;
            for(int i=1; i<=V; i++)
                d[i]=min(d[i],d[v]+cost[v][i]);
    }
}
int main(){
    int num=0;
    while(cin>>V>>E && (V||E)){
        for(int i=0; i<mxn; i++)
            for(int j=0; j<mxn; j++)
                cost[i][j]=inf;
        for(int i=0; i<E; i++){
            int a,b,c;
            cin>>a>>b>>c;
            if(c<cost[a][b]){
            cost[a][b]=c;
            cost[b][a]=c;
            }
        }
        dijkstra();
        double max1=-inf,max2=-inf;
        int mark,mark1,mark2;
        for(int i=1; i<=V; i++){
            if(max1<d[i]){
                max1=d[i]*1.0;
                mark=i;
            }
        }
        for(int i=1; i<=V; i++)
            for(int j=i; j<=V; j++)
                if(cost[i][j]!=inf){
                    if(max2<(d[i]+d[j]+cost[i][j])/2.0){
                        max2=(d[i]+d[j]+cost[i][j])/2.0;
                        mark1=i;
                        mark2=j;
                    }
                }
        ++num;
        cout<<"System #"<<num<<endl;
        if(max1>=max2) printf("The last domino falls after %.1f seconds, at key domino %d.\n",max1,mark);
        else printf("The last domino falls after %.1f seconds, between key dominoes %d and %d.\n",max2,mark1,mark2);
        cout<<endl;
        }
    return 0;
}
#include <iostream>
#include <cstdio>
using namespace std;
#define mxn 510
int d[mxn],cost[mxn][mxn];
bool vis[mxn];
int V,E;
void dijkstra(){
    for(int i=0; i<mxn; i++) d[i]=99999999;
    memset(vis,false,sizeof(vis));
    d[1]=0;
    while(1){
        int v=-1;
        for(int i=1; i<=V; i++)
            if(!vis[i] && (v==-1 || d[i]<d[v])) v=i;
        if(v==-1) break;
        vis[v]=true;
        for(int i=1; i<=V; i++)
            d[i]=min(d[i],d[v]+cost[v][i]);
    }
}
int main(){
    int num=0;
    while(cin>>V>>E && (V||E)){
        for(int i=0; i<mxn; i++)
            for(int j=0; j<mxn; j++)
                cost[i][j]=99999999;
        for(int i=0; i<E; i++){
            int a,b,c;
            cin>>a>>b>>c;
            if(c<cost[a][b]){
                cost[a][b]=c;
                cost[b][a]=c;
            }
        }
        dijkstra();
        double max1=-100000000,max2=-100000000;
        int mark,mark1,mark2;
        for(int i=1; i<=V; i++){
            if(max1<d[i]){
                max1=d[i]*1.0;
                mark=i;
            }
        }
        for(int i=1; i<=V; i++)
            for(int j=i; j<=V; j++)
                if(cost[i][j]!=99999999){
                    if(max2<(d[i]+d[j]+cost[i][j])/2.0){
                        max2=(d[i]+d[j]+cost[i][j])*1.0/2.0;
                        mark1=i;
                        mark2=j;
                    }
                }
        ++num;
        cout<<"System #"<<num<<endl;
        if(max1>=max2) printf("The last domino falls after %.1f seconds, at key domino %d.\n",max1,mark);
        else printf("The last domino falls after %.1f seconds, between key dominoes %d and %d.\n",max2,mark1,mark2);
        cout<<endl;
    }
    return 0;
}
#include <iostream>
#include <cstdio>
using namespace std;
using namespace std;
#define mxn 110
int d[mxn],cost[mxn][mxn];
bool vis[mxn];
int level[mxn];
int M,V,E;
void dijkstra(){
    for(int i=0; i<mxn; i++) d[i]=99999999;
    memset(vis,false,sizeof(vis));
    d[V+1]=0;
    for(int i=1; i<=V; i++)
        if(level[i]-level[1]<=M && level[1]-level[i]<=M) d[i]=cost[V+1][i];
    while(1){
        int v=-1;
        for(int i=1; i<=V+1; i++)
            if(!vis[i] && (v==-1 || d[i]<d[v])) v=i;
        if(v==-1) break;
        vis[v]=true;
        for(int i=1; i<=V+1; i++)
            if(level[i]-level[1]<=M && level[1]-level[i]<=M && level[i]-level[v]<=M && level[v]-level[i]<=M )
            d[i]=min(d[i],d[v]+cost[v][i]);
    }
}
int main(){
    while(cin>>M>>V){
        for(int i=0; i<mxn; i++)
            for(int j=0; j<mxn; j++)
                cost[i][j]=99999999;
        for(int i=1; i<=V; i++){
            int c;
            cin>>cost[V+1][i]>>level[i]>>c;
                int v,edge;
                for(int j=0; j<c; j++){
                    cin>>v>>edge;
                    cost[i][v]=edge;
                }
            }
        dijkstra();
        cout<<d[1]<<endl;
    }
    return 0;
}

#include<iostream>
#include<cstring>
const int N=1010;
const int inf=99999999;
using namespace std;

int edge[N][N];
int dist[N];
int vis[N],s[N];
int n,m;

void Dijkstra(){
    memset(vis,false,sizeof(vis));
    memset(dist, 0x3f,sizeof(dist));
    dist[2]=0;
    while(true){
        int v=-1;
        for(int i=1; i<=n; ++i)
            if( !vis[i] && (v==-1 || dist[i]<dist[v])) v=i;
        if(v==-1) break;
        vis[v]=true;
        for(int i=1; i<=n; i++)
            dist[i]=min(dist[i],dist[v]+edge[v][i]);
    }
}
//记忆化搜索
int dfs(int x){
    if(s[x]) return s[x];
    if(x==2) return 1;
    for(int i=1; i<=n; i++){
        if(edge[x][i] != 99999999 && dist[i]<dist[x]){
            s[x]+=dfs(i);
        }
    }
    return s[x];
}

int main(){
    while(scanf("%d",&n)!=EOF){
        if(n==0)break;
        scanf("%d",&m);
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(i==j) edge[i][j]=0;
                else  edge[i][j]=99999999;
            }
        }
        int a,b,dis;
        for(int i=1;i<=m;i++){
            scanf("%d%d%d",&a,&b,&dis);
            if(edge[a][b]>=dis){
                edge[a][b]=edge[b][a]=dis;
            }
        }
        Dijkstra();
        //for(int i=1; i<=n; i++) cout<<dist[i]<<endl;
        memset(s,0,sizeof(s));
        int count=dfs(1);
        printf("%d\n",count);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
double height[1005];
int dp[2][1005];
int main(){
    int n;
    while(cin>>n){
        for(int i=0; i<n; ++i)
            cin>>height[i];
        memset(dp,0,sizeof(dp)/sizeof(int));
        for(int i=0; i<n; i++){
            dp[0][i]=1;
            for(int j=0; j<i; j++)
                if(height[j]<height[i]) dp[0][i]=max(dp[0][j]+1,dp[0][i]);
        }
        for(int i=n-1; i>=0; i--){
            dp[1][i]=1;
            for(int j=i; j<n; j++)
                if(height[j]<height[i]) dp[1][i]=max(dp[1][j]+1,dp[1][i]);
        }
        int ans=dp[0][n-1];
        for(int i=0; i<n; i++)
            for(int j=i+1; j<n; j++)
                ans=max(ans,dp[0][i]+dp[1][j]);
        cout<<n-ans<<endl;
    }
    return 0;
}

#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int n,k;
struct edge{
    int cost;
    int from,to;
}e[10010];
int par[105];
int cmp(edge x, edge y){
    return x.cost < y.cost;
}
void init(){
    for(int i=1; i<=n; i++)
        par[i]=i;
}
int find(int x){
    return par[x]==x ? x : par[x]=find(par[x]);
}
void unit(int x, int y){
    x=find(x);
    y=find(y);
    if(x!=y) par[x]=y;
}
int Kruskal(){
    int ans=0;
    sort(e,e+k,cmp);
    for(int i=0; i<k; ++i){
        int x=find(e[i].from),y=find(e[i].to);
        if(x!=y){
            ans+=e[i].cost;
            unit(x,y);
        }
    }
    return ans;
}
int main(){
    while(scanf("%d",&n)!=EOF){
        k=0;
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++){
                cin>>e[k].cost;
                if(i!=j){
                    e[k].from=i,e[k].to=j;
                    k++;
                }
            }
        init();
        int m;
        scanf("%d",&m);
        int x,y;
        for(int i=0; i<m; i++){
            cin>>x>>y;
            x=find(x),y=find(y);
            if(x!=y) unit(x,y);
        }
        cout<<Kruskal()<<endl;
    }
    return 0;
}



#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
using namespace std;
#define mxe 10010
#define mxn 101
#define INF 0x3f3f3f3f
int fst[mxn],nxt[mxe],to[mxe],length[mxe],toll[mxe],e;
int n,cost;
struct node{
    int n,d,t;
    bool operator < (const struct node a)const{
        if(a.d==d) return a.t < t;
        return a.d < d;
    }
};
void add(int u,int v,int l,int t){
    to[e]=v,nxt[e]=fst[u],length[e]=l,toll[e]=t,fst[u]=e++;
}
void bfs(){
    priority_queue <node> q;
    node start;
    int res = INF;
    while (!q.empty()) q.pop();
    start.n=1,start.d=0,start.t=0;
    q.push(start);
    while(!q.empty()){
        node x,y;
        x=q.top();q.pop();
        if(x.n==n){
            res=x.d;
            break;
        }
        for(int i=fst[x.n]; ~i; i=nxt[i]){
            int v=to[i],l=length[i],t=toll[i];
            if(x.t+t <= cost){
                y.n=v,y.d=x.d+l,y.t=x.t+t;
                q.push(y);
                
            }
        }
    }
    if(res==INF) cout<<"-1"<<endl;
    else cout<<res<<endl;
}

int main(){
    int m;
    while(scanf("%d %d %d",&cost,&n,&m)!=EOF){
        int u,v,l,t;
        memset(fst,-1,sizeof fst);
        e=0;
        for(int i=0; i<m; i++){
            scanf("%d %d %d %d",&u,&v,&l,&t);
            add(u,v,l,t);
        }
        bfs();
    }
    return 0;
}

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace  std;
#define mxn 1010
int map[mxn][mxn],d[mxn],vis[mxn];
int n,m;
void dijkstra(){
    for(int i=1; i<=n; ++i)
        d[i]=map[1][i];
    memset(vis,false,sizeof vis);
    while( 1 ){
        int v=-1;
        for(int i=1; i<=n; i++)
            if( !vis[i] && (v==-1 || d[i] > d[v])) v=i;
        if(v==-1) break;
        vis[v]=true;
        for(int i=1; i<=n; i++)
            if(d[i] < min(d[v],map[v][i]))  d[i]=min(d[v],map[v][i]);
    }
}
int main(){
    int T,now;
    scanf("%d",&T);
    now=T;
    while(T--){
        scanf("%d %d",&n,&m);
        int a,b,c;
        memset(map,-1,sizeof map);
        for(int i=0; i<m; i++){
            scanf("%d %d %d",&a,&b,&c);
            map[a][b]=map[b][a]=c;
        }
        dijkstra();
        printf("Scenario #%d:\n",now-T);
        printf("%d\n\n",d[n]);
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int d[105],vis[105],a[105][105];
int n;
void dijkstra(){
    memset(d,0x3f,sizeof d);
    memset(vis,false,sizeof vis);
    d[1]=0;
    while (true) {
        int v=-1;
        for(int i=1; i<=n; ++i)
            if( !vis[i] && (v==-1 || d[i] < d[v])) v=i;
        if(v==-1) break;
        vis[v]=true;
        for(int i=-1; i<=n; i++)
            d[i]=min(d[i],d[v]+a[v][i]);
    }
}
int opera(string s){
    int res=0,tmp;
    int n=s.size();
    for(int i=0; i<n; ++i){
                tmp=s[i]-'0';
        for(int j=0; j<n-i-1; j++)
            tmp*=10;
        res+=tmp;
    }
    return res;
}
int main(){
    string s;
    while(cin>>n){
        memset(a,0x3f,sizeof a);
        for(int i=2; i<=n; i++)
            for(int j=1; j<i; j++){
                cin>>s;
                if(s[0]=='x') continue;
                a[j][i]=a[i][j]=opera(s);
            }
        dijkstra();
        sort(d+1,d+n+1);
        cout<<d[n]<<endl;
    }
    return 0;
}
#include <iostream>
#include <cstring>
using namespace std;
int d[50005];
struct edge{
    int from,to;
    int cost;
}e[50005];
int n,max_,min_;
void bellman_ford(){
    bool flag=true;
    while(flag){
        flag=false;
        for(int i=1; i<=n; i++)
            if(d[e[i].to]>d[e[i].from]-e[i].cost){
                d[e[i].to]=d[e[i].from]-e[i].cost;
                flag=true;
            }
        for(int i=min_; i<=max_; i++)
            if(d[i]>d[i-1]+1){
                d[i]=d[i-1]+1;
                flag=true;
            }
        for(int i=max_; i>=min_; i--)
            if(d[i-1]>d[i]){
                d[i-1]=d[i];
                flag=true;
        }
    }
}
int main(){
    while(~scanf("%d",&n)){
        min_=INT_MAX,max_=-1;
        for(int i=1; i<=n; i++){
            scanf("%d %d %d",&e[i].to,&e[i].from,&e[i].cost);
            min_=min(min_,e[i].to);
            max_=max(max_,e[i].from);
            d[i]=0;
            e[i].to--;
        }
        bellman_ford();
        cout<<d[max_]-d[min_-1]<<endl;
    }
    return 0;
}

#include <iostream>
#include <cstring>
#include <queue>
#include <cstdio>
using namespace std;
#define mxn 1000001
#define MAX_INT 0x7fffffff
int fst1[mxn],fst2[mxn],dis[mxn],vis[mxn];
int to1[mxn],to2[mxn],nxt1[mxn],nxt2[mxn],edge1[mxn],edge2[mxn];
queue <int> q;
int n,e1,e2;
void add1(int u,int v,int w){
    to1[e1]=v,nxt1[e1]=fst1[u],edge1[e1]=w,fst1[u]=e1++;
}
void add2(int u,int v,int w){
    to2[e2]=v,nxt2[e2]=fst2[u],edge2[e2]=w,fst2[u]=e2++;
}
void spfa1(){
    for(int i=1; i<=n; i++)
        dis[i]=MAX_INT;
    while(!q.empty()) q.pop();
    memset(vis,0,sizeof vis);
    q.push(1);
    vis[1]=1;
    dis[1]=0;
    while(!q.empty()){
        int x=q.front(); q.pop();
        for(int i=fst1[x]; ~i; i=nxt1[i]){
            if(dis[to1[i]] > dis[x]+edge1[i]){
                dis[to1[i]] = dis[x] + edge1[i];
                if(!vis[to1[i]]){
                    q.push(to1[i]);
                    vis[to1[i]]=1;
                }
            }
        }
    }
}
void spfa2(){
    for(int i=1; i<=n; i++)
        dis[i]=MAX_INT;
    while(!q.empty()) q.pop();
    memset(vis,0,sizeof vis);
    q.push(1);
    vis[1]=1;
    dis[1]=0;
    while(!q.empty()){
        int x=q.front(); q.pop();
        for(int i=fst2[x]; ~i; i=nxt2[i]){
            if(dis[to2[i]] > dis[x]+edge2[i]){
                dis[to2[i]] = dis[x] + edge2[i];
                if(!vis[to2[i]]){
                    q.push(to2[i]);
                    vis[to2[i]]=1;
                }
            }
        }
    }
}
int main(){
    int T,m;
    cin>>T;
    while(T--){
        scanf("%d %d",&n,&m);
        int a,b,c;
        memset(fst1,-1,sizeof fst1);
        memset(fst2,-1,sizeof fst2);
        e1=e2=0;
        for(int i=0; i<m; i++){
            scanf("%d %d %d",&a,&b,&c);
            add1(a,b,c);
            add2(b,a,c);
        }
        spfa1();
        long long sum=0;
        for(int i=1; i<=n; i++)
            sum+=dis[i];
        spfa2();
        for(int i=1; i<=n; i++)
            sum+=dis[i];
        printf("%lld\n",sum);
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <map>
#include <queue>
#include <string>
#include <cstdio>
using namespace std;
map <string,int> m;
struct edge{
    int u,v;
    int start,end;
}e[1100];
int fst[1100],nxt[1000001],to[1000001],kk,edge2[1100];
int dis[1100],que[110000],ans;
bool vis[1100];
const int inf = 1<<30;
int check(int x,int y){
    if((e[x].end<=6 && e[y].start>=18) || (e[y].start < e[x].end && ((e[y].start <=6 && e[x].end <=6)||(e[y].start>=18 && e[x].end>=18))))
        return 1;
    return 0;
}
void add(int u,int v,int w){
    to[kk]=v,nxt[kk]=fst[u],edge2[kk]=w,fst[u]=kk++;
}
void spfa(int s,int k,int n){
    int front,rear;
    front=rear=0;
    for(int i=1; i<n; i++){
        dis[i]=inf,vis[i]=false;
        if(e[i].u == s){
            que[rear++]=i;
            dis[i]=0;
            vis[i]=true;
        }
    }
    while ( front < rear) {
        int pre = que[front++];
        vis[pre]=false;
        for (int i=fst[pre]; ~i; i=nxt[i]){
            int v = to[i];
            if(dis[v] > dis[pre] + edge2[i]){
                dis[v]=dis[pre]+edge2[i];
                if(!vis[v]){
                que[rear++]=v;
                vis[v]=true;
                }
            }
        }
    }
    for(int i=1; i<n; i++)
        if( ans > dis[i] && e[i].v==k){
            ans = dis[i];
        }
}
int main(){
    int T,nc=0;
    cin>>T;
    while(T--){
        kk=0;
        memset(fst,-1,sizeof fst);
        int n,c,d,num=1,len=1;
        m.clear();
        string a,b;
        kk=0;
        cin>>n;
        for(int i=0; i<n; i++){
            cin>>a>>b;
            scanf("%d %d",&c,&d);
            if(!m[a]) m[a]=num++;
            if(!m[b]) m[b]=num++;
            c%=24;
            if((c>=18 && (c+d) <= 30)||(c<=6 && (c+d)<=6)){
                e[len].u=m[a],e[len].v=m[b],e[len].start=c,e[len++].end=(c+d)%24;
            }
        }
        cin>>a>>b;
        printf("Test Case %d.\n", ++ nc);
        if( m[a] == m[b] ){
            printf("Vladimir needs 0 litre(s) of blood.\n");
            continue;
        }
        if(!m[a] || !m[b]){
            printf("There is no route Vladimir can take.\n");
            continue;
        }
        for(int i=1; i<len; i++)
            for(int j=1; j<len; j++)
                if(e[i].v==e[j].u){
                    add(i,j,check(i,j));
        }
        ans=inf;
        spfa(m[a],m[b],len);
        if(ans==inf) printf("There is no route Vladimir can take.\n");
        else printf("Vladimir needs %d litre(s) of blood.\n", ans);
    }
    return 0;
}
 CF 222A
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
struct Point{
    double x;
    double y;
    double angle;
}p[100002];

bool cmp(Point a,Point b){
    return a.angle<b.angle;
}
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; i++) {
        scanf("%lf %lf",&p[i].x,&p[i].y);
        p[i].angle=atan2(p[i].y,p[i].x);
    }
    sort(p,p+n,cmp);
    double ans=2*acos(-1.0);
    p[n].angle=ans+p[0].angle;
    for(int i=0; i<n; i++){
        ans=min(ans,2*acos(-1.0)-fabs(p[i+1].angle-p[i].angle));
    }
    printf("%.10f\n",ans*180.0/acos(-1.0));
    return 0;
}
poj 3685
#include <iostream>
#include <cstdio>
using namespace std;
#define ll long long
ll n;
ll fun(ll i,ll j){
    return i*i+100000*i+j*j-100000*j+i*j;
}
ll search(ll x){
    ll num=0;
    ll l,r,mid;
    for(int i=1; i<=n; i++){
        l=1,r=n+1;
        mid=(l+r)>>1;
        while( l<r ){
            if(fun(mid,i)>=x) r=mid;
            else l=mid+1;
            mid=(l+r)>>1;
        }
        num+=mid-1;
    }
    return num;
}
int main(){
    int T;
    scanf("%d",&T);
    while(T--){
        ll m;
        scanf("%lld %lld",&n,&m);
        ll l,r;
        l=-1e12,r=1e12;
        ll mid=(l+r)>>1;
        while( l<r ){
            if(search(mid)>=m) r=mid;
            else l=mid+1;
            mid=(l+r)>>1;
        }
        printf("%lld\n",mid-1);
    }
    return 0;
}
 5
 5
 3 1 200
 5 3 150
 2 5 160
 4 3 170
 4 2 170
 1 2 2 2 1
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define inf 0x7ffffff
int d[666],used[666];
int cost[666][666],leader[666];
bool flag[666][666];
int n;
void dijkstra(){
    for(int i=0; i<=n; i++)
        d[i]=inf,used[i]=0;
    d[1]=0;
    while( true ){
        int v=-1;
        for(int i=1; i<=n; i++)
            if(!used[i] && (v==-1 || d[i]<d[v])) v=i;
        if(v==-1) break;
        used[v]=1;
        for(int i=1; i<=n; i++)
            d[i]=min(d[i],d[v]+cost[v][i]);
    }
}
int main(){
    int m;
    while(scanf("%d",&n) && n){
        scanf("%d",&m);
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++)
                cost[i][j]=inf;
        for(int i=0; i<m; i++){
            int a,b,c;
            scanf("%d %d %d",&a,&b,&c);
            if(cost[a][b]>c){
                cost[a][b]=cost[b][a]=c;
            }
        }
        for(int i=1; i<=n; i++) scanf("%d",&leader[i]);
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++)
                if(cost[i][j]!=inf){
                    if(leader[i]!=leader[j]){
                        if(leader[i]==1) cost[j][i]=inf;
                        else cost[i][j]=inf;
                    }
                }
        dijkstra();
        if(d[2]<inf) cout<<d[2]<<endl;
        else cout<<"-1"<<endl;
    }
    return 0;
}

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define mxn 1000000
using namespace std;
int a[mxn],b[mxn];
int main(){
    int n,MIN;
    while(~scanf("%d %d",&n,&MIN)){
        for(int i=0; i<n; i++) scanf("%d",&a[i]);
        for(int i=0; i<n; i++) scanf("%d",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int worst=0;
        //for(int i=0; i<n; i++)
          //  if(a[i]+b[i]>=MIN) worst++;
        int temp=0;
        for(int i=0,j=n-1; i<n && j>=0; i++)
            if(a[i]+b[j]>=MIN){
                temp++;
                j--;
            }
        worst=max(worst,temp);
        temp=0;
        for(int i=0,j=n-1; i<n && j>=0; i++)
            if(a[j]+b[i]>=MIN){
                temp++;
                j--;
            }
        worst=max(worst,temp);
        printf("1 %d\n",worst);
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int first[100],second[100],third[100],arr[101];
int a,b,c;
int main(){
    int n,negative,zero;
    while(cin>>n){
        a=b=c=0;
        for(int i=0; i<n; i++){
            cin>>arr[i];
            if(arr[i]<0) first[a++]=arr[i];
            if(arr[i]>0) second[b++]=arr[i];
            if(arr[i]==0) third[c++]=arr[i];
        }
        if(b==0){
            second[0]=first[a-2];
            second[1]=first[a-1];
            b+=2,a-=2;
        }
        if( a%2==0 ){
            third[c++]=first[a-1];
            a--;
        }
        sort(first,first+a);
        sort(second,second+b);
        sort(third,third+c);
        cout<<a;
        for(int i=0; i<a; i++) cout<<" "<<first[i];
        cout<<endl;
        cout<<b;
        for(int i=0; i<b; i++) cout<<" "<<second[i];
        cout<<endl;
        cout<<c;
        for(int i=0; i<c; i++) cout<<" "<<third[i];
        cout<<endl;
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
using namespace std;
#define inf 1<<25
int fst[101],nxt[2001],w[2001],to[2001];
int e,C,R,Q;
int dis[101],price[101],path[101][101];
bool used[101];

void add(int u,int v,int cost){
    to[e]=v,nxt[e]=fst[u],w[e]=cost,fst[u]=e++;
}

void spfa(int s){
    queue <int> que;
    while(!que.empty()) que.pop();
    //memset(used,false,sizeof used);
    for(int i=1; i<=C; i++) dis[i]=inf;
    que.push(s);
    //used[s]=true;
    dis[s]=0;
    while(!que.empty()){
        int u = que.front();
        que.pop();
        used[u]=false;
        for(int i=fst[u]; ~i; i=nxt[i])
            if(dis[to[i]]>dis[u]+w[i] && price[to[i]]<=price[s]){
                dis[to[i]]=dis[u]+w[i];
                if(!used[to[i]]){
                    que.push(to[i]);
                    used[to[i]]=true;
            }
        }
    }
    for(int i=1; i<=C; i++)
        path[s][i]=dis[i];
}
int main(){
    int test=0;
    while(scanf("%d %d %d",&C,&R,&Q) && C+R+Q){
        memset(fst,-1,sizeof fst);
        for(int i=1; i<=C; i++) scanf("%d",&price[i]);
        int a,b,c;
        e=0;
        for(int i=0; i<R; i++){
            scanf("%d %d %d",&a,&b,&c);
            add(a,b,c);
            add(b,a,c);
        }
        for(int i=1; i<=C; i++)
            spfa(i);
        if(test) printf("\n");
        test++;
        printf("Case #%d\n",test);
        for(int i=1; i<=Q; i++){
            int from,to;
            scanf("%d %d",&from,&to);
            int ans=inf;
            for(int i=1; i<=C; i++){
                if(path[i][from]==inf || path[i][to]==inf) continue;
                ans=min(ans,path[i][from]+path[i][to]+price[i]);
            }
            if(ans==inf) printf("-1\n");
            else printf("%d\n",ans);
            
        }
    }
    return 0;
}
#include <iostream>
#include <cstring>
using namespace std;
int dp[100010],w[10001],v[10001];
int power_2(int n){
    int ret=2,ans=1;
    while(n){
    if( n & 1 ) ans*=ret;
    ret*=ret;
    n>>=1;
    }
    return ans;
}
int main(){
    int V;
    while(~scanf("%d",&V)){
        int N,n,d;
        memset(dp,0,sizeof dp);
        scanf("%d",&N);
        int num=0;
        for(int i=1; i<=N; i++){
            scanf("%d %d",&n,&d);
            int k=0;
            while (true) {
                if(n-power_2(k+1)+1<=0) break;
                k++;
            }
            for(int i=0; i<k; i++){
                int f=power_2(i);
                num++;
                v[num]=d*f;
            }
            num++;
            int f=n-power_2(k)+1;
            v[num]=d*f;
        }
        for(int i=1; i<=num; i++)
            for(int j=V; j>=v[i]; j--)
                dp[j]=max(dp[j],dp[j-v[i]]+v[i]);
        printf("%d\n",dp[V]);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
#define mxn 301
#define mxe 95000
#define inf 0x3f3f3f3f
int fst[mxn],d[mxn],cur[mxn],s,t,c;
struct edge{
    int from,to;
    int cap,flow;
    int nxt;
    void set(int ff,int tt,int cc,int fl,int nn){
        from=ff,to=tt,cap=cc,flow=fl,nxt=nn;
    }
};
edge e[mxe];
void init(){
    memset(fst,-1,sizeof fst);
    c=0;
}
void add(int u,int v,int cap){
    e[c].set(u,v,cap,0,fst[u]),fst[u]=c++;
}
bool bfs(){
    queue <int> que;
    memset(d,-1,sizeof d);
    que.push(s);
    d[s]=0;
    while(!que.empty()){
        int u=que.front();
        que.pop();
        for(int i = fst[u]; ~i; i=e[i].nxt){
            int v=e[i].to;
            if( d[v]==-1 && e[i].cap > e[i].flow){
                d[v] = d[u] + 1;
                que.push(v);
            }
        }
    }
    return d[t] != -1;
}
int dfs(int x,int a){
    if( x==t || a==0 ) return a;
    int f,flow=0;
    for(int &i = cur[x]; ~i; i=e[i].nxt){
        if( i==inf ) i=fst[x];
        if( i==-1 ) break;
        int v=e[i].to;
        if( d[v]==d[x]+1 && (f = dfs(v,min(a,e[i].cap-e[i].flow)))>0){
            a-=f,e[i^1].flow-=f;
            e[i].flow+=f,flow+=f;
            if(!a) break;
        }
    }
    return flow;
}
int dinic(){
    int flow=0;
    while(bfs()){
        memset(cur,0x3f,sizeof cur);
        flow+=dfs(s,inf);
    }
    return flow;
}
int main(){
    int n,m;
    while(scanf("%d %d",&n,&m) && n + m){
        init();
        int x;
        for(int i=1; i<=n; i++) {
            scanf("%d",&x);
            if(x){
                add(0,i,1);
                add(i,0,1);
            }
            if(!x){
                add(n+1,i,1);
                add(i,n+1,1);
            }
        }
        int a,b;
        for(int i=0; i<m; i++){
            scanf("%d %d",&a,&b);
            add(a,b,1);
            add(b,a,1);
        }
        s=0,t=n+1;
        cout<<dinic()<<endl;
    }
    return 0;
}
#include<iostream>
#include<cstring>
#include<cstdio>
#include<set>
#include<algorithm>
#include<vector>
#include<cstdlib>


#define inf 0xfffffff
#define CLR(a,b) memset((a),(b),sizeof((a)))

using namespace std;
int const nMax = 110;
typedef int LL;
typedef pair<LL,char> pij;

int du[7];
struct edge{
    bool vis;
    int u,v;
};

edge e[nMax];
vector<int> a[7];
vector<pij> st;

void dfs(int u){
    int v;
    for(int i=0;i<a[u].size();i++)if(!e[v=a[u][i]].vis){
        e[v].vis=true;
        if(u==e[v].u){
            dfs(e[v].v);
            st.push_back(pij(v+1,'+'));
        }else {
            dfs(e[v].u);
            st.push_back(pij(v+1,'-'));
        }
    }
    return ;
    
}

int n;
int main()
{
    CLR(du,0);
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d%d",&e[i].u,&e[i].v);
        e[i].vis=false;
        du[e[i].u]++;du[e[i].v]++;
        a[e[i].u].push_back(i);
        a[e[i].v].push_back(i);
    }
    int k=0;
    for(int i=0;i<=6;i++)k+=(du[i]&1);
    if((k!=0&&k!=2))puts("No solution");
    else {
        st.clear();
        if(k){
            for(int i=0;i<=6;i++)if(du[i]%2){
                dfs(i);
                break;
            }
        }else  {
            for(int i=0;i<=6;i++){
                if(du[i]){
                    dfs(i);
                    break;
                }
            }
        }
        if(st.size()<n)puts("No solution");
        else {
            for(int i=st.size()-1;i>=0;i--)printf("%d %c\n",st[i].first,st[i].second);
        }
    }
    return 0;
}


树dp
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;
#define mxn 10010
int bc[mxn],father[mxn],parlen[mxn],dis[mxn][3];
int n;
vector<int> tree[mxn];
void readin(){
    int a,b;
    for(int i=0; i<=n; i++) tree[i].clear();
    for(int i=2; i<=n; i++){
        scanf("%d%d",&a,&b);
        tree[a].push_back(i);
        father[i]=a;
        parlen[i]=b;
    }
    memset(bc,0,sizeof bc);
    dis[0][0]=dis[0][1]=dis[0][2]=0;
    father[1]=parlen[1]=0;
}

void dfs1(int u){
    dis[u][0]=0;
    for(int i=0; i<tree[u].size(); i++){
        int v=tree[u][i];
        int len=parlen[v];
        dfs1(v);
        if(dis[u][0]<dis[v][0]+len){
            dis[u][0]=dis[v][0]+len;
            bc[u]=v;
        }
    }
    dis[u][1]=0;
    for(int i=0; i<tree[u].size(); i++){
        int v=tree[u][i];
        int len=parlen[v];
        if(v == bc[u]) continue;
        dis[u][1]=max(dis[u][1],dis[v][0]+len);
    }
}

void dfs2(int u){
    dis[u][2]=0;
    if(u == bc[father[u]])
        dis[u][2]=max(dis[u][2],dis[father[u]][1]);
    else
        dis[u][2]=max(dis[u][2],dis[father[u]][0]);
    dis[u][2]=max(dis[u][2],dis[father[u]][2]);
    dis[u][2]+=parlen[u];
    for(int i=0; i<tree[u].size(); i++){
        int v=tree[u][i];
        dfs2(v);
    }
}
int main(){
    while(~scanf("%d",&n)){
        readin();
        dfs1(1);
        dfs2(1);
        for(int i=1; i<=n; i++){
            printf("%d\n",max(dis[i][0],dis[i][2]));
        }
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
#define mxn 15005
int w[mxn],l[mxn],p[mxn],s[mxn];
priority_queue< pair<int,int> > heap;
int n;
int main(){
    while(~scanf("%d",&n)){
        s[0]=0;
        for(int i=1; i<=n; i++){
            scanf("%d%d%d",&w[i],&l[i],&p[i]);
            s[i]=s[i-1]+w[i];
        }
        int cost=0,start=0,ans=0x3f3f3f3f;
        for(int i=n; i>=1; i--){
            for(;!heap.empty() && heap.top().first > s[i-1]; heap.pop())
                cost-=heap.top().second;
            heap.push(make_pair(s[i]-l[i], p[i]));
            cost+=p[i];
            if(cost<ans){
                ans=cost;
                start=i;
            }
        }
        for(int i=start; i<=n; i++){
            if(s[i]-s[start-1]<=l[i]){
                printf("%d\n",i);
            }
        }
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <ctime>
#include <cmath>
#include <queue>
#include <numeric>
using namespace std;
#define mxn 56000
#define mxe 311000
#define inf 0x3f3f3f3f
#define mod 1000000009
#define eps 1e-5
char pro[110][100];
int a[100010];
int res[28];
int main(){
    int n,m;
    while(~scanf("%d%d",&n,&m)){
        for(int i=1; i<=n; i++)
            for(int j=1; j<=m; j++)
                scanf(" %c",&pro[i][j]);
        int N;
        cin>>N;
        for(int i=0; i<N; i++ ) cin>>a[i];
        memset(res,0,sizeof res);
        int nx=1,ny=1;
        int face=0,now=0,cnt=0;
        while( true ){
            if(pro[nx][ny]=='v') face=1;
            if(pro[nx][ny]=='^') face=3;
            if(pro[nx][ny]=='>') face=0;
            if(pro[nx][ny]=='<') face=2;
            if(pro[nx][ny]=='#') break;
            if(pro[nx][ny]>='A' && pro[nx][ny]<='Z') swap(res[0],res[pro[nx][ny]-'A'+1]);
            if(pro[nx][ny]=='+')  res[0]++;
            if(pro[nx][ny]=='-')  res[0]--;
            if(pro[nx][ny]=='@'){
                if(res[0]==0){
                    face=(face+3)%4;
                }
                else {
                    face=(face+1)%4;
                }
            }
            if(pro[nx][ny]=='!'){ cout<<res[0]<<endl; res[0]=0;}
            if(pro[nx][ny]=='?') {
                res[0]=a[now++];
                if(now >= N) now=N-1;
            }
            if(abs(res[0])>100000){
                cout<<"OVERFLOW ERROR"<<endl;
                break;
            }
            switch(face){
                case 3:
                    nx--;break;
                case 0:
                    ny++;break;
                case 1:
                    nx++;break;
                case 2:
                    ny--;break;
            }
            if(nx<1||nx>n||ny<1|| ny>m){
                cout<<"RUNTIME ERROR"<<endl;
                break;
            }
            cnt++;
            if(cnt>=1000000){
                cout<<"TIME LIMIT EXCEEDED"<<endl;
                break;
            }
        }
    }
    return 0;
}

6.4 1
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define mxn 1000
class book{
public:
    string bookname[mxn];
    int booknum[mxn];
    int price[mxn];
    void display(int x);
    void borrow(int x);
    void restore(int x);
}b;

void book::display(int x){
    cout<<b.bookname[x]<<endl;
    cout<<b.price[x]<<endl;
    cout<<b.booknum[x]<<endl;
}

void book::borrow(int x){
    b.booknum[x]--;
}

void book::restore(int x){
    b.booknum[x]++;
}

int main(){
    int now=0;
    while(cin>>b.bookname[now]){
        cin>>b.price[now]>>b.booknum[now];
        if(b.price[now]<50) b.borrow(now);
        else b.restore(now);
        b.display(now);
        now++;
    }
    return 0;
}
 2
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
class Box{
public:
    int length,width,height;
    void setBox(int l,int w,int h);
    int volume();
}B;

void Box::setBox(int l,int w,int h){
    B.length = l;
    B.width = w;
    B.height = h;
}

int Box::volume(){
    return length*width*height;
}

int main(){
    int a,b,c;
    while(cin>>a>>b>>c){
        B.setBox(a, b, c);
        cout<<B.volume()<<endl;
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
class Student{
    static int total;
    static int count;
public:
    int score;
    void scoretotal(int s);
    static int sum(){
        return total;
    }
    ~Student(){
        cout<<total;
    }
}S;
int Student::total = 0;
int Student::count = 0;
void Student::scoretotal(int s){
    total=Student::sum();
    total+=s;
    count++;
}
int main(){
    int s;
    while(cin>>s){
        S.scoretotal(s);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
#define eps 1e-8
int main(){
    double dp[1010][31][31],p[1010][31],s[1010][31];
    int m,t,n;
    while(~scanf("%d%d%d",&m,&t,&n) && (n+m+t)){
        for(int i=1; i<=t; i++)
            for(int j=1; j<=m; j++)
                scanf("%lf",&p[i][j]);
        memset(dp,0,sizeof dp);
        for(int i=1; i<=t; i++){
            dp[i][0][0]=1.0;
            for(int j=1; j<=m; j++)
                dp[i][j][0]=dp[i][j-1][0]*(1-p[i][j]);
            for(int j=1; j<=m; j++)
                for(int k=1; k<=j; k++)
                    dp[i][j][k]=dp[i][j-1][k]*(1-p[i][j])+dp[i][j-1][k-1]*p[i][j];
            s[i][0]=dp[i][m][0];
            for(int j=1; j<=m; j++)
                s[i][j]=s[i][j-1]+dp[i][m][j];
        }
        double p1=1.0,p2=1.0;
        for(int i=1; i<=t; i++)
            p1*=(s[i][m]-s[i][0]);
        for(int i=1; i<=t; i++)
            p2*=(s[i][n-1]-s[i][0]);
        printf("%.3f\n",p1-p2);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define mxn 10010
#define eps 1e-9
double A[mxn],B[mxn],C[mxn];
double k[mxn],e[mxn];
vector<int> vec[mxn];

bool dfs(int t,int pre){
    int m = vec[t].size();
    A[t]=k[t];
    B[t]=(1-k[t]-e[t])/m;
    C[t]=1-k[t]-e[t];
    double tmp=0;
    for(int i=0; i<m; i++){
        int v=vec[t][i];
        if ( v == pre) continue;
        if ( !dfs(v,t)) return false;
        A[t]+=(1-k[t]-e[t])/m*A[v];
        C[t]+=(1-k[t]-e[t])/m*C[v];
        tmp+=(1-k[t]-e[t])/m*B[v];
    }
    if(fabs(1-tmp)<eps) return false;
    A[t]/=(1-tmp);
    B[t]/=(1-tmp);
    C[t]/=(1-tmp);
    return true;
}

int main(){
    int T;
    int n;
    int u,v;
    int iCase=0;
    scanf("%d",&T);
    while(T--)
    {
        iCase++;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)vec[i].clear();
        for(int i=1;i<n;i++)
        {
            scanf("%d%d",&u,&v);
            vec[u].push_back(v);
            vec[v].push_back(u);
        }
        for(int i=1;i<=n;i++)
        {
            scanf("%lf%lf",&k[i],&e[i]);
            k[i]/=100;
            e[i]/=100;
        }
        printf("Case %d: ",iCase);
        if(dfs(1,-1)&&fabs(1-A[1])>eps)
        {
            printf("%.6lf\n",C[1]/(1-A[1]));
        }
        else printf("impossible\n");
    }
    return 0;
}
#include <iostream>
#include <cstring>
#include <string>
#include <queue>
using namespace std;
#define mxn 22
bool vis[mxn][mxn],vist[mxn*mxn];
int dis[mxn][mxn],num[mxn][mxn],disx[4]={-1,1,0,0},disy[4]={0,0,-1,1};
char map[mxn][mxn];
int n,m,cnt,ans;
struct point{
    int x,y;
    int step;
}pos[mxn*mxn];
bool exam(point x){
    if( x.x < 1 || x.x > n || x.y < 1 || x.y > m) return false;
    return true;
}
void bfs(point s,int p){
    vis[s.x][s.y]=true;
    queue <point> q;
    while(!q.empty()) q.pop();
    q.push(s);
    while(!q.empty()){
        point cur=q.front();
        q.pop();
        if(map[cur.x][cur.y]== 'o' || map[cur.x][cur.y]=='*')
            dis[p][num[cur.x][cur.y]]= cur.step;
        point next;
        next.step=cur.step+1;
        for(int i=0; i<4; i++){
            next.x=cur.x+disx[i];
            next.y=cur.y+disy[i];
            if( exam(next) && !vis[next.x][next.y] && map[next.x][next.y]!='x'){
                q.push(next);
                vis[next.x][next.y]=true;
            }
        }
    }
}
void dfs(int x,int step,int d){
    if(step==cnt){
        ans=min(ans,d);
        return ;
    }
    if(d>ans) return ;
    for(int i=1; i<=cnt; i++){
        if(vist[i]) continue;
        vist[i]=true;
        dfs(i,step+1,d+dis[x][i]);
        vist[i]=false;
    }
}
int main(){
    while(cin>>n>>m && n && m){
        getchar();
        cnt=0;
        memset(pos,0,sizeof pos);
        memset(num,0,sizeof num);
        
        for(int i=1; i<=n; i++){
            gets(map[i]+1);
            for(int j=1; j<=m; j++){
                if(map[i][j]=='o'){
                    pos[++cnt].x=i;
                    pos[cnt].y=j;
                }
            }
        }
    }
}
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cstring>
using namespace std;
int maze[500][500];
int diretion[][2] = {{0,1},{1,0},{0,-1},{-1,0}};
int w,h,u,v;
int mazeGenerator(int y, int x){
    u=w,v=h;
    if(x<1||y<1||x>=u-1||y>=v-1||maze[y][x]) return 0;
    else maze[y][x]=1;
    for (int f=rand()%4, i=0, p=rand() & 1 ? 1 : 3; i<4; ++i,f=(f+p)%4)
        if(mazeGenerator(y+diretion[f][0]*2,x+diretion[f][1]*2)) maze[y+diretion[f][0]][x+diretion[f][1]]=1;
    return 1;
}
int main(){
    cout<<"输入迷宫的宽度和高度"<<endl;
    while(cin>>w>>h){
        memset(maze,0,sizeof maze);
        srand((unsigned)time(NULL));
        int x1=rand()%w,y1=rand()%h,x2=rand()%w,y2=rand()%h,z=rand();
        if(x1==0) x1+=2; if(x1==w-1) x1-=2;
        if(y1==0) y1+=2; if(y1==v-1) y1-=2;
        if(x2==0) x2+=2; if(x2==w-1) x2-=2;
        if(y2==0) y2+=2; if(y2==v-1) y2-=2;
        if(z & 1){
            mazeGenerator(x1,1);
            maze[x1][0] = maze[x2][u-1] = 1;
            if(w % 2 == 0) maze[x2][u-2]=maze[x2-1][u-2]=1;
            else if(h % 2 == 0) maze[x2][u-2]=maze[x2][u-3]=1;
        }
        else{
            mazeGenerator(1,y1);
            maze[0][y1] = maze[v-1][y2] = 1;
            if(w % 2 == 0) maze[v-2][y2]=maze[v-2][y2-1]=1;
            else if(h % 2 == 0) maze[v-2][y2]=maze[v-3][y2]=1;
            
        }
        for (int y=0; y<v; ++y,cout<<endl)
            for (int x=0; x<u; ++x)
                printf("%s ", maze[y][x] ? "." : "#" );
    }
    return 0;
}
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define sz(x) ((int) (x).size())
const int INF = 11111;
int f[INF], flag;
string s;
int main() {
    cin >> s;
    int s1 = 0, s2 = 0, len = s.size() - 1;
    for (int i = 0; i <= len; i++) {
        if (s[i] == '(')		f[i] = s1++;
        else     			f[i] = s2++;
    }
    for (int i = len, t; i >= 0; i--) {
        if (s[i] == ')') t = i;
        else if (f[t] < f[i]) {
            swap (s[len], s[i]);
            reverse (s.begin() + i + 1, s.end() );
            flag = 1;
            break;
        }
    }
    if (flag == 0)	cout << "No solution";
    else          		cout << s;
}
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
#define mxn 202
#define inf 0x3f3f3f3f
int fst[mxn],d[mxn],cur[mxn],s,t,c;
struct edge{
    int u,v,cap,flow,nxt;
    void set(int uu,int vv,int cc,int ff,int nn){
        u=uu,v=vv,cap=cc,flow=ff,nxt=nn;
    }
};
edge e[mxn << 1];
void init(){
    memset(fst,-1,sizeof fst);
    c=0;
}
void add(int u,int v,int cap){
    e[c].set(u,v,cap,0,fst[u]),fst[u]=c++;
    e[c].set(v,u,0,0,fst[v]),fst[v]=c++;
}
bool bfs(){
    memset(d,-1,sizeof d);
    queue <int> q;
    q.push(s);
    d[s]=0;
    while(!q.empty()){
        int u = q.front(); q.pop();
        for(int i = fst[u]; ~i; i=e[i].nxt){
            int v=e[i].v;
            if( d[v]== -1 && e[i].cap > e[i].flow ){
                d[v] = d[u] + 1;
                q.push(v);
            }
        }
    }
    return d[t] != -1;
}
int dfs(int x,int a){
    if( x==t || a==0 ) return a;
    int f,flow=0;
    for(int &i= cur[x]; ~i; i = e[i].nxt){
        if( i == inf ) i=fst[x];
        if( i == -1 ) break;
        int v = e[i].v;
        if( d[v] == d[x]+1 && (f = dfs(v,min(a,e[i].cap-e[i].flow))) > 0){
            a-=f,e[i ^ 1].flow-=f;
            e[i].flow+=f,flow+=f;
            if(!a) break;
        }
    }
    return flow;
}
int dinic(){
    int flow = 0;
    while(bfs()){
        memset(cur,0x3f,sizeof cur);
        flow += dfs(s,inf);
    }
    return flow;
}
int main(){
    int n,m;
    while(cin>>n>>m){
        init();
        for(int i=0; i<n; i++){
            int a,b,c;
            cin>>a>>b>>c;
            add(a,b,c);
        }
        s=1,t=m;
        cout<<dinic()<<endl;
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
const int maxn=2000+100;
using namespace std;
char s1[maxn],s2[maxn];
int dp[maxn][maxn];
int n,m;
int solve(int i) {
    int top=m,ans=0;
    if(i<m) return maxn;
    while(top&&i) {
        if(s1[i]==s2[top]) top--;
        else ans++;
        i--;
    }
    if(top) return maxn;
    else return ans;
}
int main() {
    scanf("%s%s",s1+1,s2+1);
    n=strlen(s1+1);
    m=strlen(s2+1);
    for(int i=0;i<=n;i++)
        for(int j=i+1;j<=n;j++)
            dp[i][j]=-maxn;//j>i不可能有值，赋以无穷小，防止被取到
    for(int i=1;i<=n;i++) {
        int k=solve(i);
        for(int j=0;j<=i;j++) {
            dp[i][j]=max(dp[i-1][j],dp[i][j]);
            if(j>=k) {
                dp[i][j]=max(dp[i][j],dp[i-m-k][j-k]+1);//前面的j>i赋无穷小就是防止j-k>i-m-k时被取到。
            }
        }
    }
    for(int i=0;i<=n;i++) {
        printf("%d ",dp[n][i]);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
struct city{
    double pos;
    int num;
}c[15005];
double cmp(city x,city y){
    return x.pos<y.pos;
}
int main(){
    int n;
    while(~scanf("%d",&n)){
        int tot=0;
        for(int i=1; i<=n; i++){
            scanf("%lf %d",&c[i].pos,&c[i].num);
            tot+=c[i].num;
        }
        tot/=2; tot++;
        sort(c+1,c+1+n,cmp);
        int now=0;
        for(int i=1; i<=n; i++){
            now+=c[i].num;
            if(now>=tot){
                printf("%.5lf\n",c[i].pos);
                break;
            }
        }
    }
    return 0;
}
#include <iostream>
#include <cstdio>
using namespace std;
bool power_mod(int x,int n,int k){
    int tmp=1;
    while(n){
        if( n & 1 ) tmp=(x*tmp)%k;
        x=(x*x)%k;
        n>>=1;
    }
    if(tmp%k) return false;
    return true;
}
int main(){
    int n,m,k;
    while(~scanf("%d %d %d",&n,&m,&k)){
        int a,ans=0;
        for(int i=0; i<n; i++){
            scanf("%d",&a);
            if(power_mod(a, m, k)) ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
#include<cstdio>
#include<cmath>
#include<cstring>
#include<ctime>

#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<set>
using namespace std;
int data[]={0,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1};
int mon[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int main(){
    int n,m;
    while(~scanf("%d %d",&n,&m)){
        int ans=0;
        if(m<1 || m>12 ) printf("Impossible\n");
        else if(n<1 || n>mon[m]) printf("Impossible\n");
        else{
            for(int i=1; i<m; i++) ans+=mon[i];
            ans+=n;
            printf("%d\n",data[ans]);
        }
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int sprime[]={0,3,5,11,17,31,41,59,67,83,109,127,157,179,191,211,241,277,283,331,353,367,401,431,461,509,547,563,587,599,617,709,739,773,797,859,877,919,967,991,1031,1063,1087,1153,1171,1201,1217,1297,1409,1433,1447,1471,1499,1523,1597,1621,1669,1723,1741,1787,1823,1847,1913,2027,2063,2081,2099,2221,2269,2341,2351,2381,2417,2477,2549,2609,2647,2683,2719,2749,2803,2897,2909,3001,3019,3067,3109,3169,3229,3259,3299,3319,3407,3469,3517,3559,3593,3637,3733,3761,3911,3943,4027,4091,4133,4153,4217,4273,4339,4397,4421,4463,4517,4549,4567,4663,4759,4787,4801,4877,4933,4943,5021,5059,5107,5189,5281,5381,5441,5503,5557,5623,5651,5701,5749,5801,5851,5869,6037,6113,6217,6229,6311,6323,6353,6361,6469,6599,6653,6661,6691,6823,6841,6863,6899,7057,7109,7193,7283,7351,7417,7481,7523,7607,7649,7699,7753,7841,7883,8011,8059,8101,8117,8221,8233,8287,8377,8389,8513,8527,8581,8719,8747,8761,8807,8849,8923,8999,9041,9103,9293,9319,9403,9461,9539,9619,9661,9739,9833,9859,9923,9973};
int dp[10001],pre[10001],num[1000];
int main(){
    int W;
    while(~scanf("%d",&W)){
        for(int i=0; i<=10000; i++) dp[i]=99999999;
        dp[0]=0;
        for(int i=1; i<=201; i++)
            for(int j=sprime[i]; j<=W; j++){
                if(dp[j]>dp[j-sprime[i]]+1){
                    dp[j]=dp[j-sprime[i]]+1;
                    pre[j]=j-sprime[i];
                }
            }
        if(dp[W]==99999999) printf("0\n");
        else {printf("%d\n",dp[W]);
            int now=W,k=0;
            while(now){
                num[k++]=now-pre[now];
                now=pre[now];
            }
            sort(num,num+k);
            printf("%d",num[k-1]);
            for(int i=k-2; i>=0; i--) printf(" %d",num[i]);
            printf("\n");
        }
    }
    return 0;
}

#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main(){
    int A,B;
    while(~scanf("%d %d",&A,&B)){
        if(B==0 || A==0) printf("0\n");
        else {
            if(B>A) swap(A,B);
            int ans=0;
            while(A > 0){
                ans++;
                A-=B;
                B+=B;
            }
            if(A==0) printf("%d\n",ans);
            else printf("-1\n");
        }
    }
    return 0;
}

#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main(){
    int K;
    scanf("%d",&K);
    while(K--){
        int n,a[1005];
        scanf("%d",&n);
        int sum=1;
        for(int i=0; i<n; i++) scanf("%d",&a[i]);
        for(int i=n-1; i>=1; i--){
            sum*=a[i]%9;
            sum++;
        }
        sum%=9;
        sum=(a[0]%9*sum)%9;
        if(sum==0) printf("9\n");
        else printf("%d\n",sum);
    }
    return 0;
}
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    int n, m;
    scanf("%d", &m);
    n = (m + 1) / 2;
    int tmp = gcd(n + 1, 2 * n - 1);
    int tem = (2 * n - 1) / tmp / 2;
    long long ans = (long long)tmp * tem + 1;
    printf("%lld\n", ans);
    return 0;
}
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
#define pi acos(-1.0)
struct point{
    double x;
    double y;
}p[310];

point getpoint(point a,double angle,double k){
    point b;
    b.x=k*(a.x*cos(angle)-a.y*sin(angle));
    b.y=k*(a.x*sin(angle)+a.y*cos(angle));
    return b;
}

double dis(point a,point b){
    return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

double coslaw(double dis,double angle){
    return sqrt(dis*dis/(1-cos(angle))/2.0);
}

int main(){
    int n,num1,num2;
    while(~scanf("%d %d %d",&n, &num1,&num2)){
        scanf("%lf %lf",&p[num1].x,&p[num1].y);
        scanf("%lf %lf",&p[num2].x,&p[num2].y);
        double ang1,ang2,ang;
        ang=pi/n;
        if(num1>num2) {
            swap(num1,num2);
            swap(p[num1].x,p[num2].x);
            swap(p[num1].y,p[num2].y);
        }
        //cout<<ang<<endl;
        ang1=2.0*pi/n*(double)(num2-num1);
        //cout<<ang1<<endl;
        ang2=pi-ang1*2.0;
        //cout<<ang2<<endl;
        double k=sqrt(1/(2.0*(1-cos(ang1))));
        //cout<<k<<endl;
        point x;
        x.x=p[num1].x-p[num2].x;
        x.y=p[num1].y-p[num2].y;
        point o=getpoint(x, ang2, k);
        o.x+=p[num2].x;
        o.y+=p[num2].y;
        //cout<<o.x<<" "<<o.y<<endl;
        for(int i=1; i<n; i++){
            point a;
            int t=(i+num1)%n;
            a.x=p[num1].x-o.x;
            a.y=p[num1].y-o.y;
            double tmp=-2.0*pi*i/n;
            if(t!=num2)
                p[t]=getpoint(a, tmp, 1);
        }
        for(int i=1; i<=n; i++) printf("%.5f %.5f\n",p[i].x,p[i].y);
    }
    return 0;
}
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<queue>
using namespace std;
const int maxn=1010;
struct node//边结构
{
    int v;
    int cost;
    node *next;
} edge[maxn<<1],*head[maxn];
int ptr,pos[maxn][maxn],vis[maxn],dist[maxn];
int n,e,sx,ex;
double dp[maxn][maxn];
queue<int> q;
void adde(int u,int v)
{
    edge[ptr].v=v;
    edge[ptr].next=head[u];
    edge[ptr].cost=1;
    head[u]=&edge[ptr++];
}
void spfa(int s)//算最短路并得到pos[i][j]
{
    int u,v;
    node *p;
    while(!q.empty())
        q.pop();
    memset(vis,0,sizeof vis);
    memset(dist,0x3f,sizeof dist);
    dist[s]=0;
    for(p=head[s];p!=NULL;p=p->next)//先预处理起点周围的点
    {
        v=p->v;
        pos[s][v]=v;
        q.push(v);
        dist[v]=1;
        vis[v]=1;
    }
    while(!q.empty())
    {
        u=q.front();
        vis[u]=0;
        q.pop();
        for(p=head[u];p!=NULL;p=p->next)
        {
            v=p->v;
            if(dist[u]+p->cost<dist[v])
            {
                dist[v]=dist[u]+p->cost;
                pos[s][v]=pos[s][u];//更新最优决策点
                if(!vis[v])
                {
                    q.push(v);
                    vis[v]=1;
                }
            }
            else if(dist[u]+p->cost==dist[v]&&pos[s][u]<pos[s][v])
            {
                pos[s][v]=pos[s][u];
                if(!vis[v])
                {
                    q.push(v);
                    vis[v]=1;
                }
            }
        }
    }
}
void dfs(int u,int v)//计算聪聪在u可可在v。聪聪吃到可可的步数的期望。记忆化搜索
{
    if(dp[u][v]>=0)
        return ;
    int np,cnt=0;
    double sum=0;
    node *p;
    np=pos[pos[u][v]][v];
    if(np==v)
    {
        dp[u][v]=1;
        return;
    }
    for(p=head[v];p!=NULL;p=p->next)
    {
        dfs(np,p->v);
        sum+=dp[np][p->v];
        cnt++;//统计边数
    }
    dfs(np,v);
    sum+=dp[np][v];//加上可可不动的期望
    dp[u][v]=sum/(cnt+1)+1;//走了一步了所以加1
}
int main()
{
    int i,j,a,b;
    
    while(~scanf("%d%d",&n,&e))
    {
        scanf("%d%d",&sx,&ex);
        ptr=0;
        memset(head,0,sizeof head);
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
                dp[i][j]=-1;
        for(i=0;i<e;i++)
        {
            scanf("%d%d",&a,&b);
            adde(a,b);
            adde(b,a);
        }
        for(i=1;i<=n;i++)
        {
            dp[i][i]=0;//相遇直接吃掉步数为0
            pos[i][i]=i;
            spfa(i);
        }
        dfs(sx,ex);
        printf("%.3lf\n",dp[sx][ex]);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
#define mxn 1010
int dis[mxn],pos[mxn][mxn];
bool vis[mxn];
double dp[mxn][mxn];
int fst[mxn],nxt[mxn<<1],to[mxn<<1],cost[mxn<<1],e;
void init(){
    e=0;
    memset( fst , -1 ,sizeof fst);
}
void add(int u,int v){
    to[e]=v,nxt[e]=fst[u],cost[e]=1,fst[u]=e++;
}

queue <int> q;

void spfa(int s){
    int u,v;
    while(!q.empty()) q.pop();
    memset(vis,false,sizeof vis);
    memset(dis,0x3f, sizeof dis);
    dis[s]=0;
    for(int i=fst[s]; ~i; i=nxt[i]){
        v=to[i];
        pos[s][v]=v;
        vis[v]=true;
        dis[v]=1;
        q.push(v);
    }
    while(!q.empty()){
        u = q.front();
        vis[u]=0;
        q.pop();
        
    }
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
using namespace std;
int main(){
    double p[130][130],dp[8][130];
    int n;
    while(~scanf("%d",&n) && (n!=-1) ){
        int m = 1 << n ;
        for(int i=0; i<m; i++)
            for(int j=0; j<m; j++)
                scanf("%lf",&p[i][j]);
        memset(dp,0,sizeof dp);
        for(int i=0; i<m; i++)
            dp[0][i]=1.0;
        for(int i=1; i<=n; i++)
            for(int j=0; j<m; j++)
                for(int k=0; k<m; k++)
                    if((j>>(i-1)^1) == k>>(i-1)) dp[i][j]+=dp[i-1][j]*dp[i-1][k]*p[j][k];
        int ans;
        double max=-1;
        for(int i=0; i<m; i++){
            if(dp[n][i]>max){
                max=dp[n][i];
                ans=i+1;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
# include <stdio.h>
# include <string.h>


# define m ((l+r)>>1)
# define lson l,m,p<<1
# define rson m+1,r,p<<1|1


int val[5010 << 2] ;
int a[5010] ;


int query (int L, int R, int l, int r, int p)
{
    if (L == l && R == r) return val[p] ;
    if (R <= m) return query(L,R,lson) ;
    if (L > m) return query (L,R,rson) ;
    return query(L,m,lson) + query(m+1,R,rson) ;
}


void update (int a, int l, int r, int p)
{
    val[p]++ ;
    if (l == r){
        val[p] = 1 ;
        return ;
    }
    if (a <= m) update(a,lson) ;
    else if (a > m) update (a,rson) ;
}


int main ()
{
    int sum, ans, n, i ;
    while (~scanf ("%d", &n))
    {
        memset (val, 0, sizeof(val)) ;
        sum = 0 ;
        for (i = 0 ; i < n ; i++)
        {
            scanf ("%d", &a[i]) ;
            sum += query(a[i]+1, n, 1, n, 1) ;
            update(a[i]+1, 1, n, 1) ;
        }
        ans = sum ;
        for (i = 0 ; i < n - 1 ; i++)
        {
            sum = sum + n-1 - 2*a[i] ;
            if (ans > sum) ans = sum ;
        }
        printf ("%d\n", ans) ;
    }
    return 0 ;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;
#define eps 1e-5
#define mxn 1010
double a[mxn],b[mxn];

int main(){
    int n,k;
    while(cin>>n>>k && (k+n)){
        for(int i=1; i<=n; i++) scanf("%lf",&a[i]);
        for(int i=1; i<=n; i++) scanf("%lf",&b[i]);
        double L=0.0,R=1.0,t[mxn],mid;
        while(R-L>eps){
            double sum=0.0;
            mid=(L+R)/2.0;
            for(int i=1; i<=n; i++)
                t[i]=a[i]-mid*b[i];
            sort(t+1,t+1+n);
            for(int i=k+1; i<=n; i++)
                sum+=t[i];
            if(sum < 0) R=mid;
            else L=mid;
        }
        printf("%.0f\n",mid*100);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
using namespace std;
#define eps 1e-6
#define mxn 1010
#define mxe 10010
#define inf 1<<30

int to[mxe],fst[mxn],cost[mxe],nxt[mxe],e;
double dis[mxn];
int n,m,cunt[mxn],value[mxn];
bool mark[mxn];

void add(int u,int v,int c){
    to[e]=v,nxt[e]=fst[u],cost[e]=c,fst[u]=e++;
}

bool spfa(double mid){
    memset(mark,false,sizeof mark);
    memset(cunt,0,sizeof cunt);
    for(int i=0; i<=n; i++) dis[i]=inf;
    dis[1]=0;
    queue <int> que;
    que.push(1);
    while( !que.empty()){
        int u=que.front();
        que.pop();
        cunt[u]++;
        mark[u]=false;
        if(cunt[u]>n) return true;
        for(int i=fst[u]; ~i; i=nxt[i]){
            int v=to[i],w=cost[i];
            double tmp=mid*w-value[v];
            if(dis[u]+tmp<dis[v]){
                dis[v]=dis[u]+tmp;
                if(!mark[v]){
                    mark[v]=true;
                    que.push(v);
                }
            }
        }
    }
    return false;
}

void solve(){
    double L=0,R=1000,mid;
    while(R-L>eps){
        mid=(L+R)/2;
        if(spfa(mid)){
            L=mid;
        }
        else R=mid;
    }
    printf("%.2f\n",L);
}

int main(){
    while(~scanf("%d%d",&n,&m)){
        memset(fst,-1,sizeof fst);
        for(int i=1; i<=n; i++) scanf("%d",&value[i]);
        e=0;
        for(int i=1; i<=m; i++){
            int u,v,c;
            scanf("%d%d%d",&u,&v,&c);
            add(u,v,c);
        }
        solve();
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
using namespace std;
#define eps 1e-6
#define mxn 20010
#define mxe 10010
#define inf 1<<30
double p[mxn],b[mxn],c[mxn],t[mxn],v[mxn];
int main(){
    int n,k;
    double f;
    while(~scanf("%d%d",&n,&k)){
        scanf("%lf",&f);
    for(int i=0; i<n; i++){
        scanf("%lf%lf%lf",&p[i],&b[i],&c[i]);
        v[i]=p[i]*b[i]/(p[i]+b[i]);
        //printf("%.4lf\n",v[i]);
    }
    double l=0,r=1e10,mid=0;
    while(r-l>eps){
        mid=(l+r)/2;
        double sum=0;
        for(int i=0; i<n; i++)
            t[i]=f*v[i]*c[i]-mid*v[i];
        sort(t,t+n);
        for(int i=0; i<k; i++)
            sum+=t[i];
        if(sum > 0) l=mid;
        else r=mid;
    }
    printf("%.4lf\n",mid);
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
using namespace std;
#define eps 1e-8
#define mxn 110
#define mxe 2010
#define inf 0x3f3f3f3f

struct edge{
    int u,v,nxt;
    double flow,cap;
    void set(int _u,int _v,double _c,double _f,int _n){
        u=_u,v=_v,cap=_c,flow=_f,nxt=_n;
    }
}e[mxe];
int s,t,fst[mxn],cur[mxn],d[mxn],ee;
int from[mxe],to[mxe];
double cost[mxe];
int n,m;
vector<int> ans;
bool used[mxe],vis[mxn];
void init(){
    memset(fst,-1,sizeof fst);
    ee=0;
}
void add(int u,int v,double c){
    e[ee].set(u, v, c, 0, fst[u]), fst[u]=ee++;
    e[ee].set(v, u, 0, 0, fst[v]), fst[v]=ee++;
}

int dcmp(double x){
    if(fabs(x) <= eps) return 0;
    return x < 0 ? -1 : 1;
}

bool bfs(bool flag = 0){
    memset(d,-1,sizeof d);
    queue <int> que;
    que.push(s);
    d[s]=0;
    while(!que.empty()){
        int u=que.front();
        que.pop();
        if(flag) vis[u]=1;
        for(int i=fst[u]; ~i; i=e[i].nxt){
            int v=e[i].v;
            if( d[v] == -1 && dcmp(e[i].cap-e[i].flow) > 0){
                d[v] = d[u] + 1;
                que.push(v);
            }
        }
    }
    return d[t] != -1;
}
double dfs(int x,double a){
    if( x==t || dcmp(a) <= 0 ) return a;
    double f ,flow =0;
    for(int &i =  cur[x]; ~i; i=e[i].nxt){
        if(i == inf)  i = fst[x];
        if(i == -1) break;
        int v = e[i].v;
        if(d[v] == d[x] + 1 && dcmp(f = dfs(v,min(a,e[i].cap-e[i].flow)))>0){
            a -= f,flow += f;
            e[i].flow+=f,e[i^1].flow-=f;
            if(dcmp(a)<=0) break;
        }
    }
    return flow;
}

double dinic(){
    double flow = 0;
    while(bfs(0)){
        memset( cur, 0x3f, sizeof cur);
        flow += dfs(s,inf);
    }
    return flow;
}

void getans(){
    memset( vis, 0, sizeof vis);
    bfs(1);
    for(int i=1; i<=m; i++){
        int u=from[i],v=to[i];
        if(vis[u] ^ vis[v]== 1 && !used[i])
            ans.push_back(i);
    }
    sort(ans.begin(),ans.end());
    printf("%d\n",ans.size());
    for(int i=0; i<ans.size(); i++){
        if(i==0) printf("%d",ans[i]);
        else printf(" %d",ans[i]);
    }
    printf("\n");
}

bool check(double x,bool flag = 0){
    init();
    double res = 0;
    for(int i = 1; i<=m; i++){
        if(dcmp(cost[i]-x)<=0){
            res += cost[i]-x;
            if(flag){
                ans.push_back(i);
                used[i]=true;
            }
        }
        else {
            add(from[i],to[i],cost[i]-x);
            add(to[i],from[i],cost[i]-x);
        }
    }
        res += dinic();
        return res > 0;
}
int main(){
    while(~scanf("%d%d",&n,&m)){
        s=1,t=n;
        for(int i=1; i<=m; i++){
            scanf("%d%d%lf",&from[i],&to[i],&cost[i]);
        }
        memset(used, false, sizeof used);
        double l = 0, r = 1e8, mid = 0;
        while( r-l > eps){
            mid=(l+r)/2;
            if(check(mid)) l=mid;
            else r=mid;
        }
        ans.clear();
        check(mid,1);
        getans();
    }
    return 0;
}
#include <iostream>
#include <cstdio>
using namespace std;
#define mod 1000000007
int main(){
    long long n;
    int t,s=0;
    scanf("%d",&t);
    while(t--){
        s++;
        scanf("%lld",&n);
        if( n&1 ){
                long long j=(n+1)/2;
                j=j%mod*(j%mod)%mod*(n%mod)%mod*(n%mod)%mod*((2+(n-3)/2%mod*(n%mod)%mod)%mod)%mod;
                printf("Case %d: %lld\n",s,j);
            }
        else{
            long long j=n/2;
            j=j%mod*(j%mod)%mod*((n+1)%mod)%mod*((n+1)%mod)%mod*((2+n/2%mod*((n-3)%mod))%mod)%mod;
            printf("Case %d: %lld\n",s,j);
            }
    }
    return 0;
}
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
#define inf 0x3f3f3f3f
int cmp(int x,int y){
    return x > y;
}
int main(){
    int t,s=0;
    scanf("%d",&t);
    while(t--){
        s++;
        int n,a[1010];
        scanf("%d",&n);
        int ans=0;
        memset(a,0,sizeof a);
        
        for(int i=1; i<=n; i++) {
            scanf("%d",&a[i]);
            ans=max(ans,a[i]);
        }
        sort(a+1,a+n+1,cmp);
        int k=inf,tmp=0,res=0,high;
        for(int i=1; i<=n; i++){
            if(i==1 || ans < a[i]) for(int j=0; j<=a[i]; j++){
                if(k > (a[i]+j)/(j+1)+j+res){
                    high=(a[i]+j)/(j+1);
                    k=max((a[i]+j)/(j+1),a[i+1])+j+res;
                    tmp=j;
                }
            }
            res+=tmp;
            ans=min(ans,k);
        }
        printf("Case #%d: %d\n",s,ans);
    }
    return 0;
}*/
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <set>
#include <stack>
#include <cmath>

using namespace std;

string biao = "111011111011011011001011111001101000011011000010";
int main(){
    int caseCnt = 0;
    cin >> caseCnt;
    for (int ci = 1; ci <= caseCnt; ci++) {
        int x,r,c;
        cin >> x >> r >> c;
        if (x == 1) {
            cout << "Case #" << ci << ": " << "GABRIEL" << endl;
        }else{
            if (biao[(r-1)*12+(c-1)*3+x-2] == '1') {
                cout << "Case #" << ci << ": " << "RICHARD" << endl;
            }else{
                cout << "Case #" << ci << ": " << "GABRIEL" << endl;
            }
        }
        
    }
    return 0;
}