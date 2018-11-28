#include <stdio.h>
using namespace std;
#define li long long  int
int main() 
{
    li t,i;
    scanf("%lld",&t);
    for(i=0;i<t;i++)
    {
        li x;
        int digit,a[10]={0};
        scanf("%lld",&x);
        li dummy=x;
        li count=0;
        int m;
        if(x==0)printf("Case #%d: INSOMNIA\n",i+1);
        else
        {
            
            li k;
            for( k=1;count!=10;k++)
            {
                dummy = k*x;
                
                while(dummy>0)
                {
                    digit=dummy%10;
                    if(a[digit]==0)
                    {
                        a[digit]=1;
                        count++;
                    }
                    dummy/=10;
                }
            }
           // printf("%lld\n",k);
            li ans=(k-1)*x;
            printf("Case #%lld: %lld\n",i+1,ans);
            
        }
    }
	return 0;
}

