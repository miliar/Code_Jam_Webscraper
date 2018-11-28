#include <algorithm>
#include <initializer_list>
#include <numeric>
#include <system_error>
#include <array>
#include <iomanip>
#include <ostream>
#include <thread>
#include <atomic>
#include <ios>
#include <queue>
#include <tuple>
#include <bitset>
#include <iosfwd>
#include <random>
#include <type_traits>
#include <chrono>
#include <iostream>
#include <ratio>
#include <typeindex>
#include <codecvt>
#include <istream>
#include <regex>
#include <typeinfo>
#include <complex>
#include <iterator>
#include <scoped_allocator>
#include <unordered_map>
#include <condition_variable>
#include <limits>
#include <set>
#include <unordered_set>
#include <deque>
#include <list>
#include <sstream>
#include <utility>
#include <exception>
#include <locale>
#include <stack>
#include <valarray>
#include <forward_list>
#include <map>
#include <stdexcept>
#include <vector>
#include <fstream>
#include <memory>
#include <streambuf>
#include <functional>
#include <mutex>
#include <string>
#include <future>
#include <new>
#include <strstream>
using namespace std;


namespace Debug {

    template<typename F, typename S>
    ostream &operator<<(ostream &os, const pair<F, S> &p) {
        return os << "{" << p.first << ", " << p.second << "}";
    }

    template<typename T>
    ostream &operator<<(ostream &os, const vector<T> &v) {
        os << "[";
        typename vector<T>::const_iterator it;
        for (it = v.begin(); it != v.end(); it++) {
            if (it != v.begin()) os << ", ";
            os << *it;
        }
        return os << "]";
    }

    template<typename T>
    ostream &operator<<(ostream &os, const set<T> &v) {
        os << "[";
        typename set<T>::const_iterator it;
        for (it = v.begin(); it != v.end(); it++) {
            if (it != v.begin()) os << ", ";
            os << *it;
        }
        return os << "]";
    }

    template<typename F, typename S>
    ostream &operator<<(ostream &os, const map<F, S> &v) {
        os << "[";
        typename map<F, S>::const_iterator it;
        for (it = v.begin(); it != v.end(); it++) {
            if (it != v.begin()) os << ", ";
            os << it->first << " = " << it->second;
        }
        return os << "]";
    }

#define deb(x) cerr << #x << " = " << x << endl;
}

using namespace Debug;

typedef long long i64;
typedef unsigned long long ui64;
typedef pair<int,int> pii;

#define mx 110
#define IN "/Users/bidhanroy/ClionProjects/A/in"
#define OUT "/Users/bidhanroy/ClionProjects/A/out"

int R, C;

char grid[ mx ][ mx ];
int reach[ mx ][ mx ];

void solve(int kas) {
    cout << "Case #" << kas << ": ";

    cin >> R >> C;

    for(int i = 0; i < R; i++ ) cin >> grid[i];

    int cnt = 0;

    memset(reach, 0, sizeof reach);

    for(int i = 0; i < R; i++ ) {
        for(int j = 0; j < C; j++ ) {
            if(grid[i][j] == '.') continue;
            if(grid[i][j] != '<') {
                reach[i][j]++;
                break;
            }
            cnt++;
            reach[i][j]++;
            break;
        }

        for(int j = C-1; j >= 0; j-- ) {
            if(grid[i][j] == '.') continue;
            if(grid[i][j] != '>') {
                reach[i][j]++;
                break;
            }
            cnt++;
            reach[i][j]++;
            break;
        }
    }

    //cout << kas << endl;
    //cout << "--" << endl;

    //cout << cnt << endl;

    for(int j = 0; j < C; j++ ) {
        for(int i = 0; i < R; i++ ) {
            //cout << i << " " << j << " = " << grid[i][j] << endl;
            if(grid[i][j] == '.') continue;
            if(grid[i][j] != '^') {
                reach[i][j]++;
                break;
            }
            //cout << i << " " << j << endl;
            cnt++;
            reach[i][j]++;
            break;
        }
    }

    for(int j = 0; j < C; j++ ) {
        for(int i = R-1; i >= 0; i-- ) {
            if(grid[i][j] == '.') continue;
            if(grid[i][j] != 'v') {
                reach[i][j]++;
                break;
            }
            cnt++;
            reach[i][j]++;
            break;
        }
    }

    for(int i = 0; i < R; i++ ) {
        for(int j = 0; j < C; j++ ) {
            if(reach[i][j] > 3 ) {
                cout << "IMPOSSIBLE" << endl;
                return ;
            }
        }
    }

    cout << cnt << endl;

}

int main() {
    freopen( IN, "r", stdin);
    freopen( OUT, "w", stdout);
    using namespace chrono;
    time_t start=system_clock::to_time_t(system_clock::now());
    //ios_base::sync_with_stdio(0);
    int test, kas=0;
    cin>>test;
    while( test-- ) {
        solve(++kas);
    }
    time_t end = system_clock::to_time_t(system_clock::now());
    //cout << " Program has run "<< end-start << " s " << endl;
    return 0;
}