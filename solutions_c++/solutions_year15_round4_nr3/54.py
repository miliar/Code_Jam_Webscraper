#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007

long long getLL() {
	long long ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

int getInt() {
	int ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

struct Tflow {
	int v[MaxN],next[MaxN],h[MaxN],tot,c[MaxN];
	void clear() { Fill(h,tot = 0); }
	void add(int b,int e,int f) { //cerr << b << ' ' << e << ' ' << f << endl;
		v[++tot] = e; next[tot] = h[b]; h[b] = tot; c[tot] = f;
		v[++tot] = b; next[tot] = h[e]; h[e] = tot; c[tot] = 0;
	}
	int S,T,d[MaxN],flow,found,gap[MaxN],cur[MaxN];
	long long ans = 0;
	void aug(int i) {
		if (i == T) {
			ans += flow; found = true;
			return ;
		}
		int mind = T, tf = flow, z;
		for (z = cur[i]; z; z = next[z]) if (c[z]) {
			if (d[v[z]] + 1 == d[i]) {
				flow = min(flow,c[z]); cur[i] = z;
				aug(v[z]);
				if (found) break ; if (d[S] >= T) return ;
				flow = tf; 
			} mind = min(mind,d[v[z]]);
		}
		if (found) {
			c[z] -= flow; c[(z & 1) ? (z + 1) : (z - 1)] += flow;
		} else {
			if (--gap[d[i]] == 0) d[S] = T;
			for (int z = h[i]; z; z = next[z]) if (c[z]) mind = min(mind,d[v[z]]);
			++gap[d[i] = mind + 1]; cur[i] = h[i];
		}
	}
	void isap() {
		ans = 0; Fill(d,0); Fill(gap,0); gap[0] = T; For(i,1,T) cur[i] = h[i];
		while (d[S] < T) {
			flow = INF; found = false ;
			aug(S);
		}
	}
	int Sol(int _s,int _t) {
		S = _s; T = _t;
		isap();
		return ans;
	}
} TF;

int n;
map<string, int> Map;
int have[233][4333];
char buf[MaxN], tbuf[MaxN];

int main() {
	//freopen("C-small-attempt0.in","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n;
		Map.clear();
		gets(buf);
		Fill(have, 0);
		For(i,1,n) {
			gets(buf);
			int len = strlen(buf);
			int cur = 0;
			while (cur < len) {
				sscanf(buf + cur, "%s", tbuf);
				string s = tbuf;
				cur += s.length();
				while (buf[cur] == ' ' && cur < len) ++cur;
				if (!Map.count(s)) {
					Map[s] = Map.size();
				}
				have[i][Map[s]] = true;
			}
		}
		int m = Map.size();
		cerr << m << endl;
		TF.clear();
		int S = n + n + m + m + 1, T = S + 1;
		int BIG = 1000000;
		For(i,1,n) {
			if (i != 1) TF.add(S, i, BIG);
			if (i != 2) TF.add(i + n, T, BIG);
		}
		For(i,1,n) TF.add(i, i + n, BIG);
		For(i,1,m) TF.add(n + n + i, n + n + m + i, 1);
		For(i,1,n) For(j,1,m) if (have[i][j]) TF.add(i, n + n + j, INF), TF.add(n + n + m + j, i + n, INF);
		int ans = TF.Sol(S, T);
		cout << ans % BIG << endl;
	}
	return 0;
}

