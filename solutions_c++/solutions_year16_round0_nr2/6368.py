#include<bits/stdc++.h>
using namespace std;

#define Plus    1
#define Minus   0

int main() {
    //freopen("B_in.txt", "r", stdin);
    freopen("B_output(large).out", "w", stdout);
    int T, n, m, p, ans, state[105];
    vector<int> A;
    char str[105];
    scanf("%d", &T);
    for(int cs = 1; cs <= T; cs ++) {
        scanf("%s", str);
        n = strlen(str), A.clear(), memset(state, 0, sizeof(state));
        for(int i = 0; i < strlen(str); i ++) {
            state[i] = (int)(str[i] == '+');
        }
        for(int i = 0; i < n; i ++) {
            if(A.empty()) {
                A.push_back(state[i]);
                continue;
            }
            if(state[i] == A.back()) continue;
            A.push_back(state[i]);
        }
        if(A.front() == Minus) {
            ans = A.size();
            if(ans % 2 == 0) ans --;
        } else {
            ans = A.size();
            if(ans % 2 == 1) ans --;
        }
        printf("Case #%d: %d\n", cs, ans);
    }
}
