#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<map>

using namespace std;

long long aa[]={1,4,9,121,484,1002001,1234321};

int main()
{
    int i,t,co=1,cnt;
    long long a,b;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %lld",&a,&b);
        cnt=0;
        for(i=0;i<7;i++)
        {
            if(aa[i]>=a && aa[i]<=b)
                cnt++;
            if(aa[i]>b)
                break;
        }
        printf("Case #%d: %d\n",co++,cnt);
    }
    return 0;
}
