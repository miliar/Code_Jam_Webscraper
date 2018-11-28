#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int n, p, r, s;
const int g[] = {2, 0, 1};

vector<int> try_fill(int start, int n)
{
	vector<int> res(1 << n);
	if (n == 0) {
		res[0] = start;
		return res;
	}
	vector<int> tmpres0 = try_fill(start, n - 1);
	vector<int> tmpres1 = try_fill(g[start], n - 1);
	if (tmpres0 < tmpres1) {
		res = tmpres0;
		res.insert(res.end(), tmpres1.begin(), tmpres1.end());
	} else {
		res = tmpres1;
		res.insert(res.end(), tmpres0.begin(), tmpres0.end());
	}
	return res;
}

void print(vector<int> &res)
{
	if (res[0] > 2) {
		printf("IMPOSSIBLE\n");
		return;
	}
	for (int i = 0; i < (1 << n); ++i) {
		printf("%c", "PRS"[res[i]]);
	}
	printf("\n");
}

void solve()
{
	cin >> n >> r >> p >> s;
	vector<int> v[3];
	for (int i = 0; i < 3; ++i) {
		v[i] = try_fill(i, n);
		int t[3];
		t[0] = t[1] = t[2] = 0;
		for (int j = 0; j < (1 << n); ++j) {
			t[v[i][j]]++;
		}
		if (t[0] != p || t[1] != r || t[2] != s) {
			v[i][0] = 3;
		}
	}
	if (v[0] <= v[1] && v[0] <= v[2]) {
		print(v[0]);
	} else if (v[1] <= v[0] && v[1] <= v[2]) {
		print(v[1]);
	} else {
		print(v[2]);
	}
}

int main()
{
	int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}
