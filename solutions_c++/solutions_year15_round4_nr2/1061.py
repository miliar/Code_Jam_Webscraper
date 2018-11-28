//#define WYTE
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back(x)
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define PQ priority_queue
#define IT iterator
#define INF 1e18
#define EPS 1e-9
#define MOD 1000000007
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int chk[205],S=203,T=204;
double flow,maxflow,adj[205][205];
bool augment(int node)
{
    if(node==T)return 1;
    if(chk[node])return 0;
    chk[node]=1;
    for(int i=0;i<=T;i++)
    {
        if(adj[node][i]>=flow&&augment(i))
        {
            adj[node][i]-=flow;
            adj[i][node]+=flow;
            return 1;
        }
    }
    return 0;
}
int main()
{
    freopen("B-small-attempt2.in","rb",stdin);
    freopen("output.txt","wb",stdout);
    int t,ii,n,i,j,err;
    double vol,target,rate[133],temp[133],a,b,ans;
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%d %lf %lf",&n,&vol,&target);
        for(i=0;i<n;i++)
        {
            scanf("%lf %lf",rate+i,temp+i);
        }
        for(i=0;i<=T;i++)
        {
            for(j=0;j<=T;j++)
            {
                adj[i][j]=0;
            }
        }
        for(i=0;i<n;i++)
        {
            adj[S][i]=INF;
            adj[i+100][T]=INF;
        }
        err=1;
        for(i=0;i<n;i++)
        {
            if(temp[i]==target)
            {
                err=0;
                adj[i][i+100]=1/(vol/rate[i]);
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i==j)continue;
                if(temp[i]<target&&target<temp[j]&&temp[i]!=temp[j])
                {
                    b=(vol*(target-temp[i]))/(rate[j]*(temp[j]-temp[i]));
                    a=(vol-b*rate[j])/rate[i];
                    err=0;
                    adj[i][j+100]=1/max(a,b);
                }
            }
        }
        printf("Case #%d: ",ii);
        if(err)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            flow=INF;
            maxflow=0;
            for(i=0;i<1000;i++)
            {
                INIT(chk,0);
                if(augment(S))
                {
                    maxflow+=flow;
                }
                else
                {
                    flow/=2;
                }
            }
            printf("%lf\n",1/maxflow);
        }
    }
}
