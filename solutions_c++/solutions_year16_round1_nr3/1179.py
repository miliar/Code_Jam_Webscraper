#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
using namespace std;

const int INF = 2e9;
const int N = 5555;

int place[N];
bool used[N];
int a[N];
int n;
int ans;

void upd_ans(int w) {
	for (int i = 0; i < w; i++) {
		int nx = (i + 1) % w;
		int ny = ((i - 1) + w) % w;
		if (a[place[i]] != place[nx] && a[place[i]] != place[ny])
			return;
	}
	ans = max(ans, w);
}
void rec(int idx) {
	
	if (idx != 0) {
		upd_ans(idx);
		if (idx == n)
			return;
	}
	for (int i = 0; i < n; i++) {
		if (!used[i]) {
			place[idx] = i;
			used[i] = true;
			rec(idx + 1);
			used[i] = false;
		}
	}
}

int main() {
#if _DEBUG
	freopen("C-sma.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	freopen("C-sma.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout.sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++){
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			a[i]--;
		}
		ans = 0;
		rec(0);
		cout << "Case #" << tt + 1 << ": " << ans << endl;
	}
}