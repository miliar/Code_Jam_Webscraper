#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<cstring>
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

map<string, int> words;

int q[5555][5555], nn[5555][5555];
char a[1000111];
int f[5555];

vector<int> v[5555];

int st;

void ae(int x, int y, int fl) {
	if (nn[x][y] == 0) {
		v[x].pb(y);
		v[y].pb(x);
		nn[x][y] = nn[y][x] = 1;
	}
	q[x][y] += fl;
}

void go(int x) {
	if (f[1] != -1) return;
	for (int i = 0; i < v[x].size(); i++) if (q[x][v[x][i]] > 0 && f[v[x][i]] == -1) {
		f[v[x][i]] = x;
		go(v[x][i]);
	}
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	scanf("%d\n", &T);
	for (int tt = 1; tt <= T; tt++) {
		int n;
		scanf("%d\n", &n);
		words.clear();

		st = n;

		for (int i = 0; i < n; i++) {
			gets(a);

			vector<string> e;
			string t = "";

			int k = strlen(a);

			for (int j = 0; j < k; j++) {
				if ('a' <= a[j]	&& a[j] <= 'z') {
					t += a[j];
				} else {
					if (t.size() > 0) {
						e.pb(t);
						t = "";
					}
				}
			}
			if (t.size() > 0) e.pb(t);

			for (int j = 0; j < e.size(); j++) {
				int id = -1;
				if (words.find(e[j]) == words.end()) {
					words[e[j]] = st;
					id = st;

					ae(id, id + 1, 1);
					st += 2;
				} else {
					id = words[e[j]];
				}

				ae(i, id, 1e9);
				ae(id + 1, i, 1e9);
			}

		}
		int ans = 0;
		for(;;) {
			for (int i = 0; i < st; i++) f[i] = -1;
			f[0] = 0;
			go(0);
			if (f[1] == -1) break;
			ans++;
			int x = 1;
			while (x != 0) {
				q[x][f[x]]++;
				q[f[x]][x]--;
				x = f[x];
			}
		}
		for (int i = 0; i < st; i++) for (int j = 0; j < st; j++) q[i][j] = nn[i][j] = 0;
		for (int i = 0; i < st; i++) v[i].clear();

		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}