#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int arr[10010];
int main() {
	int T; scanf("%d", &T);
	for(int kase = 1; kase <= T; ++kase) {
		int a, b;
		scanf("%d%d", &a, &b);
		for(int i = 0; i < a; ++i)
			scanf("%d", &arr[i]);
		sort(arr, arr+a);
		int ans = 0;
		int i = 0, j = a-1;
		while(i <= j) {
			//printf("%d %d\n", i, j);
			if(i == j) {
				i++;
				ans++;
				break;
			}
			else if(arr[i] + arr[j] > b) {
				j--;
				ans++;
			}
			else {
				i++;
				j--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	return 0;
}