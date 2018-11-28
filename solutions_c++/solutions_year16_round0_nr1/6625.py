#include <bits/stdc++.h>
using namespace std;
long long int a[10];
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("o.txt","w",stdout);
    long long int t, i, n, m, check, c, j, k;
    scanf("%lld", &t);
    for(i=1; i<=t; i++)
    {
        for(k=0; k<10; k++)
            a[k]=0;
        scanf("%lld", &n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n", i);
            continue;
        }
        for(k=1; ; k++)
        {
            check=1;
            m=k*n;
            c=m;
            while(m)
            {
                a[m%10]=a[m%10]+1;
                m=m/10;
            }
            for(j=0; j<=9; j++)
            {
                if(a[j]==0)
                    check=0;
            }
            if(check==1)
                break;
        }
        printf("Case #%lld: %lld\n", i, c);
    }
    return 0;
}
