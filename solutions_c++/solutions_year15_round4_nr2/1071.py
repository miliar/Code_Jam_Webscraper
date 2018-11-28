//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-12
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 110

int sgn(long double x) {
	if (fabs(x) < eps) return 0;
	return x < 0 ? -1 : 1;
}

int n;
long double V, X;
struct Pipe {
	long double R, C;
	long double t;
}data[N];

bool cmp(const Pipe & a, const Pipe &b) {
	return a.C < b.C;
}

bool check(long double T) {
	Rep(i, n) data[i].t = 0;
	long double sumV = 0, sumC = 0, A, B;
	Rep(i, n) {
		data[i].t = min(T, (V - sumV) / data[i].R);
		sumV += data[i].t * data[i].R;
		sumC += data[i].t * data[i].R * data[i].C;
	}
	if (fabs(sumV - V) > eps) return false;
	A = sumC;
	sumV = 0, sumC = 0;
	Rep(k, n) {
		int i = n - k - 1;
		data[i].t = min(T, (V - sumV) / data[i].R);
		sumV += data[i].t * data[i].R;
		sumC += data[i].t * data[i].R * data[i].C;
	}
	B = sumC;
	if (sgn(A - X) == 1) return false;
//	if (sgn(A - X) == 0) return false;
	if (sgn(B - X) == -1) return false;
//	if (sgn(B - X) == 0) return false;
	return true;
}

long double solve() {
	if (n == 1) {
		if (sgn(data[0].C - X) != 0) return -1;
		else return V / data[0].R;
	}
	if (sgn(data[0].C - X) == 0 && sgn(data[1].C - X) == 0) {
		return V / (data[0].R + data[1].R);
	}
	if (sgn(data[0].C - X) == 0) {
		return V / data[0].R;
	}
	if (sgn(data[1].C - X) == 0) {
		return V / data[1].R;
	}
	if (sgn(data[0].C - X) == sgn(data[n - 1].C - X)) return -1;
	long double t2 = V * (X - data[0].C) / (data[1].C - data[0].C) / data[1].R ;
	long double t1 = (V - data[1].R * t2) / data[0].R;
	return max(t1, t2);
}

int		main(){
	int cas , tt = 0;
	scanf("%d", &cas);
	while (cas --) {
		cin >> n >> V >> X;
		Rep(i, n) 
			cin >> data[i].R >> data[i].C;
		long double ans = solve();
		printf("Case #%d: ", ++tt);
		if (ans < 0) puts("IMPOSSIBLE");
		else {
			printf("%.12Lf\n", ans);
		}
	}
	return 0;
}
