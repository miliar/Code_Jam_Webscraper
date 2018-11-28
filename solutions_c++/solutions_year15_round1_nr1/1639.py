#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
int ar[MAXN];
int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    int N;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int i = 1; i <= N; ++i) {
            cin >> ar[i];
        }
        int ans1 = 0, ans2 = 0;
        int amt = 0;
        for (int i = 2; i <= N; ++i) {
            if (ar[i] < ar[i-1]) {
                ans1 += ar[i-1]-ar[i];
                amt = max(amt, ar[i-1]-ar[i]);
            }
        }
        for (int i = 1; i < N; ++i) {
            ans2 += min(amt, ar[i]);
        }
        printf("Case #%d: %d %d\n", t, ans1, ans2);
    }
    return 0;
}
