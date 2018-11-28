#include <stdio.h>
#include <cmath>
using namespace std;
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
	freopen("sum.out","w",stdout);
    int t;
    long long r,b;
    scanf("%d",&t);
    int test=1;
    while(t--)
    {
        scanf("%lld%lld",&r,&b);
        long long sum=0;
        int num=0;
        while(1)
        {
            sum+=2*r+1;
            r+=2;
            if(sum>b) break;
            num++;
        }
        printf("Case #%d: %d\n",test++,num);
    }
    return 0;
}
