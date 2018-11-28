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

struct Tree {
    char ch;
    Tree* left;
    Tree* right;
};

char combine(char a, char b) {
    if (not (a < b))
        std::swap(a, b);
    if (a == 'P' and b == 'R')
        return 'P';
    if (a == 'P' and b == 'S')
        return 'S';
    return 'R';
}

std::map<char, char> loser_of {{'R', 'S'}, {'P', 'R'}, {'S', 'P'}};

string gen(size_t depth_left, char ch) {    
    if (depth_left != 0) {
        string s1 = gen(depth_left - 1, ch);
        string s2 = gen(depth_left - 1, loser_of[ch]);
        return min(s1, s2) + max(s1, s2);
    } else {
        return string("") + ch;
    }
}

int main() {
    std::iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    size_t t = input<size_t>();
    for (size_t i = 1; i <= t; ++i) {
        size_t N, P, R, S;
        cin >> N >> R >> P >> S;
        string best = "";
        for (char ch : {'R', 'P', 'S'}) {
            string s = gen(N, ch);
            size_t P1 = 0, R1 = 0, S1 = 0;
            for (char ch : s) {
                if (ch == 'P')
                    ++P1;
                if (ch == 'R')
                    ++R1;
                if (ch == 'S')
                    ++S1;
            }

            if ((P1 == P and R1 == R and S1 == S) and (best == "" or best > s)) {
                best = std::move(s);
            }
        }

        if (best == "")
            best = "IMPOSSIBLE";
        
        printf("Case #%d: %s\n", (int)i, best.c_str());
    }
    
    return 0;
}
