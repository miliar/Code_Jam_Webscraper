#include <bits/stdc++.h>
using namespace std;

const int MAXN = 10000;
int T;
char S[MAXN];
int Flip[MAXN];
int K;
int cas = 0;
int main() {
	freopen("./in.txt", "r", stdin);
	freopen("./out.txt", "w", stdout);
	cin >> T;
	while(T--) {
		memset(Flip, 0, sizeof(Flip));
		printf("Case #%d: ", ++cas);
		scanf("%s", S);
		scanf("%d", &K);
		int ans = 0;
		int f = 0;
		int len = strlen(S);
		for(int i = 0; i < len; i++) {
			//cout << i << " " << f << endl;
			int c = (S[i] == '+');
			if(!(c ^ f)) {
				if(i + K > len) {
					ans = -1;
					break;
				} else {
					f ^= 1;
					Flip[i] = 1;
					ans++;
				}
			} else {
			}
			if(i - K + 1 >= 0) {
				f ^= Flip[i - K + 1];
			}
		}
		if(ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
