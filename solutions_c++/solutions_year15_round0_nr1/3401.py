#include<ctime>
#include<cassert>
#include<stdio.h>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<memory.h>
#include<unordered_map>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
typedef pair<int, int> pii;

const int inf = 1e9+7;
const ld eps = 1e-16;
const int maxn = 3500;

int main(){
#ifdef TANAS_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int n;
		string s;
		cin >> n >> s;
		int invite = 0, total = 0;
		for (int i = 0; i <= n; ++i) {
			int d = s[i] - '0';
			if (d == 0) continue;
			if (total < i) {
				int add = i - total;
				invite += add;
				total += add;
			}
			total += d;
		}
		printf("Case #%d: %d\n", t + 1, invite);
	}

	return 0;
}

