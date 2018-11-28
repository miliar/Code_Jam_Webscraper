#include <bits/stdc++.h>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define EPS (1e-14)
#define _PA(x,N) rep(i,N){cout<<x[i]<<" ";}cout<<endl;
#define _PA2(x,H,W) rep(i,(H)){rep(j,(W)){cout<<x[i][j]<<" ";}cout<<endl;}

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef complex<double> Complex;
typedef vector< vector<int> > Mat;

int T, N;
PII P[105];
vector<string> ans;

priority_queue<PII> Q;

void solve(int t) {

	ans.clear();

	for (int i = 0; i < N; i++) {
		Q.push(P[i]);
	}


	while (Q.size() > 0) {
#if 0
		priority_queue<PII> X(Q);
		while (X.size() > 0) {
			cout << X.top().first << " " << X.top().second << endl;
			X.pop();
		}
		cout << "---" << endl;
#endif


		PII cur = Q.top(); Q.pop();
		int second = abs(cur.second);
		string tmp = "";

		tmp += second + 'A';
		cur.first -= 1;
		if (cur.first > 0) {
			cur.second = -cur.second;
			Q.push(cur);
		}

		if (Q.size() > 0) {
			cur = Q.top(); Q.pop();
			second = abs(cur.second);
			tmp += second + 'A';
			cur.first -= 1;
			if (cur.first > 0) {
				cur.second = -cur.second;
				Q.push(cur);
			}
		}

		ans.push_back(tmp);
	}

	if (ans[ans.size() - 1].size() == 1 && ans.size() >= 2) {
		swap(ans[ans.size() - 1], ans[ans.size() - 2]);
	}


	printf("Case #%d:", t);
	for (int i = 0; i < ans.size(); i++) {
		printf(" %s", ans[i].c_str());
	}
	printf("\n");
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> N;
		rep(j, N) {
			cin >> P[j].first;
			P[j].second = j;
		}
		solve(i + 1);
	}
	return 0;
}


