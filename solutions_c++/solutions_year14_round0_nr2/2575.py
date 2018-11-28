/// 优先队列 priority_queue
/// 全排列 next_permutation
#include<cstdio>
#include<cmath>
#include<queue>
#include<stack>
#include<string>
#include<cstring>
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<set>
#include<ctime>
#include<cmath>
#define mmax  100010
#define eps 1e-8
#define ll __int64
#define ex 2.7182818284590452354
#define pi 3.141592653589793239
#define inf 0x7fffffff
#define DC(n) printf("Case #%d: ",++n)
#define SD(n) scanf("%d",&n)
#define SS(str) scanf("%s",str)
#define SDB(n) scanf("%lf",&n)
#define mm 1000000007
///#define debug
using namespace std;
int main()
{
    int t,ca=0;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    SD(t);
    double c,f,x;
    while(t--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        double ans=x/2;
        double sp=2.0;
        while(1)
        {
            double tmp=(c-x)/sp+x/(sp+f);
            if(tmp>=0.0)
                break;
            sp+=f;
            ans+=tmp;
        }
        DC(ca);
        printf("%.6lf\n",ans);
    }
}
