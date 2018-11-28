#include <bits/stdc++.h>
#define D

bool cake[1005];

int main() {
    int nCases;
    scanf("%i\n", &nCases);

    for (int cas = 0; cas < nCases; cas++) {
        int len = 0;
        while (1) {
            char c;
            scanf("%c", &c);
            if (c == '+') {
                cake[len] = true;
                len++;
            } else if (c == '-') {
                cake[len] = false;
                len++;
            } else {
                break;
            }
        }

        int flipl;
        scanf("%i\n", &flipl);

        int steps = 0;
        for (int i = 0; i < (len-flipl+1); i++) {
            for (int j = 0; j < len; j++) {
                D(cake[j] ? "+" : "-");
            }
            D("\n");

            if (!cake[i]) {
                for (int j = i; j < (i+flipl); j++) {
                    cake[j] = !cake[j];
                }
                steps++;
            }
        }

        bool allGood = true;
        for (int j = 0; j < len; j++) {
            D(cake[j] ? "+" : "-");
            allGood = allGood && cake[j];
        }
        D("\n");

        if (allGood) {
            printf("Case #%i: %i\n", cas+1, steps);
        } else {
            printf("Case #%i: IMPOSSIBLE\n", cas+1);
        }
    }
    return 0;
}
