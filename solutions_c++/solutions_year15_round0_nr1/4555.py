#include <bits/stdc++.h>
using namespace std;

#define maxN 1005

int TC;
int smax;
string s;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> TC;
    for (int cs = 0; cs < TC; cs++) {
        cin >> smax >> s;

        int su = s[0] - '0';
        int add = 0;
        for (int i = 1; i < s.size(); i++) {
            int cur = s[i] - '0';
            if (su < i && cur) {
                add += i - su;
                su += i - su;
                //cout << i << " -> " << su << "," << add << endl;
            }
            su += cur;
        }
        cout << "Case #" << cs + 1 << ": " << add << endl;
    }

    return 0;
}
