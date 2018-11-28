#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
#include <iomanip>

using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()
#define mp(a,b) make_pair((a),(b))

#define RESET(c,x) memset (c, x, sizeof (c))

#define oo 1000111000

#define PI acos(-1.0)
#define fi first
#define se second
#define SIZE(c) (c).size()


typedef vector<int> VI ;
typedef vector<string> VS ;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

template<class T> inline int size(const T&c) { return c.size(); }

using namespace std;
int fastMax(int x, int y) { return (((y-x)>>(32-1))&(x^y))^y; }
int fastMin(int x, int y) { return (((y-x)>>(32-1))&(x^y))^x; }

const double eps = 0.000000001;
int T;
int n;
double V, XG;
double R[100+10];
double X[100+10];

bool eq(double a, double b) {
	return abs(a - b) <= eps;
}

int main() 
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for (int tt = 1; tt <= T; tt++) {
    	cin>>n>>V>>XG;
    	for (int i = 0; i < n; i++) {
    		cin>>R[i]>>X[i];
    		X[i] = X[i] - XG;
    	}
    	cout<<"Case #"<<tt<<": ";
    	if (n == 1) {
    		if (eq(0,X[0])) {
    			cout<<fixed<<setprecision(7)<<V / R[0]<<endl;
    		} else {
    			cout<<"IMPOSSIBLE"<<endl;
    		}
    	}
    	if (n == 2) {
    		if (eq(X[0], X[1])) {
    			if (X[0] == 0)
    				cout<<fixed<<setprecision(7)<<V / (R[0] + R[1])<<endl;
    			else
    				cout<<"IMPOSSIBLE"<<endl;
    		} 
    		else {
    			double t0 = (V * X[1]) / (X[1] - X[0]) / R[0];
    			double t1 = (V * X[0]) / (X[0] - X[1]) / R[1];
    			if (t0 >= 0 && t1 >= 0)
    				cout<<fixed<<setprecision(9)<<max(t0, t1)<<endl;
    			else 
	    			cout<<"IMPOSSIBLE"<<endl;
    		} 
    	}
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}