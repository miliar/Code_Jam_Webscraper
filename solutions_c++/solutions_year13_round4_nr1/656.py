#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stack>
#include <functional>

using namespace std;

typedef pair<int,int> par;
typedef long long int llint;
const llint MOD = 1000002013;
const int MAXM = 1002;
stack<par> S; // lok ulaza, br. ljudi
int n, m;

struct bla {
	int l; // lokacija
	int p; // ljudi
	int t; // tip - 0 ulaz, 1 izlaz
} B[2*MAXM];

inline llint rac(llint a, llint b)
{
	return ((b-a)*(2*n-b+a+1))/2;
}

inline bool cmp(const bla& A, const bla& B)
{
	if (A.l != B.l)
		return A.l < B.l;
	
	return A.t < B.t;
}

void doet()
{
	while (!S.empty()) S.pop();
	llint orig = 0;
	llint sol = 0;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++) {
		int o, e, p;
		scanf("%d%d%d", &o, &e, &p);
		B[2*i].l = o;
		B[2*i].p = p;
		B[2*i].t = 0;
		B[2*i+1].l = e;
		B[2*i+1].p = p;
		B[2*i+1].t = 1;
		orig = (orig + (rac(o,e) % MOD)*p) % MOD;
	}
	sort(B, B+2*m, cmp);
	par p;
	for (int i = 0; i < 2*m; i++) {
		if (B[i].t == 0) {
			S.push( par(B[i].l, B[i].p) );
		}
		else {
			while (B[i].p > 0) {
				p = S.top(); S.pop();
				int t = min(B[i].p, p.second);
				sol = (sol + (rac(p.first, B[i].l) % MOD)*t) % MOD;
				B[i].p -= t;
				p.second -= t;
				if (p.second > 0)
					S.push(p);
			}
		}
	}
	printf("%lld\n", (orig-sol+MOD)%MOD);
}


int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		doet();
	}
	return 0;
}

