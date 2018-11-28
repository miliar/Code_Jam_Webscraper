// includes {
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cctype>
// }
using namespace std;
// defines {
#define FOR(i,n) for((i)=0; (i)<(n); (i)++)
#define REP(i,n) for((i)=1; (i)<=(n); (i)++)
#define SET(a,v) memset(a, v, sizeof(a))
#define SZ(a) (int)(a).size()
#define LEN(a) (int)(a).length()
#define PB push_back
#define all(a) (a).begin(), (a).end()
#define sqr(a) (a)*(a)
#define inrange(lb,i,ub) ((lb) <= (i) && (i) <= (ub))
#define foreach(it, a) for(typeof((a).begin()) it=(a).begin(); it != (a).end(); it++)
// }
typedef pair<double,double> dd;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double TIPO ;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
	int T=0; cin >> T;
	int cont = 1;

	while (T--){
        TIPO C,F,X;
        cin >> C >> F >> X;
        TIPO max_time = X/2;
        int n=0;
        TIPO actual=0,before=0,opt=0;
        while( true ){
            TIPO sum=0;
            for( int i = 0 ; i < n ; i ++){
                sum +=C/(2+i*F);
            }
            sum+=X/(2+n*F);
            before = actual;
            actual = sum;
            if ( before == 0 ) before = actual;
            opt = min ( actual, before );
            n++;
            if ( actual > before ) break;
        }
        printf("Case #%d: %.7f\n",cont++,opt);
	}
	return 0;
	}
