#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <set>
#include <inttypes.h>
using namespace std;
struct qu_t {
    int x; // 1 i j k
    bool neg;
    qu_t() {
        x = 0;
        neg = false;
    }
    qu_t(int x, bool neg): x(x), neg(neg) { }
    qu_t(char c) {
        neg = false;
        if (c == 'i')
            x = 1;
        else if (c == 'j')
            x = 2;
        else if (c == 'k')
            x = 3;
        else throw 0;
    }
    bool operator==(const qu_t &that) const {
        return x == that.x && neg == that.neg;
    }
    bool operator!=(const qu_t &that) const {
        return !(*this == that);
    }
    bool operator<(const qu_t &that) const {
        if (x != that.x)
            return x < that.x;
        return neg < that.neg;
    }
    qu_t operator-() const {
        return qu_t(x, !neg);
    }
    qu_t inv() const {
        switch (x) {
          case 0:
            return qu_t(0, neg);
          case 1:
            return qu_t(1, true ^ neg);
          case 2:
            return qu_t(2, true ^ neg);
          case 3:
            return qu_t(3, true ^ neg);
          default: 
            throw 0;
        }
    }
    qu_t operator*(const qu_t &q2) const {
        switch (x) {
          case 0:
            switch(q2.x) {
              case 0:
                return qu_t(0, neg ^ q2.neg);
              case 1:
                return qu_t(1, neg ^ q2.neg);
              case 2:
                return qu_t(2, neg ^ q2.neg);
              case 3:
                return qu_t(3, neg ^ q2.neg);
            }
          case 1:
            switch(q2.x) {
              case 0:
                return qu_t(1, neg ^ q2.neg);
              case 1:
                return qu_t(0, true ^ neg ^ q2.neg);
              case 2:
                return qu_t(3, neg ^ q2.neg);
              case 3:
                return qu_t(2, true ^ neg ^ q2.neg);
            }
          case 2:
            switch(q2.x) {
              case 0:
                return qu_t(2, neg ^ q2.neg);
              case 1:
                return qu_t(3, true ^ neg ^ q2.neg);
              case 2:
                return qu_t(0, true ^ neg ^ q2.neg);
              case 3:
                return qu_t(1, neg ^ q2.neg);
            }
          case 3:
            switch(q2.x) {
              case 0:
                return qu_t(3, neg ^ q2.neg);
              case 1:
                return qu_t(2, neg ^ q2.neg);
              case 2:
                return qu_t(1, true ^ neg ^ q2.neg);
              case 3:
                return qu_t(0, true ^ neg ^ q2.neg);
            }
        }
        throw 0;
    }
};
char str[20005];
qu_t qus[20005];
qu_t qus_rev[20005];
int64_t L, X;
bool solve() {
    qu_t block;
    for (int i = 0; i < L; ++i)
        block = block * qus[i];

    // any q, q ^ 4 == 1
    int r = X % 4;
    qu_t prd;
    for (int i = 0; i < r; ++i)
        prd = prd * block;
    // printf("prd %d %d\n", prd.x, prd.neg);
    if (prd != qu_t(0, true)) {
        return false;
    }
    
    // find first part
    int first_pos;
    {
        bool found = false;
        qu_t acc = qu_t();
        set<qu_t> s;
        for (int part = 0; part < X; ++part) {
            if (s.count(acc))
                return false;
            s.insert(acc);
            for (int pos = 0; pos < L; ++pos) {
                if (acc == qu_t('i')) {
                    first_pos = part * L + pos;
                    found = true;
                    break;
                }
                acc = acc * qus[pos];
            }
            if (found)
                break;
        }
        if (!found)
            return false;
        // printf("f %d\n", first_pos);
    }
    int last_pos;
    {
        bool found = false;
        qu_t acc = qu_t();
        set<qu_t> s;
        for (int part = 0; part < X; ++part) {
            if (s.count(acc))
                return false;
            s.insert(acc);
            for (int pos = 0; pos < L; ++pos) {
                if (acc == -qu_t('k')) {
                    last_pos = part * L + pos;
                    found = true;
                    break;
                }
                acc = acc * qus_rev[pos];
            }
            if (found)
                break;
        }
        if (!found)
            return false;
        // printf("l %d\n", first_pos);
    }
    // printf("%d %d;\n", first_pos, last_pos);
    return first_pos + last_pos < L * X;
}
int main(){
    int T, i, ca;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%" PRId64 "%" PRId64 "%s", &L, &X, str);
        for (int i = 0; i < L; ++i) {
            qus[i] = qu_t(str[i]);
            qus_rev[L - 1 - i] = qus[i].inv();
        }
        printf("Case #%d: %s\n", ca, solve()?"YES":"NO");
    }
    return 0;
}
