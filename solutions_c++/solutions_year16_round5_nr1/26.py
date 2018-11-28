#include <cstdio>
#include <algorithm>
#include <numeric>
#include <cstring>
#include <vector>
#include <stack>
using namespace std;

char s[20001];

int solve() {
    int n = strlen(s);
    vector<char> st;
    int ans = 0;
    for(int i = 0; i < n; i++) {
        if(st.empty() || st.back() != s[i])
            st.push_back(s[i]);
        else
            st.pop_back(), ans += 10;
    }
    ans += st.size() / 2 * 5;
    return ans;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++) {
        scanf("%s", s);
        printf("Case #%d: %d\n", tt, solve());
    }
}

