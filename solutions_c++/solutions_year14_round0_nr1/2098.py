#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <time.h>
#include <cctype>
#include <functional>
#include <deque>
#include <iomanip>
#include <bitset>
#include <assert.h>
#include <numeric>
#include <sstream>
#include <utility>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FORD(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,b) FOR(i,0,b)
#define ll long long
#define sf scanf
#define pf printf
using namespace std;
const int maxint = -1u>>1;
const double pi = 3.14159265358979323;
const double eps = 1e-8;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<int>::iterator vit;

int vis[20], a[8][8];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, ca = 0;
    int row;
    cin >>T;
    while (T--) {
        memset(vis, 0, sizeof(vis));
        cin >>row;
        FOR(i, 1, 5)
            FOR(j, 1, 5) cin >>a[i][j];
        FOR(i, 1, 5) vis[a[row][i]]++;
        cin >>row;
        FOR(i, 1, 5)
            FOR(j, 1, 5) cin >>a[i][j];
        FOR(i, 1, 5) vis[a[row][i]]++;
        int ans = -1;
        for (int i = 1; i <= 16; ++i) {
            if (vis[i] == 2) {
                if (ans == -1) ans = i;
                else {
                    ans = -2;
                }
            }
        }
        if (ans >= 0) 
            cout <<"Case #" <<++ca <<": " <<ans <<endl;
        else if (ans == -2) 
            cout <<"Case #" <<++ca <<": Bad magician!"  <<endl;
        else if (ans == -1) {
            cout <<"Case #" <<++ca <<": Volunteer cheated!"  <<endl;
        }
    }
    return 0;
}

