#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FAIL { puts("NO"); continue; }
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define NX(x) (1 + (x % 3))
#define LL long long
#define N 200000
LL n, m;
char s[N];
int  f[300];
struct P{
	int s, v;
	P(int a, int b):s(a), v(b){}
	P(){}
	P operator *(P p){
		P ret = P(s,v);
		ret.s ^= p.s;
		if (ret.v && p.v && NX(ret.v) != p.v) ret.s ^= 1;
		ret.v ^= p.v;
		return ret;
	}
	P operator =(P p){
		s = p.s;
		v = p.v;
		return P(s,v);
	}
	P operator ^(int pow){
		P ret = P(0,0), tmp = *this;
		FOR(i,0,pow) ret = ret * *this;
		/*
		FOR(i,0,30){
			if (pow & (1 << i)) ret = ret * tmp;
			tmp = tmp * tmp;
		}
		*/
		return ret;
	}
	bool operator ==(P p) { return s == p.s && v == p.v; }
	bool operator !=(P p) { return s != p.s || v != p.v; }
	void prt(){printf("%d %d\n", s, v);}
}tot, I = P(0,1), J = P(0,2), K = P(0,3), ONE = P(0,0), S[N];

int main(){
	f['1'] = 0;
	f['i'] = 1;
	f['j'] = 2;
	f['k'] = 3;
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		tot = P(0,0);
		printf("Case #%d: ", cc);
		scanf("%lld%lld%s", &n, &m, s);
		FOR(i,0,n) s[i] = f[s[i]];
		FOR(i,0,n) S[i] = P(0, s[i]);
		FOR(i,0,n) tot = tot * S[i];

		int pre, suf;

		P tmp = ONE;
		for (pre = 0; pre < n * m && pre < 10 * N; pre++){
			if (tmp == I) break;
			tmp = tmp * S[pre % n];
		}
		if (tmp != I) FAIL;

		tmp = ONE;
		for (suf = 0; suf < n * m && suf < 10 * N; suf++){
			if (tmp == K) break;
			tmp = S[(n + (n - 1 - suf) % n) % n] * tmp;
		}
		if (tmp != K) FAIL;
		if (pre + suf >= n * m) FAIL;
		tot = tot ^ m;
		if (!tot.s || tot.v) FAIL;

		int t1 = pre / n, t2 = m - suf / n - !!(suf % n);

		tmp = ONE;

		if (t1 == t2){
			pre %= n;
			suf %= n;
			for (int i = pre; i + suf < n; i++) tmp = tmp * S[i];
		}
		else{
			tot = ONE;
			FOR(i,0,n) tot = tot * S[i];
			for (int i = pre % n; i < n; i++) tmp = tmp * S[i];
			if (t2 - 1 > t1) tmp = tmp * (tot^(t2 - t1 - 1));
			suf %= n;
			if (suf)
				for (int i = 0; i + suf < n; i++) tmp = tmp * S[i];
		}
		if (tmp != J) FAIL;
		puts("YES");
	}
	return 0;
}

