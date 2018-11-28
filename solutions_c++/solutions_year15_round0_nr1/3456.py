#include <bits/stdc++.h>

using namespace std;
int a[1004];
char c;
int main()
{
   // freopen("A-large.in","r",stdin);
   // freopen("output.out","w",stdout);
    int tests;
    cin >> tests;
    for (int j = 1; j <= tests; ++j){
        int n;
        cin >> n;
        int cnt = 0;
        int ans = 0;
        for (int i = 0; i <= n; ++i){
            cin >> c;
            a[i] = c - 48;
            if (cnt < i){
                ans += (i - cnt);
                cnt += (i - cnt);
            }
            cnt += a[i];
        }
      cout << "Case #" << j << ": " << ans << endl;
    }

    return 0;
}
