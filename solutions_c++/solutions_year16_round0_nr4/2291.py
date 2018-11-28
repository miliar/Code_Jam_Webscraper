#include <cstdio>
#include <cmath>
using namespace std;
long long int t,k,c,s;
int main()
{
    scanf("%lld",&t);
    for(int j=1;j<=t;j++)
    {
       scanf("%lld%lld%lld",&k,&c,&s);
       printf("Case #%d: ",j);
       for(int i=0;i<k;i++)
       printf("%d ",i+1);
       printf("\n");
    }
    return 0;
}
