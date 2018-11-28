#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <bitset>
#include <utility>
#include <cstring>

using namespace std;

const long double EPS = 1e-8;
const long double PI = 3.1415926535897932384626433832795;
const long double E = 2.7182818284;
const int INF = 1000000000;

typedef long long ll;
typedef long double ld;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define pb push_back
#define all(a) a.begin(), a.end()
#define mp make_pair;
#define X first
#define Y second

int main(void)
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;
        int a[n][m];
        for(int j = 0; j < n; j++) {
            for(int h = 0; h < m; h++) {
                cin >> a[j][h];
            }
        }
        int max_kol[m];
        int max_row[n];
        for (int j = 0; j < n; j++) {
            max_row[j] = a[j][0];
            for(int h = 1; h < m; h++) {
                if (max_row[j] < a[j][h]) max_row[j] = a[j][h];
            }
        }

        for(int h = 0; h < m; h++) {
            max_kol[h] = a[0][h];
            for(int j = 1; j < n; j++) {
                if (max_kol[h] < a[j][h]) max_kol[h] = a[j][h];
            }
        }

        int res = 0;
        for(int j = 0; j < n; j++) {
            if (res) break;
            for(int h = 0; h < m; h++) {
                if (a[j][h] != min(max_kol[h], max_row[j])) {
                    res = 1;
                    break;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (res) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
    return 0;
}
