#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
#include<cstdlib>
#include<queue>
#pragma comment(linker,"/STACK:1024000000,1024000000")
using namespace std;

#define N 1000005
#define L(x) x<<1
#define R(x) x<<1|1
#define M(x,y) (x + y)>>1
#define MOD 1000000007
#define MODD 1000000006
#define inf 0x7fffffff
#define llinf 0x7fffffffffffffff
#define LL long long
#define eps 1e-8

double a[1005],b[1005];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int i,j,k,l;
    int r,c;
    int t,test = 1,n,m;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i = 1;i <= n;i++)
            scanf("%lf",&a[i]);
        for(i = 1;i <= n;i++)
            scanf("%lf",&b[i]);
        sort(a + 1,a + 1 + n);
        sort(b + 1,b + 1 + n);
        int x = 0,y = 0;
        for(i = j = n;i >= 1;i--)
        {
            while(a[i] < b[j] && j != 0)
                j--;
            if(j != 0)
            {
                 x++;
                 j--;
            }
        }
        for(i = j = n;i >= 1;i--)
        {
            while(b[i] < a[j] && j != 0)
                j--;
            if(j != 0)
            {
                 y++;
                 j--;
            }
        }
        printf("Case #%d: %d %d\n",test++,x,n - y);
    }
    return 0;
}
