#include <bits/stdc++.h>

using namespace std;
int a[1004],n;
char c;
int check(int curmax)
{
    int cnt = 0;
    for (int i = 1; i <= n; ++i){
       cnt += (a[i] / curmax + (a[i] % curmax != 0) - 1);
    }
    return cnt;
}
int main()
{
  //  freopen("B-large.in","r",stdin);
  //  freopen("output.out","w",stdout);
    int tests;
    cin >> tests;
    for (int j = 1; j <= tests; ++j){
        cin >> n;
        for (int i = 0; i <= 1000; ++i) a[i] = 0;
        for (int i = 1; i <= n; ++i){
            int k;
            cin >> a[i];

        }
        int ans = 100000000;
        for (int i = 1; i <= 1000; ++i){
            ans = min(ans,i + check(i));
        }
        cout << "Case #" << j << ": " << ans << endl;
    }

    return 0;
}
