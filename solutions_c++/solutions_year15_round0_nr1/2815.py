#include <algorithm>
#include <bitset>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
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
#include <cstdlib>
#include <ctime>

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
auto rc() { return read<char>(); };
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
    auto n = ri() + 1;
    vector<int> s(n);
    generate_n(begin(s), n, []
               {
                   return rc() - '0';
               });
    auto c = 0;
    auto invited = 0;
    for (auto i = 0; i < n; ++i)
    {
        //cout << "i " << i << " c " << c << " s[i] " << s[i] << endl;
        if (i > c)
        {
            invited += i - c;
            c += i - c;
        }
        c += s[i];
    }
    cout << invited;
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
