#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 20*1000+5;

void clear() {
}

char s[maxn];
int n;

int main() {
    int testcases; scanf("%d", &testcases);
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d: ", testnum);
        scanf(" %s", s);
        n = strlen(s);
        int ans = 0;
        std::stack<char> t;
        for (int i = 0; i < n; i++) {
            if (!t.empty() && t.top() == s[i]) {
                t.pop();
                ans += 10;
            } else  t.push(s[i]);
        }
        ans += sz(t) / 2 * 5;
        printf("%d\n", ans);
        clear();
    }
}

