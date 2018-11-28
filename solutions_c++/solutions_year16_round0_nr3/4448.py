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

int f[N];
int p[N];
int k;

int n, J;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	for (int i = 2; i <= 1e5; i++) if (!f[i]) {
		p[k++] = i;
		int j = i + i;
		while (j <= 1e5) {
			f[i] = 1;
			j += i;
		}

	}

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> J;

		vector<string> s;
		vector<vector<int> > d;

		set<string> was;

		while (s.size() < J) {
			string t = "";
			for (int i = 0; i < n; i++) t.pb(rand() % 2 + '0');
			t[0] = '1';
			t.back() = '1';

			if (was.count(t)) continue;
			was.insert(t);

			vector<int> r;

			for (int y = 2; y <= 10; y++) {
				long long e = 0;
				for (int i = 0; i < n; i++) e = e * y + t[i] - '0';

				int h = -1;
				for (int j = 0; j < k; j++) if (p[j] < e && e % p[j] == 0) {
					h = p[j];
					break;
				}
				if (h == -1) break;
				r.pb(h);
			}
			if (r.size() < 9) continue;
			s.pb(t);
			d.pb(r);
			cerr << s.size() << endl;
		}


		cout << "Case #" << tt << ": " << endl;
		for (int i = 0; i < J; i++) {
			cout << s[i];
			for (int j = 0; j < 9; j++) cout << " " << d[i][j];
			cout << endl;
		}		

	}
	return 0;
}