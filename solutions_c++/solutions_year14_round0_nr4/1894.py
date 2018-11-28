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
const int N = 1111;

int n, ansx, ansy;
double naomi[N], ken[N];
bool vis[N];

int find_first_notvis_big(double x) {
    REP(i, n) {
        if (vis[i]) {
            if (ken[i] > x) return i;
        }
    }
    return -1;
}
int main() 
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T, ca = 0;
    cin >>T;
    while (T--) {
        cin >>n;
        REP(i, n) cin >>naomi[i];
        REP(i, n) cin >>ken[i];
        sort(naomi, naomi + n);
        sort(ken, ken + n);
        ansx = ansy = 0;
        
        //ansy
        set<double> tset;
        memset(vis, true, sizeof(vis));
        REP(i, n) tset.insert(ken[i]);
        REP(i, n) {
            set<double>::iterator iter = tset.upper_bound(naomi[i]);
            if (iter == tset.end()) ansy++;
            else tset.erase(iter);
        }
        
        //ansx
        int ken_max_ptr = n - 1;
        ansx = 0;
        int l = 0, r = n - 1;
        while (l <= r) {
            if (naomi[r] > ken[ken_max_ptr]) {
                ansx++;
                r--;
            }
            else {
                l++;
            }
            ken_max_ptr--;
        }
        cout <<"Case #" <<++ca <<": " <<ansx <<" "<<ansy <<endl;
    }
    return 0;
}

