#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int main() {
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int T , cas = 1;
	scanf("%d",&T);
	while (T --) {
		long long n , p;
		cin >> n >> p;
		long long maxn = 1<<n;
		if (p == maxn) {
			cout << "Case #" << cas ++ << ": " << maxn - 1 << " " << maxn - 1 << endl;
			continue;
		} else if (p == 1) {
			cout << "Case #" << cas ++ << ": " << 0 << " " << 0 << endl;
			continue;
		}
		long long cnt = 0;
		long long maxp = 0;
		long long resa = 0;
		for (long long i = 0; i < maxn ; i += (1<<cnt)) {
			if (maxp < p) {
				resa = i;
			} else {
				break;
			}
			cnt ++;
			maxp |= (1<<(n - cnt));
		}
		resa = min(resa , maxn - 1);

		long long resb = maxn - 1;
		cnt = 0;
		long long minp = maxn - 1;
		for (long long i = maxn - 1 ; i >= 0 ; i -= (1<<cnt)) {
			if (minp < p) {
				resb = i + (1<<(cnt)) - 1;
				break;
			}
			cnt ++;
			minp ^= (1<<(n-cnt));
		}
		resb = max(resb , 0LL);
		cout << "Case #" << cas ++ << ": " << resa << " " << resb << endl;
	}
	return 0;
}