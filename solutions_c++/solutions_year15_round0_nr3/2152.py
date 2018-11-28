#include <iostream>
#include <cstdio>
#include <cstring>
#include "quaternion.h"
#include <cassert>

using namespace std;

quaternion str[10001];
ull slen, x;
char s[10001];

quaternion power(const quaternion &val, int pow) {
    if (val == O)
        return O;
    if (val == -O)
        return (pow % 2 ? -O : O);
    switch (pow % 4) {
        case 0 : return O;
        case 1 : return val;
        case 2 : return -O;
        case 3 : return -val;
    }
}

quaternion prefix(ull pos) {
    return power(str[slen], pos / slen) * str[pos % slen];
}

quaternion suffix(ull pos) {
    return (str[slen] / str[(pos + slen - 1) % slen + 1]) 
        * power(str[slen], (x * slen - pos) / slen);
}

int main() {
    int ttt;
    scanf("%d", &ttt);
    for (int qqq = 1; qqq <= ttt; qqq++) {
        scanf("%llu%llu\n%s", &slen, &x, s);
        str[0] = O;
        for (int i = 1; i <= slen; i++)
            str[i] = str[i - 1] * fromChar(s[i - 1]);
        bool ok = false;
        //ull ansI, ansJ;
        for (ull i = 1; !ok && i <= min(x, 8ULL) * slen; i++)
            if (prefix(i) == I)
                for (ull j = x * slen - 1; !ok && j >= max(i + 1, slen * (x - min(x, 8ULL))); j--)
                    if (suffix(j) == K) {
                        quaternion middle;
                        if (j / slen > i / slen)
                            middle = (str[slen] / str[i % slen])
                                   * power(str[slen], j / slen - i / slen - 1)
                                   * str[j % slen];
                        else
                            middle = str[(j + slen - 1) % slen + 1] / str[i % slen];
                        ok = (middle == J);
                        //if (ok) {
                        //    fprintf(stderr, "%llu %llu\n", i, j);
                        //    ansI = i;
                        //    ansJ = j;
                        //}
                    }
//        if (ok) {
//            quaternion check = O;
//            for (ull i = 0; i < ansI; i++)
//                check *= fromChar(s[i % slen]);
//            assert(check == I);
//            check = O;
//            for (ull i = ansI; i < ansJ; i++)
//                check *= fromChar(s[i % slen]);
//            assert(check == J);
//            check = O;
//            for (ull i = ansJ; i < x * slen; i++)
//                check *= fromChar(s[i % slen]);
//            assert(check == K);
//        }
        printf("Case #%d: %s\n", qqq, ok ? "YES" : "NO");
    }
    return 0;
}
