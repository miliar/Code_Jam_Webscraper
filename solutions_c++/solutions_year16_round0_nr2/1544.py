#include <bits/stdc++.h>
using namespace std;

int n;
string s;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output1.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int Case = 1; Case <= nTests; ++Case) {
        cin >> s;
        n = (int)s.size();
        int res = 0;
        for(int i = n - 1; i >= 0; --i) {
            if (s[i] == '+') continue;
            if (s[0] == '-') {
                ++res;
                for(int j1 = 0, j2 = i; j1 <= j2; ++j1, --j2) {
                    char ch1 = (s[j1] == '+' ? '-' : '+');
                    char ch2 = (s[j2] == '+' ? '-' : '+');
                    s[j2] = ch1; s[j1] = ch2;
                }
            }
            else {
                int pos = 0;
                for(; s[pos] == '+'; ++pos);
                --pos;

                ++res;
                for(int j1 = 0, j2 = pos; j1 <= j2; ++j1, --j2) {
                    char ch1 = (s[j1] == '+' ? '-' : '+');
                    char ch2 = (s[j2] == '+' ? '-' : '+');
                    s[j2] = ch1; s[j1] = ch2;
                }

                ++res;
                for(int j1 = 0, j2 = i; j1 <= j2; ++j1, --j2) {
                    char ch1 = (s[j1] == '+' ? '-' : '+');
                    char ch2 = (s[j2] == '+' ? '-' : '+');
                    s[j2] = ch1; s[j1] = ch2;
                }
            }
        }

        printf("Case #%d: %d\n", Case, res);
    }

    return 0;
}

