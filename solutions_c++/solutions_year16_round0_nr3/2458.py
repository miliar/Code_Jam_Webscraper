#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long gcd(long long a, long long b){
	if (a < b)
		return gcd(b, a);

	return b ? gcd(b, a % b) : a;
}

int main(){
	int t, n, aim, cnt = 0, cnt2;
	vector<int> V;

	scanf("%d\n%d %d", &t, &n, &aim);
	puts("Case #1:");

	for (int i = 1; i <= n; i++){
		V.resize(i, 0);
		V.resize(n, 1);

		do{
			if (V[0] != 1 || V[n - 1] != 1)
				continue;

			if (cnt == aim)
				break;

			cnt2 = 0;
			int ans[11] = {0};

			for (int j = 2; j <= 10; j++){
				bool found = false;
				int d = n - 1;
				long long t = 0;

				while (d >= 0){
					t += V[n - d - 1] * pow(j, d);
					d--;
				}

				long long sqrt_t = sqrt(t);
				for (int k = 3; k <= sqrt_t; k += 2){
					long long r = gcd(k, t);

					if (r != 1){
						ans[j] = k;
						cnt2++;
						found = true;
						break;
					}
				}

				if (!found)
					break;
			}

			if (cnt2 == 9){
				for (int k = 0; k < n; k++){
					printf("%d", V[k]);
				}
				for (int k = 2; k <= 10; k++){
					printf(" %d", ans[k]);
				}
				puts("");
				cnt++;
			}
		} while (next_permutation(V.begin(), V.end()));

		V.clear();
	}

	return 0;
}

