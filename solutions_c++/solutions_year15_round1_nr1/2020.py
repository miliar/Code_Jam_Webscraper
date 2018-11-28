#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<stack>
#include<fstream>
#include<sstream>
#include<map>
#include<algorithm>
#include<cassert>
#include<vector>
#include<climits>
#include<set>


#define DEBUG 0
#define SMALL 0
#define LARGE 1

using namespace std;
#if DEBUG
#define LOG(a) cerr << "value of " << #a << ":" << a << endl
#define LOG(a,b) LOG(a);LOG(b)
#define LOG(a,b,c) LOG(a,b);LOG(c)
#define LOG(a,b,c,d) LOG(a,b);LOG(c,d)
#else
#define LOG(a) 
#define LOG(a,b) 
#define LOG(a,b,c) 
#define LOG(a,b,c,d) 
#endif

#define si(a) scanf("%d",&a)
#define sl(a) scanf("%I64d",&a);

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()


typedef long long int64;
typedef unsigned long long uint64;

#define MAX 1010

struct greaterValue {
	bool operator() (int a, int b) {
		return a>b;
	}
};
int a[2000];
int main() {
#if SMALL
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
#endif
#if LARGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	int T,D,N,W,H;
	int y,z,d,m;
	si(T);
	for(int i=1;i<=T;i++) {
		si(N);
		for(int j=0;j<N;j++) si(a[j]);
		z=0;
		y=0;
		d=0; m=INT_MIN;
		REP(j,N-1) {
			if(a[j]>=a[j+1]) {
				d = (a[j]-a[j+1]);
				if(d > m) m=d;
				y+=d;
			}
		}
		z=0;
		REP(j,N-1) {
			if(a[j]>=m) z+=m;
			else z+=a[j];
		}
		cout << "Case #" << i << ": "<<y<< " "<<z<<endl;

	}
	return 0;
}
