#include <iostream>
#include <sstream> 
#include <cstdio>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdlib> 
#include <ctime>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
template<typename T> T ABS(const T& val) { return val < 0 ? -val : val; }


int main ()
{
    std::ios_base::sync_with_stdio(false);

    int T;
    while (cin >> T) {
        for (int test = 1; test <= T; ++test) {
            int N, X;
            cin >> N >> X;

            int ans = 0;
            typedef multiset<int, std::greater<int> > elems_t;
            elems_t elems;
            for (int i = 0; i < N; ++i) {
                int val;
                cin >> val;
                elems.insert(val);
            }

            while (!elems.empty()) {
                int big = *elems.begin();
                elems.erase(elems.begin());
                elems_t::iterator it = elems.lower_bound(X - big);

                if (it != elems.end()) {
                    elems.erase(it);
                }

                ++ans;
            }

            cout << "Case #" << test << ": " << ans << "\n";
        }
    }


    return 0;
}
