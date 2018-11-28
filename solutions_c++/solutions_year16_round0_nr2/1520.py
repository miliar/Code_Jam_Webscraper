#include <bits/stdc++.h>

using namespace std;
// const int MaxN = ;
// const int MOD = ;

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
    int t;
    scanf("%d", &t);
    for (int cs = 0; cs < t; ++cs) {
        printf("Case #%d: ", cs + 1);
        string s;
        cin >> s;
        int result = 0, i = 0;
        for (; i < (int) s.size(); ++i)
            if (s[i] == '+')
                break;
        if (i > 0)
            ++result;
        int sign = false;
        for (; i < (int) s.size(); ++i) {
            if (s[i] == '-' && !sign) {
                sign = true;
            } if (s[i] == '+' && sign) {
                sign = false;
                result += 2;
            }
        }
        if (sign) {
            result += 2;
        }
        cout << result << endl;
    }
    return 0;
}
