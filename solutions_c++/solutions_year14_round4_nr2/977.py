#include <cstdio>
#include <algorithm>
using namespace std;
int num[1010];
int idx[1010];
bool cmp (int ida, int idb) {
	return num[ida] < num[idb];
}

int main () {
	int T;
	int tt = 1;
	scanf("%d", &T);
	while (T--) {
		int N;
		scanf("%d", &N);
		for (int i = 0 ; i < N ; i++) {
			scanf("%d", &num[i]);
		}
		for (int i = 0 ; i < N ; i++){
			idx[i] = i;
		}
		sort(idx, idx+N, cmp);
		int ans = 0;
		int l = 0, r = N-1;
		for (int i = 0 ; i < N ; i++) {
			//printf("l %d r %d\n", l, r);
			//printf("%d\n", idx[i]);
			if (idx[i]-l <= r-idx[i]) {
				ans += (idx[i]-l);
				for (int j = i+1 ; j < N ; j++){
					if(idx[j] < idx[i]) {
						idx[j]++;
					}
				}
				l++;
			}
			else {
				ans += (r-idx[i]);
				for (int j = i+1 ; j < N ; j++) {
					if(idx[j] > idx[i]) {
						idx[j]--;
					}
				}
				r--;
			}
		}
		printf("Case #%d: %d\n", tt, ans);
		tt++;
	}
	return 0;
}
