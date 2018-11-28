/* Divanshu Garg */

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
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%llu",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
ill ABS(ill a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    // freopen("D-small-attempt0.in","r",stdin);
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
}

/* Input opener ends */

int main() {
    // input();
    int t, tst = 1;
    cin >> t;
    // cout << t << endl;
    while ( t-- ) {
        double a[1002], b[1002];
        int n; cin >> n;
        F(i,0,n) cin >> a[i];
        F(i,0,n) cin >> b[i];
        sort(a,a+n);
        sort(b,b+n);
        // F(i,0,n) cout << a[i] << " "; cout << endl;
        // F(i,0,n) cout << b[i] << " "; cout << endl;
        
        int i = 0, j = n-1;

        i = 0, j = 0;
        while ( i < n && j < n ) {
            while ( j < n && a[j] < b[i] ) j++;
            if ( j == n ) break;
            i++; j++;
        }
        
        cout << "Case #" << tst++ << ": ";
        cout << i << " ";

        i = 0, j = 0;
        while ( i < n && j < n ) {
            while ( j < n && b[j] < a[i] ) j++;
            if ( j == n ) break;
            i++; j++;
        }

        cout << n-i << endl;

    }
    return 0;
}