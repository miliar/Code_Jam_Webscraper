#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MAXN = 200 + 10;

struct PN {
	int sz;
	vector<double> v;

	PN() {}
	PN(double a, double b) {
		v.PB(a);
		v.PB(b);
		sz = 1;
	}

	PN operator*(const PN &b) const {
		PN *ret = new PN();
		ret->v.resize(sz + b.sz+1);
		ret->sz = sz+b.sz;
		for(int i=0; i<=sz; i++) {
			for(int j=0; j<=b.sz; j++) {
				ret->v[i+j] += (v[i]*b.v[j]);
			}
		}
		return *ret;
	}
};

double p[MAXN];

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		int n, k;
		scanf("%d%d", &n, &k);
		for(int i=0; i<n; i++)	scanf("%lf", p+i);
		
		double ans = 0;
		for(int i=0; i<(1<<n); i++) {
			PN tmp(1, 0);
			int cnt = 0;
			for(int j=0; j<n; j++) {
				if((i>>j) & 1)	cnt++;
			}
			if(cnt != k)	continue;

			for(int j=0; j<n; j++) {
				if((i>>j) & 1)	tmp = tmp*PN(p[j], 1-p[j]);
			}
			
			ans = max(ans, tmp.v[k/2]);
		}

		printf("Case #%d: %f\n", kase, ans);
	}
    
    return 0;
}
