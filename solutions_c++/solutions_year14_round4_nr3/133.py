#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<queue>
using namespace std;
#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

typedef pair<int,int> ii;
int w,h,B;


int a[1005],b[1005],c[1005],d[1005];
vector<ii> v[1005];
int len;

int countDS(int aa,int bb)
{
    int a1=a[aa],a2=a[bb],b1=b[aa],b2=b[bb],c1=c[aa],c2=c[bb],d1=d[aa],d2=d[bb];

    if (a2<a1)
    {
        int tmp=c1+(a1-a2);
        a2=c1-(c2-a1);
        c2=tmp;
    }
    if (b2<b1)
    {
        int tmp=d1+(b1-b2);
        b2=d1-(d2-b1);
        d2=tmp;
    }

    int ret=1000000000;
    if (d1>=b2)ret=min(ret,a2-c1-1);
    if (c1>=a2)ret=min(ret,b2-d1-1);
    if (a2>c1&&b2>d1)ret=min(ret,max(a2-c1-1,b2-d1-1));
    return ret;
}

void init()
{
    for (int i=0;i<1005;i++)v[i].clear();
    scanf("%d%d%d",&w,&h,&B);
    for (int k=1;k<=B;k++)
    {
        scanf("%d%d%d%d",&a[k],&b[k],&c[k],&d[k]);
    }

    for (int i=1;i<=B;i++)
    {
        v[0].push_back(ii(a[i],i));
        v[i].push_back(ii(w-c[i]-1,B+1));
    }
    for (int i=1;i<=B;i++)
    {
        for (int j=i+1;j<=B;j++)
        {
            int ds=countDS(i,j);
            v[i].push_back(ii(ds,j));
            v[j].push_back(ii(ds,i));
            //printf("%d %d = %d\n",i,j,ds);
        }
    }

    /*
    for (int i=0;i<w;i++)
    {
        for (int j=0;j<len;j++)
            printf("%d",s[i][j]);
        puts("");
    }*/
}

int dis[1005];
priority_queue<ii,vector<ii>,greater<ii> > pq;
//int dx[8]={1,1,1,0,0,-1,-1,-1};
//int dy[8]={1,0,-1,1,-1,1,0,-1};

void solve()
{
    for (int i=0;i<=B+1;i++)dis[i]=-1;

    while (!pq.empty())pq.pop();

    pq.push(ii(0,0));

    int mx=w;
    while (!pq.empty())
    {
        ii tmp=pq.top();pq.pop();

        int x=tmp.first,y=tmp.second;
        if (dis[y]!=-1)continue;
        dis[y]=x;
        //printf("dis[%d]=%d\n",y,x);
        if (y==B+1){mx=x;break;}

        FO(it,v[y])if (dis[it->second]==-1)
        {
            pq.push(ii(x+it->first,it->second));
        }

    }
    printf("%d\n",mx);

}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int Q;
    scanf("%d",&Q);
    for (int i=1;i<=Q;i++)
    {
        init();
        printf("Case #%d: ",i);
        solve();
    }


    return 0;
}
