#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
int main(int argc, char **argv)
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    ULL T;
    cin >> T;
    for (ULL t = 1; t <= T; ++t) {
        string S;
        cin >> S;
        ULL ans = 0;
        char ch = '-';
        LL i = S.size();
        i = S.rfind(ch, i);
        while (i != string::npos) {
            ++ans;
            ch = (ch == '-') ? '+' : '-';
            i = S.rfind(ch, i);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
