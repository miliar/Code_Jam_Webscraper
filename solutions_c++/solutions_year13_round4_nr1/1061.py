#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>
#include <deque>
#include <map>
#include <set>
#include <vector>

using namespace std;

const int32_t MOD = 1000002013;
const int32_t N = 10001;

typedef struct Seg {
    int32_t o, e, p;
}Seg;
Seg A[N];
int32_t n, m;

int32_t CalcD(int32_t o, int32_t e, int32_t p) {
    int32_t d = e - o;
    return 1LL * d * (2 * n - d + 1) / 2 % MOD * p % MOD;
}
int32_t main() {
    int32_t cas = 0;
    scanf("%d", &cas);
    for (int32_t ic = 1; ic <= cas; ic++) {
        scanf("%d%d", &n, &m);
        set<int32_t> S;
        map<int32_t, int32_t> O, E;
        for (int32_t i = 0; i < m; i++) {
            scanf("%d%d%d", &A[i].o, &A[i].e, &A[i].p);
            O[A[i].o] += A[i].p;
            E[A[i].e] += A[i].p;
            S.insert(A[i].o);
            S.insert(A[i].e);
        }
        int32_t ans = 0;
        for (int32_t i = 0; i < m; i++) {
            ans = (ans + CalcD(A[i].o, A[i].e, A[i].p)) % MOD;
        }
        deque<pair<int32_t, int32_t> > person;
        for (set<int32_t>::iterator it = S.begin(); it != S.end(); ++it) {
            //printf("station %d\n", *it);
            if (O[*it] > E[*it]) {
                person.push_back(make_pair(*it, O[*it] - E[*it]));
            } else if (O[*it] < E[*it]) {
                int32_t d = E[*it] - O[*it];
                int32_t s = 0;
                for (int32_t i = person.size() - 1; i >= 0; i--) {
                    s += person[i].second;
                    if (s >= d) {
                        if (s == d) {
                            ans = (ans - CalcD(person.back().first, *it, person.back().second)) % MOD;
                            person.pop_back();
                        } else {
                            ans = (ans - CalcD(person.back().first, *it, person.back().second - (s - d))) % MOD;
                            person.back().second -= person.back().second - (s - d);
                        }
                        break;
                    }
                    ans = (ans - CalcD(person.back().first, *it, person.back().second)) % MOD;
                    //printf("(%d, %d, %d) = %d\n", person.back().first, *it, person.back().second, ans);
                    person.pop_back();
                }
            }
        }
        if (ans < 0) {
            ans += MOD;
        }
        printf("Case #%d: %d\n", ic, ans);
    }
    return 0;
}
