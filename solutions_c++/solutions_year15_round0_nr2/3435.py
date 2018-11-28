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
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
}

/* Input opener ends */

int a[1005];

int main() {
    // input();
    
    int t, kase = 1; cin >> t;
    while ( t-- ) {

        int n; cin >> n;
        F(i,0,n) {
            cin >> a[i];
        }

        int ans = 1001;
        FD(i,1001,1) {
            int moves = i;
            F(j,0,n) {
                if ( a[j] > i ) {
                    int left = a[j] - i;
                    moves += (left+i-1)/i;
                }
            }
            ans = min(ans,moves);
        }
        
        printf("Case #%d: %d\n", kase++, ans);

    }

    return 0;
}