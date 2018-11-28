#include <bits/stdc++.h>
using namespace std;

char s[20010];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%s", s);
        stack<char> st;
        int n = strlen(s), val = 0;
        for (int i = 0; i < n; i++) {
            if (st.empty() || st.top() != s[i]) {
                st.push(s[i]);
            } else {
                st.pop();
                val += 10;
            }
        }
        val += st.size() / 2 * 5;
        printf("Case #%d: %d\n", cas, val);
        fprintf(stderr, "Case #%d: %d\n", cas, val);
    }
    return 0;
}