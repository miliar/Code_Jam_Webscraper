#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <hash_map>
#include <string>
#include <map>
#include <set>
#include <queue>

#if 0
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
typedef int1024_t lll;
typedef uint1024_t ulll;
#endif

using namespace std;
using namespace std::tr1;
using namespace stdext;

typedef __int64 ll;
typedef unsigned __int64 ull;


int T, N, J;

int main(int argc, char* argv[]) {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << (t + 1) << ":\n";
        cin >> N >> J;

        set<unsigned> a;
        a.insert(0x80018001);
        int d = 0x21;
        while (a.size() < (unsigned)J) {
            for (set<unsigned>::iterator it = a.begin(); it != a.end(); ++it) {
                unsigned x = *it;
                for (int sh = 0; sh < 25; ++sh) {
                    unsigned y = (d << sh);
                    if (x > y && ((x & y) == 0) && a.find(x | y) == a.end()) {
                        a.insert(x | y);
                        goto repeat;
                    }
                }
            }
            repeat: {}
        }
        int j = 0;
        for (set<unsigned>::iterator it = a.begin(); j < J; ++it, ++j) {
            unsigned x = *it;
            for (int sh = 0; sh < N; ++sh) {
                cout << ((x & (1 << (N - 1 - sh))) ? '1' : '0');
            }
#if 0
            for (int i = 2; i <= 10; ++i) {
                lll y = 0, q = 1;
                for (int sh = 0; sh < N; ++sh) {
                    y += ((x & (1 << (N - 1 - sh))) ? q : 0);
                    q *= i;
                }
                if (y % (i * i * i * i * i + 1) != 0)
                    throw int(42);
            }
#endif
            for (int i = 2; i <= 10; ++i) {
                cout << ' ' << (i * i * i * i * i + 1);
            }
            cout << '\n';
        }
    }
    return 0;
}
