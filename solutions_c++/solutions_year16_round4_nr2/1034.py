#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define endl '\n'

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

vector<long double> prob;
int n,k;
vi idx;

long double memo[20][40];
int vis[20][40];

long double pd(int cur, int delta) {
	int memodelta = delta + 20;
	if(cur == idx.size() and delta == 0) {
		return 1.0;
	}else if(cur == idx.size() and delta) {
		return 0.0;
	}else if(vis[cur][memodelta]) {
		return memo[cur][memodelta];
	}else {
		long double ans = prob[idx[cur]] * pd(cur + 1, delta + 1) + (1.0 - prob[idx[cur]]) * pd(cur + 1, delta - 1);
		vis[cur][memodelta] = 1;
		return memo[cur][memodelta] = ans;
	}
}


int main() {
	ios_base::sync_with_stdio(0);
	cout << fixed << setprecision(7);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		memset(vis, 0, sizeof vis);
		prob.clear();

		cout << "Case #" << t <<": ";
		cin >> n >> k;			
		for(int i = 0; i < n; i++){
			long double aux;
			cin >> aux;
			prob.pb(aux);
		}

		int half = k/2;
	
		long double mx = 0.0;
		for(int i = 0; i < (1 << n); i++){
			idx.clear();
			int cur = i;
			for(int j = 0; j < n; j++){
				if((cur >> j)&1) idx.pb(j);
			}

			if(idx.size() == k) {
				memset(vis, 0, sizeof vis);
				mx = max(mx, pd(0, 0));
			}
		}
		cout << mx << endl;

	}

	return 0;
}
