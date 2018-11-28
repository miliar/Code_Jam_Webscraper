#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define LD long double
#define pb push_back
#define x first
#define y second
#define PII pair<int,int>
#define PLI pair<LL,int>
#define PIL pair<int,LL>
#define PLL pair<LL,LL>
#define PDD pair<LD,LD>
#define eps 1e-9
#define HH1 402653189
#define HH2 1610612741

int TC;
FILE *OUT;

char s[1055];
int n, k, ans;

void init() {
	ans = 0;
}

void solve() {
	scanf("%s%d", s, &k);
	n = strlen(s);
	
	FOE(i, 0, n - k) {
		if (s[i] == '-') {
			FOR(j, 0, k) s[i + j] = (s[i + j] == '+') ? '-' : '+';
			ans++;
		}
	}
	
	FOR(i, 0, n) if (s[i] == '-') {
		fprintf(OUT, "IMPOSSIBLE");
		return;
	}
	
	fprintf(OUT, "%d", ans);
}

int main () {
	
	scanf("%d", &TC);
	
	OUT = fopen("a.out", "w");
	
	FOE(ttc, 1, TC) {
		
		printf("Processing on Case #%d...\n", ttc);
		
		init();
		
		fprintf(OUT, "Case #%d: ", ttc);
		
		solve();
		
		fprintf(OUT, "\n");
		
	}
	
	return 0;
	
}
