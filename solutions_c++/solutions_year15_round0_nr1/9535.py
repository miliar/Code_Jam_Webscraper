#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, q;
    cin >> T;
    for(int q = 0; q < T; q++) {
        string s;
        int n;
        cin >> n >> s;

        int sum = 0, res = 0;
        for(int i = 0; i <= n; i++) {
            if (sum < i && s[i] != '0') {
                res += i - sum;
                sum = i;
            }
            sum += (s[i] - '0');
        }

        /*int sum = 0, res, pos = 0;
        for(int i = 0; i < (int)s.size(); i++) {
            sum += (s[i] - '0');
            if (s[i] != '0') {
                pos = i;
            }
        }
        sum -= (s[pos] - '0');
        res = max(0, pos - sum);*/
        cout << "Case #" << (q + 1) << ": " << res << endl;
    }
    return 0;
}
