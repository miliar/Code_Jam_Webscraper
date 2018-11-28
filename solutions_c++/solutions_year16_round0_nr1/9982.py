#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,k;
    long long ans,d,i,j;
    int a[10];
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        if(n==0)
           printf("Case #%d: INSOMNIA\n",k);
        else
        {
            for(i=0;i<10;i++)
                a[i]=0;
            for(i=1;;i++)
            {
                d=i*n;
                while(d>0)
                {
                    a[d%10]=1;
                    d=d/10;
                }
                for(j=0;j<10;j++)
                {
                    if(a[j]>=1)
                        continue;
                    break;
                }
                if(j==10)
                    break;

            }
            printf("Case #%d: %lld\n",k,i*n);

        }

    }

}
