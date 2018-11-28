#include <stdio.h>
#include <vector>
using namespace std;
int N, M, mx, cnt;
char s[11][11];
int d_same[9][9];
vector <int> d_server[5];
int d[9];
int chk[10];
void get_ans(int lvl) {
	if(lvl == M+1) {
		int i, j, k, k2, tmp = 0, tmp2;
		for(i = 1; i <= 4; i++) {
			while(d_server[i].size() != 0) d_server[i].pop_back();
		}
		for(i = 1; i <= M; i++) {
			d_server[d[i]].push_back(i);
		}
		for(i = 1; i <= N; i++) {
			if(d_server[i].size() == 0) break;
		}
		if(i != N+1) return;
		for(i = 1; i <= N; i++) {
			for(k = 0; k < d_server[i].size(); k++) chk[k] = 0;
			for(j = 1; j <= 10; j++) {
				for(k = 0; k < d_server[i].size(); k++) {
					if(chk[k] == j) continue;
					chk[k] = j;
					if(s[d_server[i][k]][j] == 0) continue;
					tmp++;
					for(k2 = k+1; k2 < d_server[i].size(); k2++) {
						if(d_same[d_server[i][k]][d_server[i][k2]] >= j) chk[k2]=j;
					}
				}
			}
			tmp++;
		}
		if(tmp > mx) {
			mx = tmp;
			cnt = 1;
		}
		else if(tmp == mx) {
			cnt++;
		}
		return;
	}
	for(int i = 1; i <= N; i++) {
		d[lvl] = i;
		get_ans(lvl+1);
	}
	return;
}
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("ans4.txt", "w", stdout);
	int T, test_no, i, j, k;
	scanf("%d", &T);
	for(test_no = 1; test_no <= T; test_no++) {
		for(i = 1; i <= 10; i++) for(j = 0; j <= 10; j++) s[i][j] = 0;
		scanf("%d %d", &M, &N);
		for(i = 1; i <= M; i++) scanf("%s", s[i]+1);
		for(i = 1; i <= M; i++) {
			for(j = i+1; j <= M; j++) {
				for(k = 1;; k++) {
					if(s[i][k] != s[j][k]) break;
					if(s[i][k] == 0 && s[j][k] == 0) break;
				}
				d_same[i][j] = k-1;
			}
		}
		mx = 0, cnt = 0;
		get_ans(1);
		printf("Case #%d: %d %d\n", test_no, mx, cnt);
	}
	return 0;
}