#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string.h>
#include <utility>
#include <vector>

using namespace std;

using vi = vector<int>;
using vc = vector<char>;
using vd = vector<double>;
using vl = vector<long long>;
using vvi = vector<vector<int>>;
using vvc = vector<vector<char>>;
using vvd = vector<vector<double>>;
using vvl = vector<vector<long long>>;

template <typename T>
auto read()
{
    T i;
    cin >> i;
    return i;
}
auto rc() { return read<char>(); };
auto ri() { return read<int>(); };
auto rd() { return read<double>(); };
auto rl() { return read<long long>(); };
auto rs() { return read<string>(); };

void test_case(int case_num)
{
    auto cakes = rs();

    auto K = ri();

    auto flips = 0;

    for (auto i = 0; i < cakes.size() - K + 1; ++i) {
        if (cakes[i] == '-') {
            ++flips;
            for (auto j = 0; j < K; ++j) {
                cakes[i+j] = cakes[i+j] == '+' ? '-' : '+';
            }
        }
    }

    for (auto i = cakes.size() - K; i < cakes.size(); ++i) {
        if (cakes[i] == '-') {
            cout << "IMPOSSIBLE";
            return;
        }
    }
    cout << flips;
}

void run()
{
    auto num_cases = ri();
    cout << fixed << setprecision(7);
    for (auto i = 0; i < num_cases; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        test_case(i);
        cout << endl;
    }
}

// int main() { run(); }
