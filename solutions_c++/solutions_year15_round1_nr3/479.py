#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>
#define EPS 1e-9

using namespace std;

struct P {
	double x, y;
	P() {}
	P( double x, double y ): x(x), y(y) {}
	void eat() { scanf( "%lf%lf", &x, &y ); }
	void out() { printf( "(%f, %f)", x, y ); }

	P operator+( P p ) { return P( x + p.x, y + p.y ); }
	P operator-( P p ) { return P( x - p.x, y - p.y ); }
	P operator*( double s ) { return P( x * s, y * s ); }
	double operator*( P p ) { return x * p.x + y * p.y; }
	double operator^( P p ) { return x * p.y - y * p.x; }
	bool operator<( const P p ) const { return x != p.x ? x < p.x : y < p.y; }

	double mag() { return sqrt( x * x + y * y ); }
	double mag2() { return x * x + y * y; }

	P nor() { return * this * ( 1.0 / mag() ); }

	P rot() { return P( -y, x ); }
	P rot( double si, double co ) { return P( x * co - y * si, x * si + y * co ); }
	P rot( double th ) { return rot( sin( th ), cos( th ) ); }
};

/* convex hull weapon */
P p[55555], ch[55555];
int n, m; // n, m - # of points in original polygon / convex hull

bool mult(const P sp,const P ep,const P op){
	return (sp.x - op.x) * (ep.y - op.y) - (ep.x - op.x) * (sp.y - op.y) >= EPS;
}
void convex_hull(){
	int i, len;
	m = 1;
	sort(p, p + n);
	if(n == 0) {m = 0; return;} ch[0]=p[0];
	if(n == 1) {m = 1; return;} ch[1]=p[1];
	if(n == 2) {m = 2; return;} ch[2]=p[2];
	for(i = 2; i < n; i++){
		while(m && mult(p[i],ch[m],ch[m - 1])) m--;
		ch[++m] = p[i];
	}
	len = m; ch[++m] = p[n - 2];
	for(i = n - 3; i >= 0; i--){
		while(m != len && mult(p[i], ch[m], ch[m - 1])) m--;
		ch[++m] = p[i];
	}
}

int N;
P p2[1000];
int ans[1000];
map<P, int> Map;

void solve(){
	scanf("%d", &N);
	for (int i = 0; i < N; i++) ans[i] = 10000;
	for (int i = 0; i < N; i++) scanf("%lf%lf", &p2[i].x, &p2[i].y);
	for (int i = 0; i < (1 << N); i++){
		n = 0;
		Map.clear();
		for (int j = 1, k = 0; j < (1 << N); j <<= 1, k++){
			if ((i & j) > 0){
				p[n] = p2[k];
				Map[p[n++]] = k;
			}
		}
		convex_hull();
		for (int i = 0; i < m; i++){
			ans[Map[ch[i]]] = min(ans[Map[ch[i]]], N - n);
		}
	}
	for (int i = 0; i < n; i++) printf("%d\n", ans[i]);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d:\n", t);
		solve();
	}
	return 0;
}
