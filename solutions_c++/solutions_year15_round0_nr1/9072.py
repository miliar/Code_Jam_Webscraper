#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,k,i,s,curr,ans;
    string st;
    scanf("%d", &t);

    for (k = 1; k <= t; k++) {
        scanf("%d", &s);
        cin >> st;
        curr = 0;
        ans = 0;
        for (i = 0; i <=s; i++) {
            if (curr < i) {
                ans += (i - curr);
                curr = i;
            }
            curr += (st[i] - 48);
        }
        printf("Case #%d: %d\n", k,ans);
    }
    return 0;
}
