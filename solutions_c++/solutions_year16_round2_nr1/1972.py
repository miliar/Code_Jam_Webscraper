#define _CRT_SECURE_NO_WARNINGS
// #define _GLIBCXX_DEBUG
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <deque>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <ctime>
#include <iterator>
#include <bitset>
#include <numeric>
#include <list>
#include <iomanip>
#include <cassert>
#include <array>
#include <tuple>
#include <initializer_list>
#include <unordered_set>
#include <unordered_map>
#include <forward_list>
using namespace std;
typedef long long ll;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
#define all(c) begin(c), end(c)

using vi = vector<int>;
using vii = vector < vector<int>>;

//namespace std {
//    template<class T>
//    ostream &operator << (ostream &os, const vector<T> &v) {
//        os << "[";
//        for (auto it != v.begin(); it != v.end(); ++it) {
//            os << it << (it + 1 != v.end() ? "," << "");
//        }
//        return os << "]";
//    }
//    void show_grid(const vector<string> &g) {
//        for (auto &e : g) cout << e << '\n';
//        cout << flush;
//    }
//}

string solve(string s) {
    map<char, int> cnt;
    for (auto &c : s) {
        cnt[c] ++;
    }
    static const vector<string> dig = {
        "ZERO",
        "SIX",
        "TWO",
        "FOUR",
        "ONE",
        "EIGHT",
        "FIVE",
        "SEVEN",
        "THREE",
        "NINE"
    };
    
    static const string key   = "ZXWUOGFVTE";
    static const string ord_n = "0624185739";

    string ans;
    for (int i = 0; i < 10; ++i) {
        // cerr << key[i] << endl;
        int x = cnt[key[i]];
        for (char c : dig[i]) {
            assert(cnt[c] >= x);
            cnt[c] -= x;

            if (cnt[c] == 0) {
                cnt.erase(c);
            }
        }
        ans += string(x, ord_n[i]);
    }

    assert(cnt.size() == 0);

    sort(ans.begin(), ans.end());
    return ans;
}


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        // cout << s << endl;
        string ans = solve(s);
        printf("Case #%d: %s\n", i + 1, ans.c_str());
    }
}