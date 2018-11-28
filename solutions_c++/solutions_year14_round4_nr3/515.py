#define FROM_FILE
#define TO_FILE

//-Wl,--stack,52800000
#include <bits/stdc++.h>

using namespace std;

#define foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define MP make_pair
#define PB push_back
#define FF first
#define SS second
#define All(n) (n).begin(), (n).end()

typedef long long int lli;
typedef unsigned long long int ull;
typedef pair<int,int> pii;
typedef pair<lli,lli> pll;
typedef vector<int> vi;

#ifdef FROM_FILE
void* __VERY__LONG__FROM=freopen("in.txt","r",stdin);
#endif

#ifdef TO_FILE
void* __VERY__LONG__TO=freopen("out.txt","w",stdout);
#endif


//const int MOD=1000*1000*1000 + 7;
const lli INF=1000000000000000000ll;

bool tb[510][510];

const int MAXM=600*1000;
const int MAXN=MAXM;
int f[MAXM];//flow yal
int to[MAXM];//sare dige yal
int cap[MAXM];//capacity yal
int prv[MAXM];//yale ghable i ke bara hamoon ras hast
int head[MAXN];//akharin yale rase i

int getNum(int x,int y)
{
    return (x*502+y+1)*2;
}

int ec;

int add_e(int u,int v,int w)//yal ha injoori behtar negah dashte mishe hafeze n^2 nemikhaim
{
    to[ec]=v;prv[ec]=head[u];cap[ec]=w;head[u]=ec;ec++;
    to[ec]=u;prv[ec]=head[v];cap[ec]=0;head[v]=ec;ec++;
}

int n;
int h[MAXN];
int bfq[MAXN];
bool bfs()//a simple BFS
{
    memset(h,-1,sizeof h);
    int p2=0;
    bfq[p2++]=0;
    h[0]=0;
    for(int i=0;i<p2;i++)
    {
        int u=bfq[i];
        if(u==n-1)return true;
        for(int j=head[u];j!=-1;j=prv[j])
        {
            if(f[j]<cap[j] && h[to[j]]==-1)
            {
                h[to[j]]=h[u]+1;
                bfq[p2++]=to[j];
            }
        }
    }
    return false;
}

int pe[MAXN];

lli dfs(int u,lli bala=INF)
{
    if(u==n-1)return bala;
    lli ans=0;
    for(int& i=pe[u];i!=-1 && bala;i=prv[i])
    {
        if(f[i]<cap[i] && h[to[i]]==h[u]+1)//hatman bayad ertefae ras yeki az ma bishtar bashe
        {
            lli y=dfs(to[i],min(bala,(lli)cap[i]-f[i]));
            f[i]+=y;
            f[i^1]-=y;
            ans+=y;
            bala-=y;
            if(!bala)break;//age bala tamoom shod dige bishtar az in nemitoonam az bache ham flow begiram pas bayad felan
            //javabe ans ro return konam ta hala badan age ba ye yale behtari biam toosh edame bedam
        }
    }
    return ans;
}

lli dinic()
{
    lli ans=0;
    while(bfs())//bfs faghat mige vojood dare flow ya na + height ras ha ro set mikone
    {
        for(int i=0;i<n;i++)
            pe[i]=head[i];//eine euleri pointer migirim bara yal ha.
        ans+=dfs(0);
    }
    return ans;
}


int main()
{
	ios::sync_with_stdio(false);
	int tt;
	cin>>tt;
	for(int zz=1;zz<=tt;zz++)
    {
        memset(head,-1,sizeof head);
        ec=0;
        memset(f,0,sizeof f);
        memset(to,0,sizeof to);
        memset(cap,0,sizeof cap);
        memset(prv,0,sizeof prv);
        memset(tb,0,sizeof tb);
//        int f[MAXM];//flow yal
//        int to[MAXM];//sare dige yal
//        int cap[MAXM];//capacity yal
//        int prv[MAXM];//yale ghable i ke bara hamoon ras hast
//        int head[MAXN];//akharin yale rase i
        int w,h,b;
        cin>>w>>h>>b;
        for(int i=0;i<b;i++)
        {
            int x0,x1,y0,y1;
            cin>>x0>>y0>>x1>>y1;
            for(int j=x0;j<=x1;j++)
                for(int k=y0;k<=y1;k++)
                    tb[k][j]=true;
        }
        const int dx[]={-1,0,0,1};
        const int dy[]={0,-1,1,0};
        for(int i=h-1;i>=0;i--)
        {
            for(int j=0;j<w;j++)
            {
                if(tb[i][j])continue;
                add_e(getNum(i,j),getNum(i,j)^1,1);
                for(int k=0;k<4;k++)
                {
                    int tx=i+dx[k];
                    int ty=j+dy[k];
                    if(tx<0 || tx>=h)continue;
                    if(ty<0 || ty>=w)continue;
                    if(!tb[tx][ty])
                    {
                        add_e(getNum(i,j)^1,getNum(tx,ty),1);
//                        add_e(getNum(tx,ty),getNum(i,j),1);
                    }
                }
            }
        }
        for(int i=0;i<w;i++){
            if(!tb[0][i])
                add_e(0,getNum(0,i),1);
            if(!tb[h-1][i])
                add_e(getNum(h-1,i)^1,MAXN-1,1);
        }
        n=MAXN;
        cout<<"Case #"<<zz<<": "<<dinic()<<endl;
    }
    return 0;
}
