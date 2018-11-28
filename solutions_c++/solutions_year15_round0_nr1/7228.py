#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x)
#define fr first
#define sc second
#define pb push_back
#define mp make_pair

using namespace std;

string ss;

int main()
{
    lli tcase, si, i, j, k, cur, ans, tt;

    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    s(tcase);
    tt = 1;

    while (tt <= tcase) {
        printf("Case #%lld: ", tt);
        ++tt;
        ss.clear();

        ans = 0;
        cur = 0;

        s(si);
        cin >> ss;

        k = ss.length();

        for (i = 0; i < k; ++i) {
            if (cur >= i) {
                cur = cur + (ss[i]-'0');
            } else {
                if (ss[i] > '0') {
                    ans = ans + (i-cur);
                    cur = cur + (i-cur);
                    cur = cur + (ss[i]-'0');
                }
            }
        }

        printf("%lld\n", ans);
    }

    return 0;
}
