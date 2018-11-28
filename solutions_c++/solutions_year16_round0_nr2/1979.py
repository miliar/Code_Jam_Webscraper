#include <bits/stdc++.h>
#define debug(args...) //fprintf(stderr, args)
using namespace std;

string s;

void go() {
    cin >> s;
    int n = s.size();
    for(int i = 0; ; i++) {
        string sn = s;
        int cnt = i;
        for(int j = 0; j < n; j++) {
            if(sn[j] == '+') {
                if(cnt % 2) cnt--;
            } else {
                if(!(cnt % 2)) cnt--;
            }
            debug("%c / %d\n", sn[j], cnt);
        }
        if(cnt >= 0) {
            printf("%d\n", i);
            break;
        }
    }
}
int main() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        debug("Entering Test %d\n", i);
        printf("Case #%d: ", i);
        go();
    }
    return 0;
}
