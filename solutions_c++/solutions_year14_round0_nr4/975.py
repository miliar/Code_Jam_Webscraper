#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
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
#define INFL  numeric_limits<long>::max()
#define INFLL numeric_limits<llong>::max()
#define INFD  numeric_limits<double>::max()
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

int n;

bool check(double* naomi, double* ken, int ptrn) {
    bool res = true;
    FOR(i,ptrn,n) {
        if (naomi[i] < ken[i-ptrn]) {
            res = false;
            break;
        }
    }
    return res;
}

void solve() {
    cin >> n;
    double naomi[n];
    double ken[n];
    FORZ(i,n) cin >> naomi[i];
    FORZ(i,n) cin >> ken[i];
    sort(naomi, naomi+n);
    sort(ken, ken+n);
    
    int i = 0;
    int j = n-1;
    while (!check(naomi, ken, i)) {
        i++;
        j--;
    }
    cout << n-i << " ";
    
    i = 0; j = 0;
    int cnt = 0;
    while (i < n && j < n) {
        if (naomi[i] > ken[j]) {
            j++;
        }
        else {
            i++;
            j++;
            cnt++;
        }
    }
    cout << n-cnt << endl;
}

int main() {
#ifdef DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t; cin >> t;
    FORZ(i,t) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
