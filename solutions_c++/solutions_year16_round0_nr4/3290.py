#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <climits>
#include <cfloat>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stdexcept>

using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ULL unsigned long long
#define LL long long
#define REP(i,n) for(int i=0;i<(n);i++)
#define set_bit(x, i) (x) |= (1 << (i))
#define clr_bit(x, i) (x) & ~(1 << (i))
#define tog_bit(x, i) (x) ^= (1 << (i))
#define chk_bit(x, i) (((x) >> (i)) & 1)
#define feq(x,y) (fabs(x-y) <= DBL_EPSILON)

#define MAXN 65536

#define MOD 1000000007

typedef pair<int,int> ii;
#define mp make_pair


#define sq(x) ((x)*(x))


ULL ullpow(int x, int base) {
	ULL ans = 1;
	while(base--) {
		ans *= x;
	}
	return ans;
}


//#define ONLINE_JUDGE
int main() {

#ifndef ONLINE_JUDGE
	//freopen("test", "r", stdin);
	freopen("in-small", "r", stdin);
	freopen("out-small", "w+", stdout);
#endif

	int testcases = 0;
	scanf("%d", &testcases);
	for(int k=1;k<=testcases;k++) {
		//ULL x = rand() % 100000;
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		cout<<"Case #"<<k<<": ";
		if( C == 1 || K == 1 ) {
			for(int i=0;i<K;i++) {
				if(i > 0)
					cout<<" ";
				cout<<i+1;
			}
		}
		else {
			ULL step = ullpow(K, C-1);
			ULL x = 2;
			ULL px = x;
			for(int i=0;i<K-1;i++) {
				if(i > 0)
					cout<<" ";
				cout<<x;
				x += step + 1;
				if( x < px ) {
					cout<<"   fuck   ";
				}
				px = x;
			}
		}
		cout<<endl;
		
	}

	return 0;
} 


