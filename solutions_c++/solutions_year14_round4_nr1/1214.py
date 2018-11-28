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
#define MAX(a,b) ((a)>(b)?(a):(b))
int ABS(int a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
#endif
}

int a[100005];

int main() {
    // input();
    int t;
    cin >> t;
    int tst = 1;
    while ( t-- ) {
        int n,x;
        cin >> n >> x;
        F(i,0,n) cin >> a[i];
        sort(a,a+n);

        int i = 0, j = n-1;
        int ans = 0;

        while ( i < j ) {
            if ( a[i] + a[j] <= x ) {
                i++; j--;
                ans++;
            } else {
                j--; ans++;
            }
        }

        if ( i == j ) ans++;

        cout << "Case #" << tst++ << ": ";
        cout << ans << endl;
    }
    return 0;
}
