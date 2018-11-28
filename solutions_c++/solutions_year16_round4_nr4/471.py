#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

void solve(int);

int main () {

	ios::sync_with_stdio(false);
	
	int test_num;
	cin >> test_num;
	for (int case_id = 1;case_id <= test_num;case_id++) {
		solve(case_id);
	}

	return 0;
}

const int N = 30;

int data[N][N];
string str[N];
int n;

int pass1[N], pass2[N];

typedef pair<int, int> pii;

pii dfs2(int);

pii dfs1(int u) {
	if(pass1[u]) return {0, 0};
	int cnt1 = 1, cnt2 = 0;
	pass1[u] = 1;
	for(int i = 0;i < n;i++) {
		if(data[u][i] and !pass2[i]) {
			pii r = dfs2(i);
			cnt1 += r.first;
			cnt2 += r.second;
		}
	}
	return {cnt1, cnt2};
}
pii dfs2(int u) {
	if(pass2[u]) return {0, 0};
	int cnt1 = 0, cnt2 = 1;
	pass2[u] = 1;
	for(int i = 0;i < n;i++) {
		if(data[i][u] and !pass1[i]) {
			pii r = dfs1(i);
			cnt1 += r.first;
			cnt2 += r.second;
		}
	}
	return {cnt1, cnt2};
}
int check(void) {
	for(int i = 0;i < n;i++) {
		pass1[i] = pass2[i] = 0;
	}
	int ans = 0;
	for(int i = 0;i < n;i++) {
		if(not pass1[i]) {
			pii r = dfs1(i);
			if(r.first != r.second) return -1;
			ans += r.first * r.second;
		}
		if(not pass2[i]) {
			pii r = dfs2(i);
			if(r.first != r.second) return -1;
			ans += r.first * r.second;
		}
	}
	return ans;
}
void solve ( int case_id ) {

	int num_edge = 0;

	cin >> n;
	for(int i = 0;i < n;i++) {
		cin >> str[i];
		for(int j = 0;j < n;j++) {
			num_edge += str[i][j]-'0';
		}
	}

	int ans = n*n;
	for(int i = 0;i < (1 << (n*n));i++) {

		bool err = false;
		int cnt = 0;
		for(int j = 0;j < n*n;j++) {
			int x = j / n, y = j % n;
			data[x][y] = str[x][y] - '0';
			if ( (i >> j) & 1 ) {
				if ( data[x][y] == 1) err = true;
				data[x][y] = 1;
				cnt++;
			}
		}

		if (err) continue;
		int r = check();
		if ( r != -1 ) {
			ans = min(ans, r - num_edge);
		}
	}

	cout << "Case #" << case_id << ": " << ans << endl;
}