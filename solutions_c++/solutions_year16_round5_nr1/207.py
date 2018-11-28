#include <bits/stdc++.h>
using namespace std;
int TC, N;
char s[20500];
int main () {
    scanf("%d", &TC);
    for (int T = 1; T <= TC; ++T) {
        scanf("%s", s);
        N = strlen(s);
        stack<char> st;
        long long ans = 0;
        for (int i = 0; i < N; ++i) {
            if (st.empty()) {
                st.push(s[i]);
                continue;
            }
            if (st.top() == s[i]) {
                ans += 10;
                st.pop();
            }
            else st.push(s[i]);
        }
        printf("Case #%d: %lld\n", T, ans + st.size()/2 * 5);
    }
    
}