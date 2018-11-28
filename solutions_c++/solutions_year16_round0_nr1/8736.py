/*
 * Header file available here:
 * https://github.com/JosephConrad/GoogleCodeJam/tree/master/2016
 */
#include "../../template.h"


bool allDigits(const LL pInt[10]) {
    for (int i = 0; i < 10; i++) {
        if (pInt[i] == 0) {
            return false;
        }
    }
    return true;
}


std::string solve(LL number) {
    if (number == 0)
        return "INSOMNIA";
    LL tab[10];
    for (int i = 0; i < 10; i++) {
        tab[i] = 0;
    }
    LL num = number;
    LL multiplier = 1;
    while (allDigits(tab) == false) {
        num = multiplier * number;
        multiplier++;
        LL x = num;
        while (x > 0) {
            tab[x % 10] = 1;
            x /= 10;
        }
    }
    return std::to_string(num);
}


int main() {

#ifndef GOOGLE_CODE_JAM
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    clock_t start = clock();

    LL T, i;
    scanf("%lld", &T);

    REP(cc, T) {
        scanf("%lld", &i);
        printf("Case #%d: %s\n", cc + 1, solve(i).c_str());
    }
    fprintf(stderr, "*** Total time: %.3lf seconds ***\n",
            ((clock() - start) / (double) CLOCKS_PER_SEC));
    return 0;
}
