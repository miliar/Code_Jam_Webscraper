#include<cstdio>
typedef long long ll;

int main()
{
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        ll n;
        scanf("%lld",&n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", tt);
            continue;
        }
        bool chk[10] = {false};
        int sum = 0;
        ll i;
        for(i=1;;i++)
        {
            ll tmp = i*n;
            while(tmp>0)
            {
                if(!chk[tmp%10])
                {
                    chk[tmp%10] = true;
                    sum++;
                }
                tmp/=10;
            }   
            if(sum == 10) break;
//            if(i>1e7) printf("BUG");
        }
        printf("Case #%d: %lld\n", tt, i*n);
    }
    return 0;
}
