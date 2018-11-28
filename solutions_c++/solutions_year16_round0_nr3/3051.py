#include <cstdio>

const int LEN = 16;
int value[LEN];
int ans[LEN];

inline long long divisor(long long value) {
    for(long long i = 2; i * i <= value; i++) {
        if (value % i == 0) {
            return i;
        }
    }
    return -1;
}

inline bool validate_candidate() {
    for(int base = 2; base <= 10; base++) {
        long long res = 0;
        long long power = 1;
        for(int i = 0; i < LEN; i++) {
            if (value[i]) res += power;
            power *= base;
        }   
        int prep = divisor(res);
        if (prep != -1) ans[base] = prep;
        else return false;
    }
    for(int i = 0; i < LEN; i++)
        printf("%d", value[LEN - i - 1]);
    for(int i = 2; i <= 10; i++)
        printf(" %d", ans[i]);
    puts("");
    return true;
}

void solve(int count) {
    puts("Case #1:");
    value[0] = 1, value[LEN - 1] = 1;
    int st = 0;
    for(int i = 0; i < (1 << (LEN - 2)); i++) {
        if (count == 0) {
        //    puts("ALL FOUND!");
            return;
        }
        for(int j = 0; j < LEN - 2; j++)
            value[j + 1] = (i >> j) & 1;
        if (validate_candidate()) {
            count -= 1;
        } else {
         //   puts("FAILED ATTEMPT");
        }
    }
}


int main() {
    solve(50);
}
