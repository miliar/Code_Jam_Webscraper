#include <bits/stdc++.h>



int get_answer(int x) {
    if (x == 0)
        return -1;
    bool has_digit[10] = {};
    int c_digits = 10;
    int res;
    for (int cur = x; c_digits != 0; cur += x) {
        res = cur;
        int tmp = cur;
        while (tmp != 0) {
            int dig = tmp % 10;
            tmp /= 10;
            if (!has_digit[dig]) {
                has_digit[dig] = true;
                --c_digits;
            }
        }
    }
    return res;
}

int main(int argc, char **argv) {
    FILE *in = fopen(argv[1], "r");
    FILE *out = fopen(argv[2], "w");
    int n;
    fscanf(in, "%d", &n);
    for (int i = 1; i <= n; ++i) {
        int x;
        fscanf(in, "%d", &x);
        int ans = get_answer(x);
        fprintf(out, "Case #%d: ", i);
        if (ans == -1)
            fputs("INSOMNIA\n", out);
        else
            fprintf(out, "%d\n", ans);
    }
}
