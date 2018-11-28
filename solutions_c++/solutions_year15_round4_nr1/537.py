#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

#define N 1009

int m, n,dang[N][N];
char grid[N][N];

int process() {
	int ans = 0;
	
	rp(i, m) {
		int j = 0;
		while (j < n && grid[i][j] == '.') j++;
		if (j < n) {
			dang[i][j]++;
			if (dang[i][j] == 4) return -1;
			if (grid[i][j] == '<') ans++;
		}
		
		j = n-1;
		while (j >= 0 && grid[i][j] == '.') j--;
		if (j >= 0) {
			dang[i][j]++;
			if (dang[i][j] == 4) return -1;
			if (grid[i][j] == '>') ans++;
		}
	}
	
	
	rp(i, n) {
		int j = 0;
		while (j < m && grid[j][i] == '.') j++;
		if (j < m) {
			dang[j][i]++;
			if (dang[j][i] == 4) return -1;
			if (grid[j][i] == '^') ans++;
		}
		
		j = m-1;
		while (j >= 0 && grid[j][i] == '.') j--;
		if (j >= 0) {
			dang[j][i]++;
			if (dang[j][i] == 4) return -1;
			if (grid[j][i] == 'v') ans++;
		}
	}
	
	return ans;
}

int main() {
	int t, cn = 1;
	sc(t); while (t--) {
		printf("Case #%d: ", cn++);
		sc2(m, n);
		rp(i, m) scs(grid[i]);
		cl(dang, 0);
		int ans = process();
		if (ans == -1) puts("IMPOSSIBLE");
		else pri(ans);
	}
	return 0;
}
























