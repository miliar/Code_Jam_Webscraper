#include<bits/stdc++.h>
#define sf scanf
#define pf printf

using namespace std;

int main()
{
    freopen("output.in" , "w" , stdout);
    freopen("input.txt" , "r" , stdin);
    int t , ar[20] , temp , cc = 0;
    long long num , ans , one , cnt ;
    sf("%d" , &t);
    while(t--)
    {
        sf("%lld" , &num);
        if(num == 0)
        {
            pf("Case #%d: INSOMNIA\n" , ++cc);
            continue ;
        }
        cnt = 0;
        memset(ar , 0 , sizeof(ar));
        while(true)
        {
            temp = 0;
            for(int i = 0 ; i < 10 ; ++i) temp = temp + ar[i];
            if(temp >= 10)
            {
                ans = (num * cnt);
                break ;
            }
            ++cnt;
            one = (num * cnt);
            while(one)
            {
                temp = one % 10;
                ar[temp] = 1;
                one = one / 10;
            }
        }
        pf("Case #%d: %lld\n" , ++cc , ans);
    }
    return 0;
}
