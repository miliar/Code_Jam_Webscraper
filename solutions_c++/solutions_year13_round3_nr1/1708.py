// Fruit of Light
// FoL CC
// Orange Strawberry
// Som mudra, pekna a sikovna
// Sikovnejsia ako vcera!

#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <unistd.h>  // for fork() in ASSERT macro
#include <vector>

using namespace std;
using namespace std::tr1;

#ifdef EBUG
#define DEBUG(x) \
    cerr << "DEBUG (F " << __FUNCTION__ << ", L" << __LINE__ << "): " << #x << ": " << x << endl
#define DBG  if (1)
#define DPRINTF(args...)  fprintf(stderr, args)
#define ASSERT(x) \
    if (!(x)) fprintf(stderr, "!!! L%d, F %s: Assertion `%s' failed!\n", __LINE__, __FUNCTION__, #x);
#else
#define DEBUG(x)
#define DBG if (0)
#define DPRINTF(args...)
#define ASSERT(x)  if (!(x)) fork()
#endif

#define FORRANGE(i, ma) for (int i = 0; i < (ma); i++)
#define FORRANGE1(i, ma) for (int i = 1; i <= (ma); i++)
#define FOREACH(it, data) for (typeof((data).begin()) it = (data).begin(); it != (data).end(); ++it)
#define ITER(x) typeof((x).begin())

typedef long long int ll;
typedef unsigned long long int llu;

#define mp make_pair

template <class T1, class T2> ostream& operator<< (ostream& os, const pair<T1, T2>& p) {
    return os << "pair(" << p.first << "," << p.second << ")";
}

// =============================================================================

typedef pair<int, int> P;

char buf[10000000];
vector<bool> ones(10000000);
vector<int> S(10000000);
int main() {
    int _T; scanf("%d", &_T); FORRANGE1(_t, _T) {
        int n; scanf("%s%d", buf, &n);
        int L = strlen(buf);
        FORRANGE(i, L) {
            switch (buf[i]) {
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                    ones[i] = 0;
                    break;
                default:
                    ones[i] = 1;
                    break;
            }
        }
        int val = 0;
        FORRANGE(beg, L)
            FORRANGE(end, L) {
                int S = 0;
                for (int i = beg; i <= end; ++i) {
                    if (ones[i]) S += 1; else S = 0;
                    if (S >= n) { val++; break; }
                }
            }

        printf("Case #%d: %d\n", _t, val);

    }
    return 0;
}
