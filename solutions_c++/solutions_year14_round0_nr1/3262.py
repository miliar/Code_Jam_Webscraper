#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <cmath>
#include <set>
#include <utility>

#define eps 1e-9
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define sz(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define ms(x,i) memset((x),(i),sizeof((x)))
#define debug(x) if(DEBUG) cout << x << endl
#define DEBUG 1

using namespace std;

typedef long long ll;
typedef pair<int,int> pt;
typedef pair<pt,int> ppt;
const int nmax = 1000013;
int t, p, q;
int a[5][5];
map<int,int> mymap;
map<int,int> :: iterator it;
void input() {
    cin >> p;
    FOR(i,0,3) {
        FOR(j,0,3) {
            cin >> a[i][j];
            if(p == i+1) {
                mymap[a[i][j]]++;
            }
        }
    }
}
void solve(int test) {
    int ans = -232;
    cout << "Case #" << test << ": ";
    mymap.clear();
    input();
    input();
    ans = sz(mymap);
    if(ans == 8) {
        cout << "Volunteer cheated!" << endl;
        return;
    }
    if(ans < 7) {
        cout << "Bad magician!" << endl;
        return;
    }
    for(it = mymap.begin(); it != mymap.end(); it++) {
        if(it->se == 2) {
            cout << it->fi << endl;
            return;
        }
    }
}
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out","w",stdout);
    std::ios::sync_with_stdio(false);
    cin >> t;
    FOR(i,1,t) {
        solve(i);
    }
    return 0;
}
