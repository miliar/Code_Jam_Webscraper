#include <iostream>
#include <cstdio>
#include <string>

using namespace std;


bool r(char a, char b, char c, char d, char e) {
    return ((a == b) && (b == c) && (c == d) && (d == e));
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    int a;
    string s;
    int ans;
    int sum = 0;
    for (int i = 0; i < t; ++i) {
        ans = 0;
        sum = 0;
        cin >> a;
        cin >> s;
        for (int i = 0; i < a + 1; ++i) {
            ans = max(ans, i - sum);
            sum += s[i] - '0';
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
