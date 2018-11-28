#include <cstdio>

using namespace std;
long long int t,n,a[10],x,flag;
int main()
{
    scanf("%lld",&t);
    for(int j=0;j<t;j++)
    {
    for(int i=0;i<10;i++)
    a[i]=0;
    flag=0;

    scanf("%lld",&n);
    for(int i=0;flag==0 && i<1000000 && x<1000000000;i++)
    {x=(i+1)*n;
    while(x!=0)
    {
    a[x%10]=1;
    x/=10;
    }

    for(int i=0;i<10;i++)
    {
    if(a[i]!=0)flag=1;
    else
    {
    flag =0;
    break;
    }
    }
    if(flag==1)x=(i+1)*n;

    }
    if(x!=0)
    printf("Case #%d: %lld\n",j+1,x);
    else
    printf("Case #%d: INSOMNIA\n",j+1);


    }
    return 0;
}
