#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#define mp make_pair
#define ll long long
#define s second
#define f first
#define pii pair<int,int>
#define pll pair<ll,ll>
using namespace std;
const ll c=110,inf=2000000000ll;
int t,n,m,cnt[c],a[c][c],x,y;
bool vis[c],vis1[c];
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (int u=1; u<=t; u++)
    {
        cin>>n>>m;
        memset(cnt,0,sizeof(cnt));
        x=y=inf;
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++){
                cin>>a[i][j];
                cnt[a[i][j]]++;
                }
        int answ=1;
        for (int k=1; k<101; k++)
            if (cnt[k]){
               memset(vis,0,sizeof(vis));
               memset(vis1,0,sizeof(vis1));
               for (int i=1; i<=n && answ>0; i++)
                   for (int j=1; j<=m && answ>0; j++)
                       if (a[i][j]==k && !vis[i] && !vis1[j]){
                          x=y=1;
                          for (int v=1; v<=n; v++)
                              if (a[v][j]!=k && a[v][j]!=0){
                                 x=0;
                                 break;
                                 }
                          for (int v=1; v<=m; v++)
                              if (a[i][v]!=k && a[i][v]!=0){
                                 y=0;
                                 break;
                                 }
                          if (x==0 && y==0)
                             answ=0;
                          if (x==1)
                             vis1[j]=1;
                          if (y==1)
                             vis[i]=1;
                          }
               for (int i=1; i<=n; i++)
                   for (int j=1; j<=m; j++)
                       if (a[i][j]==k)
                          a[i][j]=0;
               }
        if (answ)
           printf("Case #%d: YES\n",u);
        else printf("Case #%d: NO\n",u);
    }
    //system("pause");
    return 0;
}
