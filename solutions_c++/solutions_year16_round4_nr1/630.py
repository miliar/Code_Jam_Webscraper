#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define FORR(i,b) FOR(i, 0, b)
#define sz(e) (int)e.size()
#define CLR(x,v) memset (x, v, sizeof x)
#define pb push_back
#define all(e) e.begin(), e.end()

typedef long long ll;
typedef pair<int, int> ii;

const int MAXN = 100005;
const int INF = 1000000000;

int n;
int v[MAXN]; 
void build (int pos, int x, int l) {
	v[pos] = x;
	//cout << "-> " << pos << " " << x << endl;
	if (l>=n) {
		return;
	} else {
		build (2*pos, x, l+1);
		build (2*pos+1, (x+1) % 3, l+1);
	}
}

string mysort (string s) {
	int t = sz(s)/2;
	if (t==0) return s;
	string s1 = s.substr (0, t), s2 = s.substr(t, t);
	string ans1 = mysort (s1), ans2 = mysort (s2);
	if (ans1.compare (ans2)<0) {
		ans1 += ans2;
		return ans1;
	} else {
		ans2 += ans1;
		return ans2;
	}
}

int main () {
	int T;
	cin>>T;
	FORR (c, T) {
		cout << "Case #" << c+1 << ": ";
		int Q[3];
		cin>>n>>Q[2]>>Q[1]>>Q[0];
		build (1, 0, 0);
		bool valid = false;
		int N = 1<<n;
		FORR (i, 3) {
			int W[3]; CLR (W, 0);
			FOR (j, N, 2*N) W[v[j]]++;
			//cout << W[0] << " " << W[1]  << " " << W[2] << endl;
			bool ok = true;
			FORR (j, 3) if (W[j]>Q[j]) ok = false;
			if (ok) {
				valid = true;
				break;
			}
			FOR (j, N, 2*N) v[j] = (v[j]+1)%3;
		}
		if (valid) {
			string res = "";
			FOR (i, N, 2*N) {
				if (v[i]==0) {
					res += 'S';
				} else if (v[i]==1) {
					res += 'P';
				} else {
					res += 'R';
				}
			}
			cout << mysort(res) << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
