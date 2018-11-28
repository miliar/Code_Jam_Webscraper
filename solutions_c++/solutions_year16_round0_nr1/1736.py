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
typedef int256_t lll;
typedef uint256_t ulll;
#endif

using namespace std;
using namespace std::tr1;
using namespace stdext;

typedef __int64 ll;
typedef unsigned __int64 ull;

int T;
ll N;

int main(int argc, char* argv[]) {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N;
        cout << "Case #" << (t + 1) << ": ";
        if (N == 0) {
            cout << "INSOMNIA";
        } else {
            ll M = 0;
            for (int d = 0; d != 0x3FF; ) {
                M += N;
                for (ll L = M; L > 0; L /= 10) {
                    int K = (int)(L % 10);
                    d = d | (1 << K);
                }
            }
            cout << M;
        }

        cout << "\n";
    }
    return 0;
}
