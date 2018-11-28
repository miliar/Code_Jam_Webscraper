#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define what_is(x) cerr << #x << ": " << x << endl;

using namespace std;

int T, s_max;
int cnt[1001];

int main() {
    #ifdef LOCAL
        freopen("input", "r", stdin);
        freopen("output", "w", stdout);
    #endif

    scanf("%d\n", &T);
    forn(t, T) {
        scanf("%d ", &s_max);

        int cur_cnt = 0;
        int ans = 0;
        forn(i, s_max + 1) {
            char ch;
            scanf("%c", &ch);
            cnt[i] = ch - '0';
            what_is(ch);
            what_is(cnt[i])

            if (cur_cnt >= i) {
                cur_cnt += cnt[i];
            } else {
                ans += i - cur_cnt;
                cur_cnt = i + cnt[i];
            }
        }
        scanf("\n");

        printf("Case #%d: %d\n", t + 1, ans);
    }

}
