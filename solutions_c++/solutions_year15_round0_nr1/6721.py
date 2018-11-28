#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

int main () {
    int T;
    int S_max;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &S_max);
        int res = 0, sum = 0;
        for (int i = 0; i <= S_max; i++) {
            char c = ' ';
            while (isspace(c))
                scanf("%c", &c);
            if (sum < i) {
                res += i-sum;
                sum += i-sum;

            }
            sum += c-'0';
        }

        printf("Case #%d: %d\n", t, res);
    }

    return 0;
}
