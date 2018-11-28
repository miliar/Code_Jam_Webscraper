#include <cstdio>
#include <cstring>
#define MAXN 1005
using namespace std;

int sol;
int nrt, n, k;
char s[MAXN];

int main() {
    scanf("%d\n", &nrt);
    for(int t = 1; t <= nrt; ++t) {
        scanf("%s %d\n", s, &k);
        n = strlen(s);

        sol = 0;
        for(int i = 0; i < n; ++i) {
            if(s[i] == '-') {
                ++sol;
                if(i + k - 1 >= n) {
                    sol = -1;
                    break;
                }

                for(int j = i; j < i + k; ++j)
                    s[j] = ((s[j] == '+') ? '-' : '+');
            }
        }

        printf("Case #%d: ", t);
        if(sol == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", sol);
    }

    return 0;
}