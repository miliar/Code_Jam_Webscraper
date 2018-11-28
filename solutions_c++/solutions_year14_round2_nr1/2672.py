#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <climits>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

int avg(int sum, int k) {
	int a = sum / k;
	if( 2*sum / k == 2*a ) return a;
	else return a + 1;
}

int parse(int *v, char *p, char *s, int slen) {
	int c = 0, sss = 1;
	FOR(i,0,slen) {
		if(s[i] == s[i+1]) {
			++sss;
			continue;
		}
		v[c] = sss;
		p[c++] = s[i];
		sss = 1;
	}
	return c;
}

bool check(int *v, char *p, int plen, char *s, int slen) {
	char T[111];
	int tlen = parse(v, T, s, slen);
	if(plen != tlen) return false;
	FOR(i,0,plen) {
		if(T[i] != p[i]) return false;
	}
	return true;
}

void testcase(int zzz) {
	char P[111], A[111];
	int V[111], SV[111];
	int M[111][111];
	int n, pl, al;
	scanf("%d", &n);
	scanf("%s", A);
	al = strlen(A);
	pl = parse(SV, P, A, al);
	FOR(i,0,pl) M[0][i] = SV[i];
	bool flag = true;
	FOR(i,1,n) {
		scanf("%s", A);
		al = strlen(A);
		if(!check(V, P, pl, A, al)) {
			flag = false;
			continue;
		}
		FOR(j,0,pl) SV[j] += V[j];
		FOR(j,0,pl) M[i][j] = V[j];
	}
	if(!flag) {
		printf("Case #%d: Fegla Won\n", zzz);
		return;
	}
	int res = 0;
	FOR(i,0,pl) {
		int d = avg(SV[i], n);
		FOR(j,0,n) res += abs(d - M[j][i]);//, printf("%d ", M[j][i]);
		//printf("\n");
	}
	printf("Case #%d: %d\n", zzz, res);
}

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) testcase(zzz + 1);
	return 0;
}
