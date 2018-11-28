#include <bits/stdc++.h>
#include <iostream>
#define FI(i, a, b) for (int i = (a); i <= (b); i++)
#define FD(i, a, b) for (int i = (a); i >= (b); i--)
using namespace std;

void work(int testCase) {
    char s[1005];
    int k;
    scanf("%s %d", s + 1, &k);
    int n = strlen(s + 1);
    queue<int> qu;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        while (!qu.empty() && qu.front() + k - 1 < i)
            qu.pop();
        if ((s[i] == '-' && qu.size() % 2 == 0) ||
            (s[i] == '+' && qu.size() % 2)) {
            if (i + k - 1 > n) {
                printf("Case #%d: IMPOSSIBLE\n", testCase);
                return;
            }
            qu.push(i);
            ans++;
        } else
            continue;
    }
    printf("Case #%d: %d\n", testCase, ans);
}
int main() {
    int T;
    scanf("%d", &T);
    FI(i, 1, T)
    work(i);
}