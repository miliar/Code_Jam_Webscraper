#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    long long int t;
    scanf("%lld", &t);

    for(long long int tc = 1; tc <= t; tc++)
    {
        long long int maxx,needed=0;
        char s[1005];
        scanf("%lld %s", &maxx, s);

        long long int daraye_jabe[1001];
        for(long long int i = 0; i <= maxx; i++)
        {
            if(i == 0)
            {
                daraye_jabe[i] = s[i] - 48;
                continue;
            }

            if(daraye_jabe[i-1] >= i)
            {
                daraye_jabe[i] = (s[i]-48) + daraye_jabe[i-1];
            }
            else if(i > daraye_jabe[i-1] && s[i] > 48)
            {
                long long int lagbe = i-daraye_jabe[i-1];
                for(long long int j = i-1; j >= 0; j--)
                {
                    if(s[j] == 9+48)
                    {
                        continue;
                    }
                    while(s[j] < 9+48 && lagbe != 0)
                    {
                        s[j]++;
                        lagbe--;
                        needed++;
                        daraye_jabe[j]++;
                    }
                    if(lagbe == 0)
                    {
                        daraye_jabe[i] = s[i]-48 + daraye_jabe[i-1];
                        break;
                    }
                    else continue;
                }
            }
            else{
                daraye_jabe[i] = daraye_jabe[i-1];
            }
        }
        printf("Case #%lld: %lld\n", tc, needed);
    }
}
