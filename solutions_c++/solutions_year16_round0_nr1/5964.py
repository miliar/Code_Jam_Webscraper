#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);
        if(N == 0) {
            printf("Case #%d: INSOMNIA\n");
            continue;
        }
        vector<bool> digs(10);
        int used = 0;
        int cur = 0;
        while(used != 10) {
            cur += N;
            string s = to_string(cur);
            for(int i = 0; i < s.size(); i++) {
                if(!digs[s[i] - '0']) {
                    digs[s[i] - '0'] = true;
                    used++;
                }
            }
        }
        printf("Case #%d: %d\n", t + 1, cur);
    }
    return 0;
}
