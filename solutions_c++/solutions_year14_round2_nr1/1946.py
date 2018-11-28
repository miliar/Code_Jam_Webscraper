#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char sa[128], sb[128];

int memo[128][128];
int len_a, len_b;

const int inf = 1000000;

int solve(int a, int b) {

    if (a == len_a && b == len_b) {
        return 0;
    }

    int &ret = memo[a][b];

    if (ret != -1) {
        return ret;
    }


    ret = inf;

    if (a + 1 < len_a, sa[a] == sa[a + 1]) {
        ret = min(ret, 1 + solve(a + 1, b));
    }

    if (sa[a] == sb[b]) {
        ret = min(ret, solve(a + 1, b + 1));
        ret = min(ret, 1 + solve(a, b + 1));
    }

    return ret;
}

int main() {
    int tests, n;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);

    scanf("%d", &tests);
    for (int case_no = 1; case_no <= tests; ++case_no) {
        scanf("%d", &n);
        scanf("%s", sa);
        scanf("%s", sb);
        len_a = strlen(sa);
        len_b = strlen(sb);
        memset(memo, -1, sizeof memo);
        int result = solve(0, 0);

        printf("Case #%d: ", case_no);

        if (result == inf) {
            printf("Fegla Won\n");
        }
        else {
            printf("%d\n", result);
        }
    }
}
