#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    freopen("A-small-attempt5.in", "r", stdin);
    freopen( "output.txt", "w",stdout);
    int n;
    scanf("%d", &n);
    for (int k = 0; k < n; k ++)
    {
        int Smax, sum = 0, ans = 0;
        scanf("%d", &Smax);
        string s;
        cin >> s;
        for (int i = 0; i <= Smax; i ++)
            {
                if (i > sum && (s[i] - '0') > 0) ans += i - sum, sum+=ans;// cout << i << " " << sum << " " << ans << endl;
                 sum +=  (s[i]- '0');
            }

        printf("Case #%d: %d\n", k+1, ans);
    }
    return 0;
}
