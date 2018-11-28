#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int song[10010];

bool use[10010];

int main () {
	int T;
	int tt = 1;
	scanf("%d", &T);
	while (T--) {
		memset(use, false, sizeof(use));
		int N, X;
		scanf("%d%d", &N, &X);
		for (int i = 0 ; i < N ; i++) {
			scanf("%d", &song[i]);
		}
		sort(song, song+N);

		int ans = 0;
		for (int i = 0 ; i < N ; i++) {
			if (use[i] == false) {
				use[i] = true;
				ans++;
				int L = i+1, R = N-1;
				int idxa = -1;
				while (L <= R) {
					int mid = (L+R)/2;
					if (song[mid]+song[i] > X) {
						if(song[mid]+song[i] == X) idxa = mid;
						R = mid-1;
					} else {
						idxa = mid;
						L = mid+1;
					}
				}
				if (idxa != -1) {
					for (int j = idxa ; j > i ; j--) {
						if (use[j] == false) {
							use[j] = true;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", tt, ans);
		tt++;
	}
	return 0;
}
