#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("anslarge.out", "w", stdout);

    int t, n, counter = 0;
    string in;

    scanf("%d", &t);
    while (t--) {
        counter++;
        scanf("%d", &n);
        cin >> in;
        int m = in[0] - '0';
        int ans = 0;

        for (int i = 1;i <= n;i++) {
            int temp = in[i] - '0';
            if (m >= i) {
                m = m + temp;
            } else {
                ans = ans + (i - m);
                m = m + (i - m) + temp;
            }
        }
        printf("Case #%d: %d\n",counter, ans);
    }

    return 0;
}
