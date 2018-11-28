#include "bits/stdc++.h"
using namespace std;
int n, m;
int arr[26];
int main() {
	freopen("input.in", "r", stdin);
	freopen("output.text", "w", stdout);
	int Case;
	cin >> Case;
	for (int tc = 1; tc <= Case;tc++) {
		int N;
		scanf("%d", &N);
		int sum = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
			sum += arr[i];
		}
		string ans = "";
		int max_value=0;
		int idx;
		for (int i = 0; i < N; i++) 
			if (max_value < arr[i]) {
				max_value = arr[i];
				idx = i;
			}
		if (sum & 1) {
			ans += (char)(idx+'A');
			ans += " ";
			arr[idx]--;
		}
		while (true) {
			max_value = 0;
			for (int i = 0; i < N;i++)
				if (max_value < arr[i]) {
					max_value = arr[i];
					idx = i;
				}
			ans += (char)(idx + 'A');
			arr[idx]--;
			max_value = 0;
			for (int i = 0; i < N; i++)
				if (max_value < arr[i]) {
					max_value = arr[i];
					idx = i;
				}
			ans += (char)(idx + 'A');
			arr[idx]--;
			max_value = 0;
			for (int i = 0; i < N; i++)
				if (max_value < arr[i]) {
					max_value = arr[i];
					idx = i;
				}
			if (!max_value)
				break;
			ans += " ";
		}
		cout << "Case #" << tc << ": ";
		cout << ans << endl;
	}
	return 0;
}