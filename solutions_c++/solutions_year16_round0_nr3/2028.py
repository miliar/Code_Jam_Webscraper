#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>

const int N_PRIME = 10;
const int prime[N_PRIME] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
typedef __uint128_t u128;

using namespace std;

int divider[10];

void random_sampling(int n, char *s) {
    int r = rand() % (1 << (n-2));
    fill(s, s+n, '0');
    s[0] = '1';
    s[n-1] = '1';
    s[n] = '\0';
    for (int i = n-2; r; --i, r>>=1)
        if (r & 1)
            s[i] = '1';
}

u128 convert(char *s, int base) {
    u128 n = 0, b = 1;
    int l = strlen(s);
    for (int i = l-1; i >= 0; --i, b*=base)
        if (s[i] == '1')
            n += b;
    return n;
}

bool check(char *s) {
    u128 n;
    bool flag;
    for (int i = 2; i <= 10; ++i) {
        n = convert(s, i);
        flag = false;
        for (int j = 0; j < N_PRIME; ++j)
            if (n % prime[j] == 0) {
                divider[i-2] = prime[j];
                flag = true;
                break;
            }
        if (!flag) return false;
    }
    return true;
}

int main() {
    int n, j, T;
    char s[40];
    u128 tmp;
    set<u128> used;
    scanf("%d", &T);
    scanf("%d %d", &n, &j);
    srand(1126);
    printf("Case #1:\n");
    while (j--) {
        do {
            random_sampling(n, s);
            tmp = convert(s, 2);
            if (used.count(tmp) != 0)
                continue;
            used.insert(tmp);
        } while (!check(s));
        printf("%s", s);
        for (int i = 0; i < 9; ++i)
            printf(" %d", divider[i]);
        printf("\n");
    }
    return 0;
}
