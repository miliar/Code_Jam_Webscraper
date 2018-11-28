#include <bits/stdc++.h>

/**

"Is money a good enough indicator for a job satisfaction?"

**/

using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int T, M;
    cin >> T;
    for(int test = 1; test <= T; test++){
        string S;
        cin >> M >> S;
        long left = 0, ans = 0;
        left += (S[0] - '0');
        for(int i = 1; i <= M; i++) {
            if(left < i && S[i] != '0'){
                long tmp = i - left;
                ans += tmp, left += tmp;
            }
            if(S[i] != '0') left += (S[i] - '0');
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
