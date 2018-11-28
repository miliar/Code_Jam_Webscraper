/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <math.h>
using namespace std;
typedef long long LL;
#define INF 0x7fffffff
const double eqs=1e-8;
int a[10005];
int flag[10005];
int main()
{
    int t,cnt=0;
    freopen("A-large.in" , "r" , stdin);
    freopen("A-large.out" , "w" , stdout);
    scanf("%d",&t);
    while(t--)
    {
        int n,x;
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        memset(flag,0,sizeof(flag));
        sort(a,a+n);
        int ans=0;
        for(int i=0,j=n-1;i<=j;)
        {
            if(a[i]+a[j]<=x)
            {
                i++,j--;
            }
            else
            {
                j--;
            }
            ans++;
        }
        printf("Case #%d: ",++cnt);
        printf("%d\n",ans);
    }
    return 0;
}

