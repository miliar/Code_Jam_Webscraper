#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string.h>

using namespace std;

char table[4][4] = {{'1', 'i', 'j', 'k'}, {'i', -'1', 'k', -'j'}, {'j', -'k', -'1', 'i'}, {'k', 'j', -'i', -'1'}};
char revtable[4][4] = {{'1', -'i', -'j', -'k'}, {'i', '1', 'k', -'j'}, {'j', -'k', '1', 'i'}, {'k', 'j', -'i', '1'}};

// mult: a * b, div: a / b
char eval(char a, char b, bool mult) {
    int parity = 1;
    if (a < 0) {
        parity *= -1;
        a *= -1;
    }
    if (b < 0) {
        parity *= -1;
        b *= -1;
    }
    switch(a) {
        case '1':a = 0;break;
        case 'i':a = 1;break;
        case 'j':a = 2;break;
        case 'k':a = 3;break;
    }
    switch(b) {
        case '1':b = 0;break;
        case 'i':b = 1;break;
        case 'j':b = 2;break;
        case 'k':b = 3;break;
    }
    if (mult)
        return table[a][b] * parity;
    return revtable[a][b] * parity;
}

char string[10001], xprods[10001];
int L;
unsigned long long X;

bool possible() {
    register char *iptr, *jptr, *kptr;
    register int ilevel, jlevel, klevel;
    char kchar = eval(xprods[X - 1], string[L - 1], true);
    for (iptr = string, ilevel = 0; *iptr != '\0';) {
        char ichar = eval(xprods[ilevel], *iptr, true);
        if (iptr[1] == '\0' && ilevel < X) {
            ilevel++;
            iptr = string;
        }
        else
            iptr++;
        if (ichar == 'i') {
            for (jptr = iptr, jlevel = ilevel; *jptr != '\0';) {
                char jchar = eval(xprods[jlevel], *jptr, true);
                if (jptr[1] == '\0' && jlevel < X) {
                    jlevel++;
                    jptr = string;
                }
                else
                    jptr++;
                if (eval(jchar, ichar, false) == 'j') {
                    char kchar = eval(xprods[X - 1], string[L - 1], true);
                    if (eval(kchar, jchar, false) == 'k')
                        return true;
                }
            }
        }
    }
    return false;
}

int main() {
    int T;
    scanf("%d", &T);
    register int i, cases;
    for (cases = 0; cases < T; cases++) {
        scanf("%d %llu", &L, &X);
        char ch;
        while (getchar() != '\n');
        scanf("%s", string);
        //printf("%c%c", string[0] < 0 ? '-' : ' ', string[0] < 0 ? -string[0] : string[0]);
        for (i = 1; i < L; i++) {
            string[i] = eval(string[i - 1], string[i], true);
            //printf(" %c%c", string[i] < 0 ? '-' : ' ', string[i] < 0 ? -string[i] : string[i]);
        }
        //printf("\n");
        xprods[0] = '1';
        for (i = 1; i < X; i++)
            xprods[i] = eval(xprods[i - 1], string[L - 1], true);

        printf("Case #%d: %s\n", cases + 1, possible() ? "YES" : "NO");
    }
}
