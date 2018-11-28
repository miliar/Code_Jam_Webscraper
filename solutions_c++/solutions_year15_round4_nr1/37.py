#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

const int N = 1000;

char img[N][N];
// u d l r
bool can[N][N][4];
char c[5] = "^v<>";

void solve(int test_id) {
    int n, m;
    cin >> n >> m;
    REP(i, n) cin >> img[i];
    bool is_valid = true;
    int answer = 0;
    REP(i, n) REP(j, m) REP(k, 4) can[i][j][k] = true;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (img[i][j] != '.') {
                can[i][j][2] = false;
                break;
            }
        }
        for (int j = m - 1; j >= 0; --j) {
            if (img[i][j] != '.') {
                can[i][j][3] = false;
                break;
            }
        }
    }
    for (int j = 0; j < m; ++j) {
        for (int i = 0; i < n; ++i) {
            if (img[i][j] != '.') {
                can[i][j][0] = false;
                break;
            }
        }
        for (int i = n - 1; i >= 0; --i) {
            if (img[i][j] != '.') {
                can[i][j][1] = false;
                break;
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            bool any = false;
            for (int k = 0; k < 4; ++k) {
                if (can[i][j][k]) any = true;
                if (img[i][j] == c[k] && !can[i][j][k]) {
                    ++answer;
                }
            }
            if (!any) {
                is_valid = false;
            }
        }
    }
    cout << "Case #" << test_id << ": ";
    if (is_valid) {
        cout << answer << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int tests;
    cin >> tests;
    for (int test_id = 1; test_id <= tests; ++test_id) {
        solve(test_id);
    }
    return 0;
}