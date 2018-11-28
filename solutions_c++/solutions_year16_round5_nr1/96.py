#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt, n;
char s[20005];
vector<char> st;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%s", s);
        n = strlen(s);
        int rem = n / 2;
        int ans = 0;
        REP(i, n) if (st.empty() || (st.back() != s[i] && rem > 0)) {
            --rem;
            st.pb(s[i]);
        } else {
            if (st.back() == s[i]) ans += 10;
            else ans += 5;
            st.pop_back();
        }
        printf("%d\n", ans);
        cerr << "done " << test << endl;
    }
    return 0;
}
