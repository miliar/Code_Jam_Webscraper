#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        string str;
        int n;
        cin >> n >> str;
        int sum = 0;
        int ans = 0;
        for (int j = 0; j <= n; ++j) {
            if (sum < j) {
                ans += j-sum;
                sum = j;
            }
            int dig = str[j]-'0';
            sum += dig;
        }
        printf("Case #%d: %d\n", i, ans);
    }
}
