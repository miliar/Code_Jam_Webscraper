#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <functional>
#include <set>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <fstream>
#include <bitset>
#include <time.h>
#include <assert.h>

#define LL long long
#define FOR(i,a,b) for(int i= (a); i<((int)b); ++i)
#define RFOR(i,a) for(int i=(a); i >= 0; --i)
#define FOE(i,a) for(auto i : a)
#define SZ(x) ((int)(x).size())
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define AND &&
#define OR ||
#define NOT !
#define SUM(x) std::accumulate(ALL(x), 0LL)
#define EPS 1e-14

template<typename T> inline void DUMP(T x) { std::cerr << x << std::endl; }
template<typename T> inline void DUMP_V(std::vector<T> v) { for (unsigned int i = 0; i < v.size(); ++i) { std::cerr << v[i] << ((i == v.size() - 1) ? "n" : " "); } }
template<typename T> inline void DUMP_V2(std::vector<std::vector<T>> v) { for (unsigned int i = 0; i < v.size(); ++i) { for (unsigned int j = 0; j < v[i].size(); ++j) { std::cerr << v[i][j] << " "; } std::cerr << std::endl; } }

using namespace std;

int solve(string s) {
    int ans = s[0] == '-';
    FOR(i, 0, SZ(s) - 1) {
        char a = s[i], b = s[i + 1];
        if (a == '+' AND b == '-') {
            ans += 2;
        }
    }
    return ans;
}


int main() {
    int t;
    string s;
    cin >> t;
    vector<int> ans_list;
    FOR(i, 0, t) {
        cin >> s;
        int ans = solve(s);
        ans_list.push_back(ans);
    }
    FOR(i, 0, t) {
        cout << "Case #" << i + 1 << ": " << ans_list[i] << endl;
    }

    return 0;
}
