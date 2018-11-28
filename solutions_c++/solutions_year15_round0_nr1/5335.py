#include <bits/stdc++.h>
using namespace std;

const int MAX = 1005;

int nTests, test;
int n, a[MAX];
string s;

int main() {
    //freopen("A.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        cin >> n >> s;
        for (int i = 0; i <= n; ++i)
            a[i] = (s[i] - '0');

        int res = 0, sum = a[0];
        for (int i = 1; i <= n; ++i) {
            if (a[i] > 0 && sum < i) {
                int t = i - sum;
                res += t;
                sum += t + a[i];
            } else {
                sum += a[i];
            }
        }

        cout << "Case #" << test << ": " << res << endl;
    }
}
