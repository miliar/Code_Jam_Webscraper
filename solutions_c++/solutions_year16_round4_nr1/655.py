#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 15;

string def = "RPS";

string str[3][N];
int n, r, p, s;

void solve(int);

int main () {

	ios::sync_with_stdio(false);
	
	for(int i = 0;i < N;i++) {
		if (i == 0) {
			str[0][i] = "R";
			str[1][i] = "P";
			str[2][i] = "S";
		} else {
			// R -> RS
			str[0][i] = min(str[0][i-1], str[2][i-1]) + max(str[0][i-1], str[2][i-1]);
			// P -> PR
			str[1][i] = min(str[1][i-1], str[0][i-1]) + max(str[1][i-1], str[0][i-1]);
			// S -> PS
			str[2][i] = min(str[1][i-1], str[2][i-1]) + max(str[1][i-1], str[2][i-1]);
		}
	}

	int test_num;
	cin >> test_num;
	for (int case_id = 1;case_id <= test_num;case_id++) {
		solve(case_id);
	}

	return 0;
}
void solve ( int case_id ) {

	int n, a, b, c;
	cin >> n >> a >> b >> c;

	cout << "Case #" << case_id << ": ";
	vector<string> ans;
	for ( int j = 0;j < 3;j++ ) {
		int ans1 = count ( str[j][n].begin(), str[j][n].end(), 'R') == a;
		int ans2 = count ( str[j][n].begin(), str[j][n].end(), 'P') == b;
		int ans3 = count ( str[j][n].begin(), str[j][n].end(), 'S') == c;
		if( ans1 and ans2 and ans3 ) {
			ans.push_back(str[j][n]);
		}
	}

	sort(ans.begin(), ans.end());

	if(ans.empty()) {
		cout << "IMPOSSIBLE" << endl;
	}else {
		cout << ans[0] << endl;
	}
}