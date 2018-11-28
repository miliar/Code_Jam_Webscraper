//Done by: K Ashwin

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TR(c, it) \
for (auto it = (c).begin(); it != (c).end(); it++)

#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define set0(a) memset(a, 0, sizeof(a))
#define setdp(a) memset(a, -1, sizeof(a))
#define INF 2000000000
#define MOD 1000000007

int main()
{
    int t, ans, flag, idx, mp;
    string s, tmp;

    freopen("inp.txt", "r", stdin);
    freopen("op.txt", "w", stdout);

    s(t);

    int tt = 0;
    while (t--) {
        ++tt;

        cin >> s;
        /*s = "";
        REP (i, 1, tt) {
            if (i % 2)
                s.pb('+');

            else
                s.pb('-');
        }*/

        ans = 0;
        while (1) {
            //cout << s << endl;
            flag = 1;
            idx = -1;
            mp = -1;
            REP (i, 0, s.size() - 1) {
                if (flag && s[i] == '+')
                    idx = i;

                else
                    flag = 0;

                if (s[i] == '-')
                    mp = i;
            }

            if (flag && idx == s.size() - 1)
                break ;

            if (!flag && idx != -1) {
                ++ans;
                REP (i, 0, idx)
                    s[i] = '-';
            }

            ++ans;
            //cout << idx << " " << mp << " " << tmp << endl;
            tmp = s.substr(0, mp + 1);
            reverse(tmp.begin(), tmp.end());

            REP (i, 0, tmp.size() - 1) {
                if (tmp[i] == '+')
                    s[i] = '-';

                else
                    s[i] = '+';
            }
        }

        printf("Case #%d: %d\n", tt, ans);
    }

    return 0;
}
