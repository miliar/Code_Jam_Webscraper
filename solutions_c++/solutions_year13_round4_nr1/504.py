#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for(int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<

struct S {
	int a,b,c;
	S(int a, int b, int c): a(a), b(b), c(c) {}
	S(){}
} p[1010];

int cap[4040];
int coord[4040];
int t;

typedef long long ll;
#define M 1000002013

int n,m;
ll f(ll x, ll q) {
	//db( (x*n%M + (x-x*x)/2%M)*q%M );
	return (x*n%M + (x-x*x)/2%M)*q%M;
}

int main() {
	int T, caso = 1;
	scanf("%d", &T);
	while( T-- ) {
		t = 0;
		printf("Case #%d: ", caso++);
		scanf("%d%d", &n, &m);
		
		ll res = 0;
		fr(i,0,m) scanf("%d%d%d", &p[i].a, &p[i].b, &p[i].c), res = (res + f(p[i].b-p[i].a, p[i].c))%M;
		fr(i,0,m) coord[t++] = p[i].a, coord[t++] = p[i].b;
		sort(coord,coord+t);
		t = unique(coord,coord+t)-coord;
		fr(i,0,m) {
			int a = p[i].a;
			int b = p[i].b;
			int c = p[i].c;
			a = lower_bound(coord,coord+t,a)-coord;
			b = lower_bound(coord,coord+t,b)-coord;
			fr(j,a,b) cap[j] += c;
		}
		
		fr(i,0,t) {
			while( cap[i] ) {
				int b = i+1, c = cap[i];
				while( cap[b] ) c = min(c,cap[b]), b++;
				res = (res - f(coord[b]-coord[i], c))%M;
				fr(j,i,b) cap[j] -= c;
			}
		}

		printf("%lld\n", (res+M)%M);
		
	}
	return 0;
}
