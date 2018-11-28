#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
int data[MAXN];
int D;

int solve(int last)
{
    int ret = last;
    for (int i = 0; i < D; ++i) {
        int t = data[i];
        while (t > last) {
            ++ret;
            t -= last;
        }
    }
    return ret;
}

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> D;
        int ma = 0;
        for (int i = 0; i < D; ++i) {
            cin >> data[i];
            ma = max(ma, data[i]);
        }
        int ans = 1024;
        for (int i = ma; i > 0; --i) {
            ans = min(ans, solve(i));
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
