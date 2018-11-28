#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <math.h>
#include <map>
#include <stdlib.h>
#include <algorithm>

#define eps 1e-5
#define inf 0x3f3f3f3f
#define Linf 0x3f3f3f3f3f3f3f3f
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b)  ((a)<(b)?(a):(b))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1 | 1
#define lc rt<<1
#define rc rt<<1 | 1
#define getx2(a)  ((a)*(a))
#define Pi acos(-1.0)

typedef long long LL;
using namespace std;
#define MM 76543
int a[2020];

int main()
{
    int t;
    int cnt=0,n;
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        printf("Case #%d: ",++cnt);
        if(!n)
            printf("INSOMNIA\n");
        else
        {
            map<int,int>M;
            int cn=10;
            LL m;
            LL ans=0;
            for(LL i=1;;i++)
            {
                m=LL(n)*i;
                ans=m;
                while(m)
                {
                    int d=m%10;
                    if(!M[d])
                    {
                        cn--;
                        M[d]=1;
                    }
                    m/=10;
                }
                if(!cn)
                {
                    break;
                }
            }
            printf("%I64d\n",ans);
        }
    }
    return 0;
}
