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

int main(int argc, char* argv[]) {
    char S[1024];
    cin >> T; cin.getline(S, 1024);
    for (int t = 0; t < T; ++t) {
        cin.getline(S, 1024);
        string Q;
        Q += S[0];
        for (int i = 1; i < 1024; ++i) {
            if (S[i] == 0) {
                break;
            }
            if (S[i] < Q.front()) {
                Q = Q + S[i];
            } else {
                Q = S[i] + Q;
            }
        }
        cout << "Case #" << (t + 1) << ": " << Q;
        cout << "\n";
    }
    return 0;
}
