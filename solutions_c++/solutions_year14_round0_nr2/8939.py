/*****************************************************************************
 * codeforces:   knst
 * topcoder:     knstqq
 * projecteuler: knstqq
 * **************************************************************************/

#include <algorithm>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>

using namespace std;
//test speed
/*
namespace std {
    template <class T1, class T2>
    class hash<pair<T1, T2>> {
    public:
        size_t operator()(const pair<T1, T2>& p) const {
            return hash<T1>()(p.first) & hash<T2>()(p.second);
        }
    };
}; */
namespace std {
    template <>
    class hash<pair<long long,long long>> {
    public:
        size_t operator()(const pair<long long, long long>& p) const {
            return hash<long long>()(p.first) ^ (hash<long long>()(p.second) << 32);
        }
    };
};

void solve(int test) {
    cout << "Case #" << test << ": ";

    double c;
    double f;
    double x;
    cin >> c >> f >> x;
    double minimum = std::numeric_limits<double>::max();
    double time = x / 2.0;
    double sum = 0.0;
    int count = 0;
    do {
        minimum = time;
        sum += c / (2.0 + count * f);
        time = sum + x / (2.0 + (count + 1) * f);
        ++count;
    } while (time < minimum);
    cout.precision(15);
    cout << minimum << endl;
}    


int main() {
    std::ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        solve(test);
    }

    return 0;
}
