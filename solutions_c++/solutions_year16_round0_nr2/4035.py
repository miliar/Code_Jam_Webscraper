#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long int
#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define sd(x) scanf("%lf", &x)
#define mod 1000000007
#define get getchar_unlocked

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("CJO2.txt", "w", stdout);
    int t, u = 0, cnt, i;
    string s, m, n;
    bool found;
    cin >> t;
    while (t--) {
        cin >> s;
        printf("Case #%d: ", ++u);
        cnt = 0;
        while (true) {
            found = false;
            for (i = 0; i < s.size(); ++i) {
                if (s[i] == '-') {
                    found = true;
                    break;
                }
            }
            if (!found)
                break;
            ++cnt;
            if (s[0] == '+') {
                for (i = 0; s[i] == '+'; ++i)
                    s[i] = '-';
                continue;
            }
            i = s.size()-1;
            m.clear();
            n.clear();
            while (s[i] == '+') {
                n.pb(s[i]);
                --i;
            }
            reverse(n.begin(), n.end());
            while (i >= 0) {
                m.pb(s[i] == '+' ? '-' : '+');
                --i;
            }
            s = m+n;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
