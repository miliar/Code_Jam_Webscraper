#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	int t, n;
	vector<int> V;

	scanf("%d", &t);

	for (int i = 1; i <= t; i++){
		V.resize(10);
		scanf("%d", &n);

		if (n == 0){
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}

		int cnt = 0, k = 1;
		long long tester, tmp;
		while (1){
			tester = n * k;
			tmp = tester;
			int divider = pow(10, (int) log10(tester));

			while (divider != 0){
				if (!V[(tmp / divider) % 10]){
					V[(tmp / divider) % 10] = 1;
					cnt++;
				}

				if (cnt == 10)
					break;

				divider /= 10;
			}

			if (cnt == 10)
				break;

			k++;
		}

		printf("Case #%d: %lld\n", i, tester);

		V.clear();
	}

	return 0;
}

