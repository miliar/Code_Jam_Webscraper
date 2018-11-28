#include <bits/stdc++.h>

using namespace std;

#define INP "inp.txt"
#define OUT "out.txt"

int T, N;

long long solve() {
	if (!N) return -1ll;
	long long NN = N;
	int cnt = 1, flag[10], flag_num = 0;
	memset(flag, 0, sizeof(flag));
	while(true) {
		long long tmp = NN * cnt;

		while(tmp) {
			int d = tmp % 10;
			if(!flag[d]) {
				flag[d] = 1;
				flag_num++;
				if(flag_num == 10) return NN * cnt;
			}
			tmp /= 10;
		}
		cnt++;
	} 
}

int main () {
	freopen(INP, "r", stdin);
	freopen(OUT, "w", stdout);

	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++) {
		scanf("%d", &N);
		printf("Case #%d: ", tt);
		long long ans = solve();
		if(ans == -1) printf("INSOMNIA\n");
		else cout << ans << endl;
	}
	return 0;
}