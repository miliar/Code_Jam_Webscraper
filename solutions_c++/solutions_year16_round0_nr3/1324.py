#include <cstdio>
#include <vector>
#include <bitset>
int len, j;
int limits = 1;
int go(std::vector<int> arr, int depth) {
	if (depth == len - 1) {
		std::vector<int> ans;
		for (int i = 2; i <= 10; i++) {
			for (int j = 3; j <= 100; j++) {
				int tmp = j;
				int count=0;
				while (tmp != 0) {
					tmp /= j;
					count++;
				}
				if (count >= len) 
					return 0;
				long long befdiv = 1;
				long long modsum = 1;
				long long val = 1;
				long long tot = 1;
				for (int k = 1; k < len; k++) {
					befdiv *= i;
					val *= i;
					befdiv %= j;
					if (arr[k] == 1) {
						modsum += befdiv;
						modsum %= j;
						tot += val;
					}
				}
				if (modsum == 0) {
					ans.push_back(j);
					break;
				}
			}
		}
		if (ans.size() != 9) 
			return 0;
		
		for (auto i = arr.rbegin(); i != arr.rend(); i++) { printf("%d", *i); }
		for (auto i : ans) { printf(" %d", i); }
		printf("\n");
		j--;
		if (j == 0) 
			exit(0);
	}
	else {
		go(arr, depth + 1);
		arr[depth] = 1;
		go(arr, depth + 1);
	}
}
int main(void) {
	int t;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	scanf("%d%d", &len, &j);
	printf("Case #1:\n");
	std::vector<int> arr(len, 0);
	int count = 0;
	while (count++ < len) limits *= 2;
	arr[0] = 1;
	arr[len - 1] = 1;
	go(arr, 1);
}