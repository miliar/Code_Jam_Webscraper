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

int T, K, C, S;

int main(int argc, char* argv[]) {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << (t + 1) << ":";
        cin >> K >> C >> S;
        if (K == 1 || C == 1) {
            if (S < K) {
                cout << "IMPOSSIBLE";
            } else {
                for (int i = 1; i <= S; ++i) {
                    cout << " " << i;
                }
            }
        } else {
            for (int i = 2; i <= K; ++i) {
                cout << " " << i;
            }
        }
        cout << "\n";
    }
    return 0;
}
