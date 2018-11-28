/*****************************************************************************
 * codeforces:   knst
 * topcoder:     knstqq
 * projecteuler: knstqq
 * **************************************************************************/

#include <algorithm>
#include <iostream>
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
    int n;
    cin >> n;
    int cards[4][4];
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            cin >> cards[i][j];
    int m;
    cin >> m;
    int cards2[4][4];
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            cin >> cards2[i][j];

    int count = 0;
    int last = -1;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (cards[n-1][i] == cards2[m-1][j]) {
                ++count;
                last = cards[n-1][i];
            }
        }
    }
    cout << "Case #" << test << ": ";
    if (count == 0)
        cout << "Volunteer cheated!" << endl;
    if (count == 1)
        cout << last << endl;
    if (count > 1)
        cout << "Bad magician!" << endl;
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
