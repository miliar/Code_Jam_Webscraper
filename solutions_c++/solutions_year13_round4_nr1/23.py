// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

const long long MOD = 1000002013;

int main() {
    int T; cin >> T;
    FOR(t,1,T) {
        long long N;
        int M;
        cin >> N >> M;
        vector<long long> O(M), E(M), P(M);
        REP(m,M) cin >> O[m] >> E[m] >> P[m];

        long long would_pay = 0;
        REP(m,M) {
            long long s = E[m] - O[m];
            long long cena1 = s*(2*N-s+1)/2;
            cena1 %= MOD;
            long long cenaall = (cena1 * P[m]) % MOD;
            would_pay += cenaall;
        }

        map< long long, long long > nastupi, vystupi;
        set< long long > events;
        REP(m,M) {
            nastupi[ O[m] ] += P[m];
            vystupi[ E[m] ] += P[m];
            events.insert( O[m] );
            events.insert( E[m] );
        }

        long long really_pay = 0;
        vector< long long > odkial, kolko_listkov;
        for (long long kde : events) {
            // najskor nastup
            if (nastupi[kde] > 0) {
                odkial.push_back(kde);
                kolko_listkov.push_back(nastupi[kde]);
            }
            // potom vystup
            if (vystupi[kde] > 0) {
                long long este = vystupi[kde];
                while (este > 0) {
                    long long skade, teraz;
                    if (kolko_listkov.back() <= este) {
                        skade = odkial.back(); odkial.pop_back();
                        teraz = kolko_listkov.back(); kolko_listkov.pop_back();
                    } else {
                        kolko_listkov.back() -= este;
                        skade = odkial.back();
                        teraz = este;
                    }
                    este -= teraz;
                    // zaplatime za prave vystupujuce listky
                    long long s = kde - skade;
                    long long cena1 = s*(2*N-s+1)/2;
                    cena1 %= MOD;
                    long long pocet = (teraz % MOD);
                    long long cenaall = (cena1 * pocet) % MOD;
                    really_pay += cenaall;
                }
            }
        }
        long long answer = (would_pay - really_pay) % MOD;
        answer = (answer + MOD) % MOD;
        cout << "Case #" << t << ": " << answer << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
