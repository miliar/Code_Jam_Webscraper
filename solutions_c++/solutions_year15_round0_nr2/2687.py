#include <algorithm>
#include <bitset>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <utility>
#include <vector>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <ctime>


// Pancake's house

using namespace std;

namespace
{
template <typename T>
auto read(istream& is = cin)
{
    T i;
    is >> i;
    return i;
}
auto rl() { return read<long long>(); };
auto ri() { return read<int>(); };
auto rd() { return read<double>(); };
auto rs() { return read<string>(); };

auto gl()
{
    string s;
    getline(cin, s);
    return s;
}


void test_case(int case_num)
{
    auto d = ri();
    vector<int> p(d);
    generate_n(begin(p), d, ri);

    auto maxp = *max_element(p.cbegin(), p.cend());

    auto minutes = INT_MAX;
    for (auto i = 1; i <= maxp; ++i)
    {
        auto specials = 0;
        auto maxleft = 0;
        for (auto& j : p)
        {
            if (i<j)
            {
                specials += j / i;
                if (j % i == 0)
                {
                    --specials;
                }
                maxleft = max(maxleft, i);
            }
            else
            {
                maxleft = max(maxleft, j);
            }
        }
        minutes = min(specials + maxleft, minutes);
    }
    cout << minutes;
}
}

int main()
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
