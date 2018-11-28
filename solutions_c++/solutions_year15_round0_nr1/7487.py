#include <iostream>
#include <string>

using namespace std;

int main()  {
	freopen("input.file", "r", stdin);
	freopen("output.file", "w", stdout);
	int t;

	cin >> t;

	for (int i = 0; i < t; i++){
		int n;
		cin >> n;
		string smax;
		cin >> smax;
		int sum = 0, cnt = 0;
		for (int j = 0; j <= n; j++){
			if (j - cnt > 0) {
				sum += j - cnt;
				cnt += j - cnt;
			}
			cnt += smax[j] - 48;
		}
		
		printf("Case #%d: %d\n", i + 1, sum);
	}
}