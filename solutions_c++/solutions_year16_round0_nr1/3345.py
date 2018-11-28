#include<bits/stdc++.h>
#define mod 1000000007
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    long long int t,k=1,count,in,i,n,m,check,nf;
    scanf("%lld",&t);
    while(k<=t)
    {
        long long int num[10]={0};count=0;check=0,i=1;
        scanf("%lld",&nf);
        n=nf;
        if(n)
        {
            while(1)
            {
                //printf("n=%lld\n",n);
                i++;
                m=n;
                while(m)
                {
                    in=m%10;
                    if(num[in]==0)
                    {
                        num[in]++;
                        count++;
                        if(count==10)
                        {
                            printf("Case #%lld: %lld\n",k,n);
                            check=1;
                            break;
                        }
                    }
                    m=m/10;
                }
                n=nf*i;
                if(check)
                    break;
            }
            
        }
        else
        {
            printf("Case #%lld: INSOMNIA\n",k);
        }
        k++;
    }
    return 0;
}
