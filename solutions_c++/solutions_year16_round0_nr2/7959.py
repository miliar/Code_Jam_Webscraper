#include <bits/stdc++.h>

using namespace std;

int f(const string &str) {
    size_t size = str.size();
    vector<int> minus(size + 1, 1e9), plus(size + 1, 1e9);
    minus[0] = plus[0] = 0;
    for (int i = 1; i <= size; ++i) {
        if (str[i - 1] == '-') {
            minus[i] = minus[i - 1];
            for (int j = i - 1; j >= 0 && str[j] == '-'; --j) {
                plus[i] = min(plus[i], minus[j] + 1);
            }
        } else {
            plus[i] = plus[i - 1];
            for (int j = i - 1; j >= 0 && str[j] == '+'; --j) {
                minus[i] = min(minus[i], plus[j] + 1);
            }
        }
    }
    return plus[size];
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    string str;
    for (int i = 0; i < n; ++i) {
        cin >> str;
        cout <<"Case #" << i + 1 << ": " << f(str) << endl;
    }
    return 0;
}
