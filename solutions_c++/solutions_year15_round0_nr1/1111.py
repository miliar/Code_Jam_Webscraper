#include <iostream>
#include <algorithm>
#include <string>


using namespace std;



int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T, acc, i, total, Case, S, n, r;
    char str[1010];
    
    scanf("%d", &T);
    
    for (Case = 1; Case <= T; Case++) {
        printf("Case #%d: ", Case);
        scanf("%d %s", &S, str);
        total = 0, acc = str[0] - '0';
        for (i = 1; i <= S; i++) {
            n = str[i] - '0';
            if (!n) continue;
            r = i - acc;
            acc += n;
            if (r > 0) {
                total += r;
                acc += r;
            }
        }
        printf("%d\n", total);
    }
    return 0;
}
