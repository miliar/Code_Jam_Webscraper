#include <bits/stdc++.h>

using namespace std;

int T;
int N, R, P, S;
string c[] = {"P", "R", "S"};
string res[20][3];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	
	for(int i = 0; i < 3; i ++) res[0][i] = c[i];
	for(int i = 1; i < 15; i ++) {
		for(int j = 0; j < 3; j ++) {
			if(res[i-1][j] + res[i-1][(j+1)%3] < res[i-1][(j+1)%3] + res[i-1][j]) {
				res[i][j] = res[i-1][j] + res[i-1][(j+1)%3];
			} else {
				res[i][j] = res[i-1][(j+1)%3] + res[i-1][j];
			}
		}
	}
	
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		bool ok = 0;
		int t;
		for(int k = 0; k < 3 && !ok; k ++) {
			int RR = 0, PP	 = 0, SS = 0;
			for(int i = 0; i < (1 << N); i ++) {
				if(res[N][k][i] == 'P') PP ++;
				if(res[N][k][i] == 'R') RR ++;
				if(res[N][k][i] == 'S') SS ++;
			}
			ok = (P == PP && R == RR && S == SS);
			if(ok) {
				t = k;
				break;
			}
		}
		printf("Case #%d: ", cas);
		if(ok) cout << res[N][t] << endl;
		else cout << "IMPOSSIBLE" << endl;
		
	}
	return 0;
}

