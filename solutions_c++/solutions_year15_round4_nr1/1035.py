#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;

int n,m;
int ans;
bool flag;
int xl[110],xr[110];
int yu[110],yd[110];
int f[110][110];
char str[110];
bool check(int i,int j)
{
    if(xl[i] != j ) return false;
    if(xr[i] != j ) return false;
    if(yu[j] != i ) return false;
    if(yd[j] != i ) return false;
    return true;
}
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    int cas=0;
    scanf("%d",&T);
    while(T--)
    {
        flag = false;
        ans = 0 ;
        scanf("%d%d",&n,&m);
        memset(xl,0,sizeof(xl));
        memset(xr,0,sizeof(xr));
        memset(yu,0,sizeof(yu));
        memset(yd,0,sizeof(yd));
        for(int i = 1;i <= n;i++)
        {
            scanf("%s",str);
            for(int j = 0;j < m;j++)
            {
                if(str[j] == '.') f[i][j+1] = 0;
                else
                {
                    if(xl[i] == 0) xl[i] = j+1;
                    xr[i] = j+1;
                    if(yu[j+1] == 0) yu[j+1] = i;
                    yd[j+1] = i;
                    if(str[j] == '^') f[i][j+1] = 1;
                    else if(str[j] == 'v') f[i][j+1] = 2;
                    else if(str[j] == '<') f[i][j+1] = 3;
                    else f[i][j+1] = 4;
                }
            }
        }
        for(int i =1;i<=n;i++)
        for(int j =1;j<=m;j++)
        {
            if(f[i][j] == 1)
            {
                if(yu[j] < i);
                else
                {
                    ans++;
                    if(check(i,j)) flag=true;
                }
            }
            else if(f[i][j] == 2)
            {
                if(yd[j] > i) ;
                else
                {
                    ans++;
                    if(check(i,j)) flag=true;
                }
            }
            else if(f[i][j] == 3)
            {
                if(xl[i] < j) ;
                else{
                    ans++;
                    if(check(i,j)) flag =true;
                }
            }
            else if(f[i][j] == 4)
            {
                if(xr[i] > j) ;
                else
                {
                    ans++;
                    if(check(i,j)) flag =true;
                }
            }
        }
        printf("Case #%d: ",++cas);
        if(flag) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
