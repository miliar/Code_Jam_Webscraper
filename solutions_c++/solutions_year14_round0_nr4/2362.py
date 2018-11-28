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
double a[1010];
double b[1010];
int main()
{
    int t,ca=0,i;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    SD(t);
    int n;
    while(t--)
    {
        DC(ca);
        SD(n);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int cnt1=0;
        int tmp=0;
        for(int i=0;i<n;i++)
        {
            if(b[i]>a[tmp])
            {
                cnt1++;
                tmp++;
            }
        }
        cnt1=n-cnt1;
        int cnt2=0;
        tmp=0;
        for(int i=0;i<n;i++)
        {
            if(a[i]>b[tmp])
            {
                cnt2++;
                tmp++;
            }
        }
        cout<<cnt2<<" "<<cnt1<<endl;
    }
}
