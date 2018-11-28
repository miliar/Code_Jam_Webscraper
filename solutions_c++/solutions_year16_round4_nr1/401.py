#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define all(v) (v).begin(),(v).end()

#define PII pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define pb push_back
#define lint long long int
#define VI vector<int>

#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debug2(x,y) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y <<endl; } 
#define debug3(x,y,z) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y << ", " << #z << " = " << z <<endl; } 
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define debugt(t,n) {{cerr <<#t <<" = "; FOR(it,0,(n)) cerr <<t[it] <<", "; cerr <<endl; }}

#define make( x) int (x); scanf("%d",&(x));
#define make2( x, y) int (x), (y); scanf("%d%d",&(x),&(y));
#define make3(x, y, z) int (x), (y), (z); scanf("%d%d%d",&(x),&(y),&(z));
#define make4(x, y, z, t) int (x), (y), (z), (t); scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define makev(v,n) VI (v); FOR(i,0,(n)) { make(a); (v).pb(a);} 
#define IOS ios_base::sync_with_stdio(0)
#define HEAP priority_queue

#define read( x) scanf("%d",&(x));
#define read2( x, y) scanf("%d%d",&(x),&(y));
#define read3(x, y, z) scanf("%d%d%d",&(x),&(y),&(z));
#define read4(x, y, z, t) scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define readv(v,n) FOR(i,0,(n)) { make(a); (v).pb(a);}


using namespace std;
const int max_n = 1e5+5;

char ans[8000];

string rob(int a, int b, int c) {
	if (a+b+c==1) {
		if (a==1) return "1";
		if (b==1) return "2";
		if (c==1) return "3";
	} 
	if (a+b+c==2) {
		if (c==0) return "12";
		if (b==0) return "13";
		if (a==0) return "23";
	}
	int aa = (a - (a+b+c)/4);
	int bb = (b - (a+b+c)/4);
	int cc = (c - (a+b+c)/4);
	string hh = rob(aa, bb, cc);
	string ans = "";
	FOR(j,0,hh.length()) {
		if (hh[j]=='1') ans += "1213";
		if (hh[j]=='2') ans += "1223";
		if (hh[j]=='3') ans += "1323";
	}
	return ans;
}


void solve() {
	make(n);
	make3(r, p, s);
	int m = (1<<n);
	int cp = p, cr = r, cs = s;
	while (m%4==0) {
		if (p < 0 || r < 0 || s < 0 || p+r<s || p+s<r || r+s<p) {
			printf("IMPOSSIBLE\n");
			return;
		}
		int a = (p - (p+r+s)/4);
		int b = (r - (p+r+s)/4);
		int c = (s - (p+r+s)/4);
		p = a;
		r = b;
		s = c;
		if (p < 0 || r < 0 || s < 0) {
			printf("IMPOSSIBLE\n");
			return;
		}
		m = m/4;
	}
	if (m==2) {
		if (p==2 || r==2 || s==2) {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	string ans = rob(cp, cr, cs);
	FOR(i,0,cp+cr+cs) {
		if (ans[i]=='1') putchar('P');
		if (ans[i]=='2') putchar('R');
		if (ans[i]=='3') putchar('S');
	}
	printf("\n");
}


int main() {
	make(tt);
	FOR(test,1,tt+1) {
		printf("Case #%d: ",test);
		solve();
	}
}

	
