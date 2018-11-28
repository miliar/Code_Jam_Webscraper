#include <iostream>
#include <cstdio>
#include <climits>
#include <vector>

using namespace std;

int main()
{
    long long int n,sum,temp;
    int t,i,k,count,a;
    scanf("%d",&t);
    for(k=1;k<=t;++k)
    {
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",k);
            continue;
        }
        sum=n;
        vector <int> d (11,0);
        count=0;
        while(count<10 && sum<LLONG_MAX && sum>0)
        {
            temp=sum;
            while(temp)
            {
                a=temp%10;
                if(d[a]==0)
                {
                    d[a]=1;
                    count++;
                }
                if(count==10)
                    break;
                temp/=10;
            }
            if(count==10)
                break;
            sum+=n;
        }
        if(sum>=LLONG_MAX || sum<0)
            printf("Case #%d: INSOMNIA\n",k);
        else
            printf("Case #%d: %lld\n",k,sum);
    }
}