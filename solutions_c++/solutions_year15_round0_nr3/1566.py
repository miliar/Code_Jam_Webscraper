#include <bits/stdc++.h>
using namespace std;

#define MAXL 10010

struct Factor {
    char letter;
    bool negative;

    Factor(char letter = '1', bool negative = 0) : letter(letter), negative(negative) {}

    Factor operator* (const Factor &o) const {
        if (letter == '1') {
            return Factor(o.letter, negative^o.negative);
        } else if (letter == 'i') {
            if (o.letter == '1')
                return Factor('i', negative^o.negative);
            else if (o.letter == 'i')
                return Factor('1', negative^o.negative^1);
            else if (o.letter == 'j')
                return Factor('k', negative^o.negative);
            else
                return Factor('j', negative^o.negative^1);
        } else if (letter == 'j') {
            if (o.letter == '1')
                return Factor('j', negative^o.negative);
            else if (o.letter == 'i')
                return Factor('k', negative^o.negative^1);
            else if (o.letter == 'j')
                return Factor('1', negative^o.negative^1);
            else
                return Factor('i', negative^o.negative);
        } else {
            if (o.letter == '1')
                return Factor('k', negative^o.negative);
            else if (o.letter == 'i')
                return Factor('j', negative^o.negative);
            else if (o.letter == 'j')
                return Factor('i', negative^o.negative^1);
            else
                return Factor('1', negative^o.negative^1);
        }
    }

    bool operator== (const Factor &o) const {
        return letter == o.letter && negative == o.negative;
    }
};

int main() {
    int T, L;
    long long X;
    char s[MAXL], ss[8*MAXL];
    Factor fl[8*MAXL], fr[8*MAXL];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %lld %s", &L, &X, s);
        bool ok = 0;
        if (X < 8) {
            ss[0] = 0;
            for (int i = 0; i < X; i++)
                strcat(ss, s);
            Factor f1('1', 0);
            for (int i = 0; i < X*L; i++) {
                f1 = f1 * Factor(ss[i], 0);
                fl[i] = f1;
            }
            Factor f2('1', 0);
            for (int i = X*L-1; i >= 0; i--) {
                f2 = Factor(ss[i], 0) * f2;
                fr[i] = f2;
            }
            bool findi = 0;
            for (int i = 0; i < X*L; i++) {
                if (fl[i] == Factor('i', 0))
                    findi = 1;
                if (findi && fl[i] == Factor('k', 0) && i+1 < X*L && fr[i+1] == Factor('k', 0)) {
                    ok = 1;
                    break;
                }
            }
        } else {
            ss[0] = 0;
            for (int i = 0; i < 8; i++)
                strcat(ss, s);
            Factor f1('1', 0);
            for (int i = 0; i < 8*L; i++) {
                f1 = f1 * Factor(ss[i], 0);
                fl[i] = f1;
            }
            Factor f2('1', 0);
            for (int i = 8*L-1; i >= 0; i--) {
                f2 = Factor(ss[i], 0) * f2;
                fr[i] = f2;
            }
            int rem = X % 4;
            Factor fk('1', 0);
            if (rem)
                fk = fr[8*L - rem*L];
            bool findi = 0;
            for (int i = 0; i < 8*L; i++) {
                if (fl[i] == Factor('i', 0))
                    findi = 1;
                if (findi && fl[i] == Factor('k', 0)) {
                    if (i+1 == 8*L && fk == Factor('k', 0)) {
                        ok = 1;
                        break;
                    }
                    if (i+1 < 8*L && fr[i+1] * fk == Factor('k', 0)) {
                        ok = 1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %s\n", t, ok ? "YES" : "NO");
    }
}
