#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define FOREACH(i,v) for(typeof((v).begin()) i = (v).begin();i!=(v).end();i++)

#define PI 3.1415926535897932384626433832795
#define INF 0x7FFFFFFF

#define MOD 1000002013

typedef pair<int, int> PII;

map<int, int> oindex, eindex;

int oo[1000 + 5];
int ee[1000 + 5];
int oocnt;
int eecnt;

int pp[1000 + 5][1000 + 5];

int main(int argc, char **argv)
{
    int T;
    scanf("%d ", &T);
    REP(t, T) {
        oindex.clear();
        eindex.clear();
        memset(oo, 0, sizeof(oo));
        memset(ee, 0, sizeof(ee));
        oocnt = 0;
        eecnt = 0;
        memset(pp, 0, sizeof(pp));

        int N, M;
        scanf("%d %d ", &N, &M);
        REP(m, M) {
            int o, e, p;
            scanf("%d %d %d ", &o, &e, &p);
            if (oindex.count(o) == 0) {
                oindex[o] = oocnt;
                oo[oocnt++] = o;
            }
            if (eindex.count(e) == 0) {
                eindex[e] = eecnt;
                ee[eecnt++] = e;
            }
            pp[oindex[o]][eindex[e]] += p;
        }

        long long sum = 0;
        bool done = false;

        while (!done) {
            done = true;

            for (int idxo1 = 0;idxo1 < oocnt;idxo1++) {
                for (int idxe1 = 0;idxe1 < eecnt;idxe1++) {
                    for (int idxo2 = 0;idxo2 < oocnt;idxo2++) {
                        for (int idxe2 = 0;idxe2 < eecnt;idxe2++) {

                            int o1 = oo[idxo1], e1 = ee[idxe1], p1 = pp[idxo1][idxe1];
                            int o2 = oo[idxo2], e2 = ee[idxe2], p2 = pp[idxo2][idxe2];

                            if (o1 < o2 && o2 <= e1 && e1 < e2 && p1 != 0 && p2 != 0) {
                                done = false;
                                long long pdiff = min(p1, p2) % MOD;
                                long long odiff = (o2 - o1) % MOD;
                                long long ediff = (e2 - e1) % MOD;

                                long long sumi = pdiff;
                                sumi = (sumi * odiff) % MOD;
                                sumi = (sumi * ediff) % MOD;

                                sum = (sum + sumi) % MOD;

                                pp[idxo1][idxe1] -= pdiff;
                                pp[idxo2][idxe2] -= pdiff;
                                pp[idxo1][idxe2] += pdiff;
                                pp[idxo2][idxe1] += pdiff;
                            }
                        }
                    }
                }
            }
        }

        printf("Case #%d: %d\n", t + 1, int(sum % MOD));
    }

    return 0;
}

