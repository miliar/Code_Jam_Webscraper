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

struct Matrix {
    char field[4][4];
};

bool brute(size_t N, const Matrix& mat, size_t cur, const vector<size_t>& order, size_t badmask) {
    if (cur == N) {
        return true;
    }

    size_t haschoice = 0;
    for (size_t j = 0; j != N; ++j)
        if (mat.field[order[cur]][j] and (badmask & (1u << j)) == 0) {
            ++haschoice;
            if (not brute(N, mat, cur + 1, order, badmask | (1u << j)))
                return false;
        }
    return haschoice != 0;
}

bool check(size_t N, const Matrix& mat) {
    vector<size_t> order(N);
    std::iota(order.begin(), order.end(), 0);
    
    do  {
        if (not brute(N, mat, 0, order, 0))
            return false;
    } while (std::next_permutation(order.begin(), order.end()));

    return true;
}

int main() {
    std::iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    auto T = input<size_t>();
    for (size_t t = 1; t <= T; ++t) {
        size_t N = input<size_t>();

        Matrix data;
        for (size_t i = 0; i != N; ++i)
            for (size_t j = 0; j != N; ++j)
                data.field[i][j] = input<char>() == '1';
        
        size_t ans = SIZE_MAX;
        if (check(N, data))
            ans = 0;
        else {
            size_t THECNT = N * N; // amount of ones.
            size_t globalmask = 0;
            for (size_t i = 0; i != N; ++i)
                for (size_t j = 0; j != N; ++j)
                    if (data.field[i][j] == 0)
                        globalmask |= (1u << (i * N + j)), --THECNT;
            if (THECNT <= 1)
                ans = N - THECNT;
            else {
                for (size_t msk = globalmask; msk != 0; msk = (msk - 1) & globalmask) {
                    Matrix newmat = data;
                    size_t DELTA = 0;
                    for (size_t i = 0; i != N; ++i)
                        for (size_t j = 0; j != N; ++j)
                            if (msk & (1u << (i * N + j)))
                                newmat.field[i][j] = true, ++DELTA;
                    if (check(N, newmat))
                        ans = min(ans, DELTA);
                }
            }
        }

        printf("Case #%d: %d\n", int(t), int(ans));
    }
    
    return 0;
}
