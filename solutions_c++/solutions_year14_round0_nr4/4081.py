#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define oo 1LL<<30
#define SZ(x) ((int)x.size())
#define valid(x,u) (x>=0 && x<u)

int di [] = {0, 0, 1, -1, 1, 1, -1, -1};
int dj [] = {1, -1, 0, 0, 1, -1, 1, -1};

vector <int> A; // naomi
vector <int> B; // ken

int war() {
	int ret = 0;
	set <int> SB(B.begin(), B.end());
	for(int i=0; i<SZ(A); i++) {
		__typeof(SB.begin()) it = SB.upper_bound(A[i]);
		if(it == SB.end()) {
			ret ++;
			SB.erase(SB.begin());
		} else {
			SB.erase(*it);
		}
	}
	return ret;
}

int cheatingStrategy() {
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	for(int k=0; k<SZ(A); k++) {
		bool good = true; int j = 0;
		for(int i=k; i<SZ(A); i++) {
			if(A[i] < B[j]) {
				good = false;
				break;
			}
			j ++;
		}
		if(good) return SZ(A) - k;
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout << fixed << setprecision(9);

	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);

	double tmp;
	int t, id = 0;
	cin >> t;

	while(t --) {
		int n; cin >> n;
		A.clear(); B.clear();
		for(int i=0; i<n; i++) {
			cin >> tmp;
			A.push_back(tmp * 100000);
		}
		for(int i=0; i<n; i++) {
			cin >> tmp;
			B.push_back(tmp * 100000);
		}
		cout << "Case #" << ++id << ": " << cheatingStrategy() << " " << war() << endl;
	}

	return 0;
}
