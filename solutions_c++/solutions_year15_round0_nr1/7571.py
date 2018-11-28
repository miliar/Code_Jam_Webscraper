// a_small.cpp Amit Thakur
#include <cstdio>
#define s(n) scanf("%d", &n)




int main() {
	int T; s(T);
	for (int t = 0; t < T; t++) {
		int sMax; s(sMax); char ch[sMax+2]; scanf("%s", ch); int *nr = new int[sMax+1];
		int ans = 0; int sum = nr[0] = (ch[0] - '0');	
		for (int i = 1 ; i <= sMax; i++) {
			nr[i] = ch[i] - '0';	
			if (nr[i] > 0) {
				if (sum >= i) {
					sum += nr[i];
				
				} else {
					int k = (i - sum);
					ans += k;
					sum += k;
					sum += nr[i];
				}
			} else {
				continue;
			}
		}

		printf("Case #%d: %d\n", (t+1), (ans));
		delete[] nr;
	}

	return 0;
}
