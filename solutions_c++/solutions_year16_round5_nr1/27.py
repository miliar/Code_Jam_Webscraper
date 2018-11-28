#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

char buf[40000];
int v[3] = {0, 0, 5};

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf(" %s", buf);
        int n = strlen(buf);
        stack<char> stk;
        int res = 0;
        FO(i,0,n) {
            if (!stk.empty() && stk.top() == buf[i]) {
                stk.pop();
                res += 10;
            } else {
                stk.push(buf[i]);
            }
        }
        res += 5 * (sz(stk) / 2);
        printf("Case #%d: %d\n", Z, res);
    }
}

