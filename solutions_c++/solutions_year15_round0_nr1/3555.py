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
    size_t T;
    cin >> T;

    for (size_t test = 0; test < T; ++test) {
        int maxshy = 0;
        cin >> maxshy;

        string line;
        cin >> line;

        vector<int> vals(maxshy + 1, 0);
        for (size_t i = 0; i < vals.size(); ++i) {
            vals[i] = line[i] - '0';
        }

        int presum = 0;
        int ans = 0;
        for (size_t i = 0; i < vals.size(); ++i ) {
            if (presum < i) {
                ++ans;
                ++presum;
            }

            presum += vals[i];
        }

        cout << "Case #" << test + 1 << ": " << ans << "\n";
    }

    return 0;
}
