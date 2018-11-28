#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>
using namespace std;

const string hand = "RPS";
string candidate = "";
int rk[20][3];

void solve(int depth, int winner) {
	if(!depth) {
		candidate += hand[winner];
		return;
	}

	if(rk[depth-1][winner] < rk[depth-1][(winner+2)%3]) {
		solve(depth-1,winner);
		solve(depth-1,(winner+2)%3);
	}
	else {
		solve(depth-1,(winner+2)%3);
		solve(depth-1,winner);
	}
}

int compare_depth;
bool cmp(int a, int b) {
	int aa[2], bb[2];
	aa[0] = a; aa[1] = (a+2)%3;
	bb[0] = b; bb[1] = (b+2)%3;

	if(rk[compare_depth-1][aa[0]] > rk[compare_depth-1][aa[1]])
		swap(aa[0], aa[1]);
	if(rk[compare_depth-1][bb[0]] > rk[compare_depth-1][bb[1]])
		swap(aa[0], bb[1]);

	if(rk[compare_depth-1][aa[0]] != rk[compare_depth-1][bb[0]])
		return rk[compare_depth-1][aa[0]] < rk[compare_depth-1][bb[0]];
	return rk[compare_depth][aa[1]] < rk[compare_depth][bb[1]];
}

int main() {
	int T;
	const string ng = "IMPOSSIBLE";

	rk[0][0] = 1;
	rk[0][1] = 0;
	rk[0][2] = 2;
	for(int i = 1; i < 20; i++) {
		int tmp[] = {0,1,2};
		compare_depth = 1;
		sort(tmp, tmp+3, cmp);
		for(int j = 0; j < 3; j++)
			rk[i][tmp[j]] = j;
	}

	cin >> T;
	for(int t = 1; t <= T; t++) {
		int N, R, P, S;
		bool flg = false;
		string res = ng;
		cin >> N >> R >> P >> S;
		for(int i = 0; i < 3; i++) {
			int cnt[3] = {};
			candidate = "";
			solve(N, i);
			for(int j = 0; j < candidate.size(); j++) {
				char c;
				c = candidate[j];
				if(c == 'R')
					cnt[0]++;
				else if(c == 'P')
					cnt[1]++;
				else if(c == 'S')
					cnt[2]++;
				else
					assert(0);
			}
			if(cnt[0] == R && cnt[1] == P && cnt[2] == S) {
				if(!flg)
					res = candidate;
				else
					res = min(res, candidate);
				flg = true;
			}
		}

		cout << "Case #" << t << ": " << res << endl;
	}
}
