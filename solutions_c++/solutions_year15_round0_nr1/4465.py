#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {

		int a;
		cin >> a;
		int sum = 0, ans = 0;
		for(int i = 0; i <= a; ++i) {
			char b;
			cin >> b;

			if(sum < i) {
				ans += i - sum;
				sum += i - sum;
			}
			sum += b - '0';
		}

		cout << "Case #" << t << ": ";
		cout << ans << endl;

	}
}
