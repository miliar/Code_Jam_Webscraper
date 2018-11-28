#include <iostream>
#include <fstream>
#define Nmax 1001

using namespace std;

int T, s[Nmax];

int main() {

    freopen("fis.in", "r", stdin);
    freopen("fis.out", "w", stdout);

    scanf("%d", &T);

    for(int t = 1; t <= T; ++t) {
        int N;
        scanf("%d ", &N);

        int total = 0;
        int needed = 0;
        for(int i = 0; i <= N; ++i) {
            char c;
            scanf("%c", &c);

            s[i] = c - '0';

            if(i > 0 && i > total) {
                int dif = i - total;
                needed += dif;
                total += dif;
            }

            total += s[i];
        }

        printf("Case #%d: %d\n", t, needed);

    }

    return 0;
}
