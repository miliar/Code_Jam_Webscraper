#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
	int T;
	cin >> T;
//	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		long long B, N;
		cin >> B >> N;
//		scanf("%d%d", &B, &N);
		vector<long long> a(37, 0);
		for (int i = 0; i < N; ++i) {
			cin >> a[i];
//			scanf("%d", &a[i]);
		}
		sort(a.begin(), a.end());

		double ret = 0;
		for (int i = (37 - N); i <= 36; ++i) {
			// 당첨될 확률이 있는 슬롯 수 = i (37이면 무조건 손해볼듯?)
			for (int j = 1; j <= i; ++j) {
				// j개가 최소값이고 나머지는 적어도 최소값+1 이상임
				
				long long left = 1, right = 9879879879879LL;
				long long mid, jm = -1;
				while (left <= right) {
					mid = (left + right) / 2;

					long long need = 0;
					{
						for (int k = 0; k < 37; ++k) {
							if (k < j) {
								need += mid - a[k];
							} else {
								if (a[k] < (mid + 1)) {
									need += (mid + 1) - a[k];
								} 
							}
						}
					}
					if (need > B) {
						right = mid - 1;
					} else {
						left = mid + 1;
						jm = mid;
					}
				}
				
				// need가 B를 안넘어가는 최대 jm을 구하자.
//				for (int jm = 1; jm <= 9999; ++jm) {
					long long need = 0;
					long long earn = 0;
					bool ispos = true;
					for (int k = 0; k < 37; ++k) {
						if (k < j) {
							if (a[k] > jm) { ispos = false; break; }
							need += jm - a[k];
							earn += 36 * (jm - a[k]);
						} else {
							if (a[k] < (jm + 1)) {
								need += (jm + 1) - a[k];
							} 
						}
					}
					if (need > B) break;
					if (ispos) {
						double tmp = earn * 1.0 / i - need;
						if (ret < tmp) { ret = tmp; }
					}
//				}
//				if (njm != -1) { printf("njm = %d, pjm = %d\n", njm, pjm); }
			}
		}
/*		
		double ret = 0;
		for (int i = 1; i <= maxm + 1; ++i) {
			// need money;
			int need = (37 - N) * i;
			int winm = (37 - N) * 36 * i;
			int totp = (37 - N), same = 0;
			for (int j = 0; j < N; ++j) {
				if (i > a[j]) {
					need += (i - a[j]);
					winm += (i - a[j]) * 36;
					totp++;
				}
				if (i == a[j]) { totp++; same++; }
			}
			if (need > B) break;
			for (int j = 0; j <= same; ++j) {
				if (ret < winm * 1.0 / (totp - j) - (need + j) && (need + j <= B))
				{
					ret = winm * 1.0 / (totp - j) - (need + j);
				}
			}
		}
*/
		printf("Case #%d: %.10lf\n", cn, ret);
	}
}

