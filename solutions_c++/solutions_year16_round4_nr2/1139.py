#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>

using namespace std;

#define FOR(i, A, B) for(long long i=(A); i<(B); i++)
#define REP(i, N) for(long long i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define CLEAR(v) memset((v), 0, sizeof(v))
#define MP make_pair
#define PB push_back
#define PII pair<int, int>
#define LL long long

int N, K;
double p[201];

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        // cout << "Case #" << caso+1 << ": ";
        printf("Case #%d: ", caso+1);

        cin >> N >> K;
        REP(i, N) cin >> p[i];

        string vote = "";
        REP(i, K/2) vote += "YN";

        double best = 0.0;
        REP(mask, (1<<N)) {
            if(__builtin_popcount(mask) != K) continue;
            SORT(vote);
            double ptie = 0.0;
            do {
                int k = 0;
                double prob = 1.0;
                REP(i, N) {
                    if(!(mask&(1<<i))) continue;
                    if(vote[k] == 'Y') prob *= p[i];
                    else prob *= (1.0 - p[i]);
                    k++;
                }
                ptie += prob;
            } while(next_permutation(ALL(vote)));

            if(ptie > best) best = ptie;
        }

        // cout << best << endl;
        printf("%.8f\n", best);
    }
}
