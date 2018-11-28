#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t=0,k=1;
    scanf("%d",&t);
    while(t--)
    {
        int n=0,f=1,i=1,j=0;
        long long res = 0, n1 = 0;
        scanf("%d",&n);
        int a[10]={0};
        if(n == 0)printf("Case #%d: INSOMNIA\n",k++);
        else
        {
            while(f)
            {
                long long ans = 0;
                n1 = n;
                res = n1 = (long long)i * n;
                while(n1)
                {
                     a[n1%10]=1;
                     n1/=10;
                }

                for(j=0;j<10;j++)
                    ans+=a[j];

                if(ans == 10)
                    f=0;

                i++;
            }
            printf("Case #%d: %lld\n",k++,res);
        }
    }
}
