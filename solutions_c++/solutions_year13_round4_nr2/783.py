#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <utility>
#include <cmath>
#include <set>
#include <queue>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define mp make_pair
#define pb push_back
#define rep(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define repr(i, l, r) for(int (i) = (l); (i) < (r); ++(i))
#define clr(t, v) memset((t), (v), sizeof(t))
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define fi first
#define se second

#define DEBUG


int T, N, P;

bool must_win(int i) {
	int cur = 0;
	int higher = i;
	rep(j, N) {
		if (higher >= 1) {
			cur += 1 << (N-j-1);
			higher = (higher-1)/2;
		}
	}
	if (cur < P)
		return true;
	return false;
}
bool can_win(int i) {
	int cur_place = 0;
	int lower = (1<<N) - i - 1;
	rep(j, N) {
		if (lower >= 1) {
			lower = (lower-1)/2;
		} else {
			cur_place += 1 << (N-j-1);
		}
	}
	if (cur_place < P)
		return true;
	return false;
}

int main() {
#ifdef DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	scanf("%d", &T);

	rep(asdf, T) {
		scanf("%d%d", &N, &P);
		int guaranteed = 0;
		int could_win = 0;
		rep(i, 1 << N) {
			if (must_win(i)) guaranteed = i;
			if (can_win(i)) could_win = i;
		}
		printf("Case #%d: %d %d\n", asdf+1, guaranteed, could_win);
	}

	return 0;
}