#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("inputxyzl.in","r",stdin);
    freopen("outputxyz.txt","w",stdout);

    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        set<int> s;
        long long int fix=1;
        printf("Case #%d: ",cases);
        long long int n;
        int res;
        scanf("%lld",&n);
        int flag=0;
        if(n==0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            for(long long int x=n;;)
            {
                while(x)
                {
                    int digit=x%10;
                    s.insert(digit);
                    if(s.size()==10)
                    {
                        res=fix;
                        flag=1;
                        break;
                    }
                    x/=10;
                }
                if(flag==1)
                {
                    break;
                }
                fix++;
                x=fix*n;
            }
            if(flag==1)
            {
                printf("%lld\n",fix*n);
            }
        }
    }
    return 0;
}
