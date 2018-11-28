#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#define INF 100005

using namespace std;
long long F[100];
int NUM[20];
int Check(long long n)
{
    int i,cnt;
    for (cnt=0;n;n/=10,cnt++)
        NUM[cnt]=n%10;
    for (i=0;i<cnt/2;i++)
        if (NUM[i]!=NUM[cnt-i-1])
            return 0;
    return 1;
}
int Calc(long long now)
{
    int low=0,high=39,mid;
    while (low<high)
        if (mid=(low+high+1)/2,F[mid]<=now) low=mid;
        else high=mid-1;
    return low;
}
int main()
{
    int h,t,cnt=0;
    long long a,b;
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    for (a=1LL;a<=10000000;a++)
        if (b=a*a,Check(a) && Check(b))
            F[++cnt]=b;
    for (h=scanf("%d",&t);h<=t;h++)
    {
        scanf("%I64d%I64d",&a,&b);
        printf("Case #%d: %d\n",h,Calc(b)-Calc(a-1));
    }
    return 0;
}
