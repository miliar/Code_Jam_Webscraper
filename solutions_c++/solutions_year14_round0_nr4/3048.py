/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : d.cpp

* Creation Date : 12-04-2014

* Last Modified : Saturday 12 April 2014 10:55:20 PM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include <iterator>
#include <cctype>
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
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <climits>
#include <limits>
#include <string>
using namespace std;

//Macros
#define dbl double
#define ll long long
#define ull unsigned long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define vi vector<int>
#define vll vector<ll>

#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))

#define MOD 1000000007
#define MAXN 100010
#define MAXBUF 5000000
#define EPS 1e-9
#define NIL 0
#define INF (INT_MAX/2)
#define LLINF (LONG_LONG_MAX/2LL)
#define NEWLINE '\n'

#define SET(A) memset(A, 1,sizeof(A));                     //NOTE: Works only for x = 0 and -1. Only for integers.
#define CLR(A) memset(A, 0,sizeof(A));
#define MEM(A,x) memset(A,x,sizeof(A));
#define CPY(A,B) memcpy(A,B,sizeof(A));

#define SIZE(A) ((int)(A.size()))
#define ALL(x)  x.begin(),x.end()
#define FILL(A,x) fill(ALL(A),x)
#define REP(i,N) for(int i=0;i<(int)(N); ++i)
#define FORab(i,a,b) for(int i=(int)(a);i<=(int)(b); ++i)
#define RFORab(i,a,b) for(int i=(int)(a);i>=(int)(b); --i)
#define FOR1(i,n) FORab(i,1,(n))
#define RFOR1(i,n) RFORab(i,(n),1)
#define FOR(i,n) FORab(i,0,(n)-1)
#define RFOR(i,n) RFORab(i,(n)-1,0)
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define SORTV(x) sort(ALL(x))
#define REVV(x) reverse(ALL(x))

#define mp make_pair
#define pb push_back
#define ff first
#define ss second

#define nbits(n) __builtin_popcount(n)                  //NOTE: Works only for int. Write your own function for long long :-/
#define atbit(x,i) (((x)>>(i))&1)
#define FIXMOD(a) (((a)%MOD+MOD)%MOD)

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

int main() {
    int t;
    cin>>t;
    REP(T, t) {
        int n;
        cin>>n;
        vector<double> lst, arr;
        lst.resize(n); arr.resize(n);
        REP(i, n) cin>>lst[i];
        REP(i, n) cin>>arr[i];
        sort(lst.begin(), lst.end());
        sort(arr.begin(), arr.end());
        reverse(lst.begin(), lst.end());
        set<double> sec_set;
        REP(i, n) sec_set.insert(arr[i]);
        int met = 0;
        set<double>::iterator it;
        REP(i, n) {
            it = sec_set.lower_bound(lst[i]);
            if(it == sec_set.end()){
                met++;
                sec_set.erase(sec_set.begin());
                continue;
            }
            sec_set.erase(it);
        }
        
        int sec = 0;
        set<double> my_set;
        REP(i, n) my_set.insert(lst[i]);
        REP(i, n) {
            it = my_set.upper_bound(arr[i]);
            if(it == my_set.end()) {
                my_set.erase(my_set.begin());
                continue;
            } 
            sec++;
            my_set.erase(it);
        }
        cout<<"Case #"<<(T+1)<<": "<<sec<<" "<<met<<endl;
    }
	return 0;
}
