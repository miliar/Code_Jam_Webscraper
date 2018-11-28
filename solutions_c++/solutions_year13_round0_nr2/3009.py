#include<cstdio>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<math.h>
#include<iostream>
#include<ctype.h>
#define ll long long
using namespace std;
double pi=acos(-1.0);
int a[105][105],n,m;
int check(int x,int y)
{
    int tmp=a[x][y],ret1=1,ret2=1;
    for(int j=0;j<m;j++)
        if(a[x][j]>tmp) {ret1=0;break;}
    for(int i=0;i<n;i++)
        if(a[i][y]>tmp) {ret2=0;break;}
    if(ret1+ret2==0) return 0;
    else return 1;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas,k=1;
    scanf("%d",&cas);
    while(cas--)
    {
        memset(a,0,sizeof(a));
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        int ok=1;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
                if(!check(i,j)) {ok=0;break;}
            if(!ok) break;
        }
        if(ok) printf("Case #%d: YES\n",k++);
        else printf("Case #%d: NO\n",k++);
    }
    return 0;
}
