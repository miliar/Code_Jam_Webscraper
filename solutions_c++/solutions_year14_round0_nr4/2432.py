#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

double a[11111],b[11111];

bool vis[11111],used[11111],ok;

int p2=0;
int n;

void dfs(int k,int sc){
    if(sc>=p2)
        p2=sc;

    for(int i=1;i<=n;i++)
    if(vis[i]==false)
    {
        vis[i]=true;
        bool flag=true;
        int mi=-1;
        for(int j=1;j<=n;j++)
        if(used[j]==false)
        {
            if(mi==-1)
                mi=j;
            if(b[j]>=a[i])
            {
                flag=false;
                used[j]=true;
                dfs(k+1,sc);
                used[j]=false;

                break;
            }
        }



        if(flag)
        {
            used[mi]=true;
            dfs(k+1,sc+1);
            used[mi]=false;
        }
        vis[i]=false;
        if(k==n)
            ok=true;

        if(ok)
            return;

    }

}

int main()
{

//freopen("d2.in","r",stdin);
  //  freopen("d2.out","w",stdout);
    int cas,l1,l2,r1,r2;
    //cin>>cas;
    scanf("%d",&cas);
    int tt=0;
    while(cas--){
        tt++;
        memset(vis,false,sizeof(vis));
        memset(used,false,sizeof(used));
        ok=false;
        //cin>>n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%lf",&a[i]);
        for(int j=1;j<=n;j++)
            scanf("%lf",&b[j]);
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);
        l1=l2=1;
        r1=r2=n;
        int p1=0;
        p2=0;
        for(int i=1;i<=n;i++)
        {
            if(b[l2]<=a[l1])
            {
                p1++;
                l1++;
                l2++;
            }
            else
            {
                l1++;
                r2--;
            }
        }

        dfs(1,0);

        printf("Case #%d: ",tt);
        printf("%d %d\n",p1,p2);
    }
    return 0;
}
