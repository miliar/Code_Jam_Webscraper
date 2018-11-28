#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

#define pairii pair<int, int>
#define llong long long
#define pb push_back
#define sortall(x) sort((x).begin(), (x).end())
#define INFI  numeric_limits<int>::max()
#define INFLL numeric_limits<llong>::max()
#define INFD  numeric_limits<double>::max()
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

void solve() {
    int n,x;
    cin >> n >> x;
    vector<int> disc;
    disc.resize(n);
    FORZ(i,n) cin >> disc[i];
    sortall(disc);
    vector<bool> vis(n,0);
    int res = 0;
    FORZ(i,n) {
        if (vis[i]) continue;
        vis[i] = true;
        bool found = false;
        for (int j = n-1; j > i; j--) {
            if (vis[j]) continue;
            if (disc[i]+disc[j] <= x) {
                res++;
                found = true;
                vis[j] = true;
                break;
            }
        }
        if (!found) res++;
        
    }
    
    cout << res << endl;
}

int main() {
#ifdef DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t;
    scanf("%d", &t);
    FOR(i,1,t+1) {
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
