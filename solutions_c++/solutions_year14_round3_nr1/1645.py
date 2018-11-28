#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
int T,n,m,p[13][13];
int sta_up[10001][721],sta_dw[10001][721];
int GCD(int xx,int yy)
{
    if(xx%yy==0)return yy;
    return GCD(yy,xx%yy);
}
void DFS_up(int deep,int status,int s)
{
    int i,tp;
    if(deep>(n+1)/2)
    {
        sta_up[status][++sta_up[status][0]]=s;
        return;
    }
    for(i=0;i<n;i++)
        if(!((1<<i)&status))
        {
            tp=status|(1<<i);
            DFS_up(deep+1,tp,s+p[deep][i+1]);
        }
}
void DFS_dw(int deep,int status,int s)
{
    int i,tp;
    if(deep>n)
    {
        sta_dw[status][++sta_dw[status][0]]=s;
        return;
    }
    for(i=0;i<n;i++)
        if(!((1<<i)&status))
        {
            tp=status|(1<<i);
            DFS_dw(deep+1,tp,s+p[deep][i+1]);
        }
}
void Solve()
{
    int i,j;
    cin>>T;
    while(T--)
    {
        cin>>n>>m;
        int jc=1;
        for(i=1;i<=n;i++)
        {
            jc*=i;
            for(j=1;j<=n;j++)
                cin>>p[i][j];
        }
        memset(sta_up,0,sizeof(sta_up));
        memset(sta_dw,0,sizeof(sta_dw));
        DFS_up(1,0,0);
        DFS_dw((n+1)/2+1,0,0);
        for(i=0;i<(1<<n);i++)
            sort(sta_dw[i]+1,sta_dw[i]+sta_dw[i][0]+1);
        int ans=0;
        for(i=0;i<(1<<n);i++)
            for(j=1;j<=sta_up[i][0];j++)
            {
                int to_sta=i^((1<<n)-1),Find=m-sta_up[i][j];
                int l=1,r=sta_dw[to_sta][0],mid;
                //cout<<i<<' '<<to_sta<<' '<<sta_up[i][j]<<' '<<m-sta_up[i][j]<<endl;
                if(sta_dw[to_sta][r]<Find)continue;
                if(sta_dw[to_sta][l]>=Find)
                {
                    ans+=sta_dw[to_sta][0];
                    continue;
                }
                while(l<r)
                {
                    mid=(l+r)/2;
                    if(sta_dw[to_sta][mid]<=Find)r=mid;
                    else l=mid+1;
                }
                ans+=sta_dw[to_sta][0]-l+1;
            }
        if(ans==0)
        {
            cout<<"No solution\n";
            continue;
        }
        int gcd=GCD(jc,ans);
        cout<<jc/gcd<<'/'<<ans/gcd<<endl;
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    Solve();
    return 0;
}
