#include <iostream>
#include <string>
using namespace std;
int T;
int n;
int arr[1005];
int arr2[1005];
string s;
int task() {
	int ans = 0;
	for (int i = 0; i <= n; i++) {
		if (i == 0) arr2[i] = arr[i];
		else arr2[i] = arr2[i - 1] + arr[i];
	}
	for (int i = 0; i <= n; i++) {
		if (arr[i] != 0 && arr2[i - 1] < i) {
			ans += i - arr2[i - 1];
			for (int j = i; j <= n; j++) {
				arr2[j] += i - arr2[i - 1];
			}
		}
	}
	return ans;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	for (int i = 0; i < 1004; i++) {
		arr[i] = 0;
		arr2[i] = 0;
	}
	cin >> T;
	
	for (int k = 1; k <= T;k++){
		cin >> n;
		cin >> s;
		for (int i = 0; i <= n; i++) {
			arr[i] = s[i]-'0';
		}
		cout << "Case #" << k << ": " << task() << endl;
	}



	return 0;
}