#include <bits/stdc++.h>
using namespace std;
#define nl '\n'
#define MAXN 50005
#define INF 1000000000
typedef long long ll;
typedef pair<int, int> pii;

ifstream fin ("a-big.in");
ofstream fout ("a.out");

int t;

int main() {

	fin>>t;

	for (int k = 0; k < t; k++) {
		int n; fin>>n;
		vector<int> cur;
		for (int j = 0; j <= n; j++) {
			char c; fin>>c;
			cur.push_back((int)c - 48);
		}

		ll tot = 0, res = 0;
		for (int i = 0; i < cur.size(); i++) {
			if (tot < i) {
				res += (i - tot);
				tot = i;
			}
			tot += cur[i];
		}

		fout<<"Case #"<<k + 1<<": "<<res<<nl;
	}
}