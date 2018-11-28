#include <cstdio>
using namespace std;

int main() {
	int T, t, L, i, cnt, sum, temp;
	char S[1005];
	
	freopen("A-large.in", "r", stdin);
	freopen("A.txt", "w", stdout);
	
	scanf("%d", &T);
	for (t = 1; t <= T; ++t) {
		scanf("%d %s", &L, S);
		for (i = cnt = sum = 0; i <= L; ++i) {
			if (S[i] != '0' && i > sum) {
				temp = i-sum;
				cnt += temp;
				sum += temp;
			}
			sum += S[i]-'0';
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	
	return 0;
}
