#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#define TOTAL_LENGTH 1000010
using namespace std;

int n, best;
string s[100];
bool done_col[100];

bool check()
{
	for (int i = 0; i < n; ++i) done_col[i] = false;
	string sts;
	for (int i = 0; i < n; ++i) if(!done_col[i]) {
		vector<int> rows;
		for(int j = 0; j < n; ++j) if (s[j][i] == '1') rows.push_back(j);
		if(rows.size() == 0) return false;
		for(int j = 1; j < rows.size(); ++j) if(s[rows[j]] != s[rows[0]]) return false;
		int col_count = 0;
		for(int j = 0; j < n; ++j) if(s[rows[0]][j] == '1'){
			++col_count;
			done_col[j] = true;
		}
		if(col_count != rows.size()) return false;
	}
	return true;
}

void dfs(int x, int y, int now){
	if(now >= best) return;
	if(y >= n) { y = 0; ++x; }
	if(x >= n) {
		if (check()){
			best  = now;
		}
		return;
	}
	if(s[x][y] != '1'){
		s[x][y] = '1';
		dfs(x, y+1, now+1);
		s[x][y] = '0';
	}
	dfs(x, y+1, now);
}

void solve(){
	cin >> n;
	for(int i = 0; i < n; ++i) cin >> s[i];
	best = n * n;
	dfs(0, 0, 0);
	cout << best << endl;
}

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i){
		cout << "Case #" << i <<": ";
		solve();
	}
	return 0;
}
