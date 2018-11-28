#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int n;
string s[55], e[55];

int f[55], q[55];

int rec(int x, int m1, int m2) {
	if (f[x]) return 0;
	f[x] = 1;
	for (int i = 0; i < n; i++) if (m2 & pw(i)) {
		if (e[x][i] == '0') continue;
		if (q[i] == -1 || rec(q[i], m1, m2)) {
			q[i] = x;
			return 1;
		}
	}
	return 0;

}

int haveb(int m1, int m2) {
	for (int i = 0; i < n; i++) q[i] = -1;
	for (int i = 0; i < n; i++) if (m1 & pw(i)) {
		for (int j = 0; j < n; j++) f[j] = 0;
		if (!rec(i, m1, m2)) return 0;
	}
	return 1;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cout << "Case #" << tt << ": ";
		cin >> n;
		for (int i = 0; i < n; i++) cin >> s[i];

		int ans = 1e9 + 1;
		for (int o = 0; o < pw(n * n); o++) {
			int bad = 0;
			int cc = 0;
			for (int i = 0; i< n; i++) e[i] = s[i];
			for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (o & pw(i * n + j)) {
				if (e[i][j] == '1') bad = 1; else {
					cc++;
					e[i][j] = '1';
				}
                        }
                        if (cc >= ans) continue;
                        if (bad) continue;

                        for (int z = 0; z < n; z++) {
                        	if (!bad)for (int o = 0; o < pw(n); o++) if (__builtin_popcount(o) == z)
                        	if (!bad)for (int oo = 0; oo < pw(n); oo++) if (__builtin_popcount(oo) == z) {
                        		if (haveb(o, oo) && !haveb((pw(n) - 1) ^ o, (pw(n) - 1) ^ oo)) bad = 1;
                        	}

                        }
                        if (bad) continue;
                        ans = min(ans, cc);
		}
		cout << ans << endl;

	}
	return 0;
}