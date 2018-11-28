#include <bits/stdc++.h>
using namespace std;
int main()
{
    #ifdef CodeJam
        freopen("A-large.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
    #endif ///CodeJam

    long long int n, N, i = 0, ans, t, c;
    unordered_map <long long int, long long int> mp;

    scanf("%lld", &t);

    while(t-- and scanf("%lld", &n) == 1)
    {
        mp.clear();
        N = n;
        c = 2;
        if(!n) printf("Case #%lld: INSOMNIA\n", ++i);
        else
        {
            while(mp.size() != 10)
            {
                ans = n;
                while(n)
                {
                    mp[n % 10] = 1;
                    n /= 10;
                }
                n = N * c++;
            }
            printf("Case #%lld: %lld\n", ++i, ans);
        }
    }


    return 0;
}
