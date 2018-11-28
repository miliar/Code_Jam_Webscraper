#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
int main() {
    int T;
    scanf("%d", &T);
    for ( int t = 1; t <= T; t++ ) {
        int N;
        scanf("%d", &N);
        vector<int> d(10, 0);
        int ans = -1;
        for ( int i = 1; i <= 200; i++ ) {
            int num = N * i;
            while (num) {
                if ( d[num % 10] == 0 ) d[num % 10] = 1;
                num /= 10;
            }
            int k = 0;
            for ( ; k < 10; k++ ) {
                if ( !d[k] ) break;
            }
            if ( k == 10 ) {
                ans = i * N;
                break;
            }
        }
        if ( ans == -1 ) printf("Case #%d: INSOMNIA\n", t);
        else printf("Case #%d: %d\n", t, ans);
    }
}
