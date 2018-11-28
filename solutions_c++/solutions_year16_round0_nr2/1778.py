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
char l[256];

int main(int argc, char* argv[]) {
    cin >> T;
    cin.getline(l, 255);
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << (t + 1) << ": ";
        cin.getline(l, 255);
        int a = 0;
        for (int i = 0; i < 255; ++i) {
            if (l[i+1] == 0) {
                if (l[i] == '-') ++a;
                break;
            }
            if (l[i] != l[i+1]) ++a;
        }
        cout << a << "\n";
    }
    return 0;
}
