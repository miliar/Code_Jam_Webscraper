// Copyright (C) 2016 Sayutin Dmitry.
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License as
// published by the Free Software Foundation; version 3

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program; If not, see <http://www.gnu.org/licenses/>.

#include <iostream>
#include <vector>
#include <stdint.h>
#include <algorithm>
#include <set>
#include <map>
#include <array>
#include <queue>
#include <stack>
#include <functional>
#include <utility>
#include <string>
#include <assert.h>
#include <iterator>

using std::cin;
using std::cout;
using std::cerr;

using std::vector;
using std::map;
using std::array;
using std::set;
using std::string;

using std::pair;
using std::make_pair;

using std::min;
using std::abs;
using std::max;

template <typename T>
T input() {
    T res;
    cin >> res;
    return res;
}

#ifdef LOCAL
#define LASSERT(X) assert(X)
#else
#define LASSERT(X) {}
#endif

double get_ans(const vector<double>& selected) {
    // dp[i][j].
    vector<vector<double>> dp(selected.size());
    for (size_t i = 0; i != selected.size(); ++i) {
        dp[i].resize(i + 2);
        if (i == 0) {
            dp[0][0] = (1 - selected[0]);
            dp[0][1] = selected[0];
        } else {
            dp[i][i + 1] = selected[i] * dp[i - 1][i];
            dp[i][0] = (1 - selected[i]) * dp[i - 1][0];
            
            for (size_t j = 1; j != i + 1; ++j)
                dp[i][j] = (1 - selected[i]) * dp[i - 1][j] + selected[i] * dp[i - 1][j - 1];
        }
    }
    return dp.back()[selected.size() / 2];
}

vector<double> data;
vector<double> cur;

double brute(size_t start, size_t left) {
    if (start == data.size()) {
        if (left == 0)
            return get_ans(cur);
        else
            return -1;
    } else {
        double best = -1;
        if (left != 0) {
            cur.push_back(data[start]);
            best = brute(start + 1, left - 1);
            cur.pop_back();
        }
        
        return max(best, brute(start + 1, left));
    }
}

int main() {
    std::iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cout << std::fixed;
    cout.precision(10);
    
    size_t T;
    cin >> T;
    for (size_t t = 1; t <= T; ++t) {
        data.resize(input<size_t>());
        assert(cur.size() == 0);
        
        size_t K = input<size_t>();
        std::generate(data.begin(), data.end(), input<double>);

        cout << "Case #" << t << ": " << brute(0, K) << "\n";
    }
    
    return 0;
}
