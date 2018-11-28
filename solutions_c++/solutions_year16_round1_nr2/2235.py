#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <time.h>
#include <map>
using namespace std;

const int INF = 2e9;
const int N = 50;

int place[N];
bool used[N];
vector<int> a[N];
int n;
int ans;
int b[N][N];
bool nused[N];

bool can(int x, int y) {
	for (int i = 0; i < n; i++) {
		if (a[x][i] >= a[y][i])
			return false;
	}
	return true;
}
bool eq(vector<int> b1, vector<int> b2) {

	for (int i = 0; i < b1.size(); i++) {
		if (b1[i] != b2[i])
			return false;
	}

	return true;
}

bool eq2(vector<int> b1, vector<int> b2, int w) {

	for (int i = 0; i < w; i++) {
		if (b1[i] != b2[i])
			return false;
	}

	return true;
}
int z[N];
int calc(int i) {
	if (z[i] != -1) {
		return z[i];
	}
	z[i] = 1;
	for (int j = 0; j < 2 * n - 1; j++) {
		if (b[i][j]) {
			z[i] = max(z[i], 1 + calc(j));
		}
	}
	return z[i];
}

bool numi(int w) {
	int cnt = 0;
	int ku = 0;
	for (int i = 0; i < N; i++) {
		nused[i] = used[i];
		ku += nused[i];
	}
	assert(ku == n);
	for (int j = 0; j < n; j++) {
		vector<int> e;
		for (int i = 0; i < w; i++) {
			e.push_back(a[place[i]][j]);
		}
		bool ok = false;
		for (int k = 0; k < 2 * n - 1; k++) {
			if (!nused[k] && eq2(a[k], e, w)) {
				nused[k] = true;
				ok = true;
				break;
			}
		}

		if (!ok) {
			if (cnt > 0) {
				return false;
			}
			cnt++;
		}
	}
	return true;
}

vector<int> check() {
	vector<int> ans;
	int cnt = 0;

	/*
	cout << "Check " << endl;
	for (int i = 0; i < n; i++) {
		assert(i == 0 || b[place[i - 1]][place[i]]);
		for (int j = 0; j < n; j++) {
			cout << a[place[i]][j] << " ";
		}
		cout << endl;
	}
	cout << endl;*/

	int ku = 0;
	for (int i = 0; i < N; i++) {
		nused[i] = used[i];
		ku += nused[i];
	}
	assert(ku == n);
	//cerr << "check " << endl;

	for (int j = 0; j < n; j++) {
		vector<int> e;
		for (int i = 0; i < n; i++) {
			e.push_back(a[place[i]][j]);
		}
		int plc = 0;
		bool ok = false;
		for (int k = 0; k < 2 * n - 1; k++) {
			if (!nused[k] && eq(a[k], e)) {
				nused[k] = true;
				ok = true;
				plc = k;
				break;
			}
		}

		if (!ok) {
			if (cnt > 0) {
				return vector<int>();
			}
			cnt++;
			ans = e;
		}
	}

	return ans;
}
vector<int> ANS;
void rec(int idx) {
	if (ANS.size() > 0) {
		return;
	}
	if (!numi(idx)) {
		return;
	}
	if (idx == n) {
		vector<int> ans = check();
		if (ans.size() > 0)
			ANS = ans;
		return;
	}
	for (int i = 0; i < 2 * n - 1; i++) {
		if (!used[i] && (idx == 0 || b[place[idx - 1]][i])) {

			if (idx + calc(i) < n)
				continue;
			place[idx] = i;
			assert(idx == 0 || b[place[idx - 1]][place[idx]]);
			used[i] = true;
			rec(idx + 1);
			used[i] = false;
		}
	}
}
int main() {
	srand(time(NULL));
#if _DEBUG
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif 

	freopen("Bsmall.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout.sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++){
		cin >> n;

		cerr << "START " << tt << " n = " << n << endl;

		for (int i = 0; i < N; i++) {
			z[i] = -1;
		}
		for (int i = 0; i < N; i++) {
			used[i] = false;
			place[i] = 0;
		}
		for (int i = 0; i < 2 * n - 1; i++) {
			a[i] = vector<int>(n);
			for (int j = 0; j < n; j++) {
				cin >> a[i][j];
			}
		}
		random_shuffle(a, a + 2 * n - 1);

		for (int i = 0; i < 2 * n - 1; i++) {
			for (int j = i + 1; j < 2 * n - 1; j++) {
				if (can(i, j))
					b[i][j] = true;
				if (can(j, i))
					b[j][i] = true;
			}
		}

		rec(0);


		cout << "Case #" << tt + 1 << ": ";
		if (ANS.size() > 0) {
			for (int j = 0; j < n; j++)
				cout << ANS[j] << " ";
			cout << endl;
		}
		else {
			cout << "No solution" << endl;
		}

		ANS.clear();
	}
}