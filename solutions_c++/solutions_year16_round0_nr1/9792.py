#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.o", "w", stdout);
    long long n,m,s,mo,d;
    int t;

    scanf("%d",&t);

    for(int cs=1; cs<=t; cs++)
    {
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",cs);
            continue;
        }
        map<long long,int>mm;
        int cnt=0;
        for(m=1;; m++)
        {
            s = m * n;
            d=s;
            while(d!=0)
            {
                mo = d%10;
                if(mm.count(mo)==0)
                {
                    mm[mo]=1;
                    cnt++;
                }
                d = d/10;
            }
            if(cnt==10)
            {
                printf("Case #%d: %lld\n",cs,s);
                break;
            }
        }
    }

    return 0;
}
