#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int a[1001];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int ct = 0; ct < t; ct++){
        int n;
        cin >> n;
        int ans = 0;
        for (int i = 0; i < n; i++){
            cin >> a[i];
            ans += a[i] - 1;
        }
        ans++;
        for (int i = 2; i <= 1000; i++){
            int ans1 = 0;
            for (int j = 0; j < n; j++){
                ans1 += (a[j] - 1) / i;
            }
            ans1 += i;
            if (ans1 < ans) ans = ans1;
        }
        cout << "Case #" << ct + 1 << ": " << ans << endl;
    }
    return 0;
}
