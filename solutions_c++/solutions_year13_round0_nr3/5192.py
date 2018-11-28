#include <iostream>
using namespace std;

int main()
{
	int ans[1002] = {0};
	ans[1] = 1;
	ans[4] = 1;
	ans[9] = 1;
	ans[121] = 1;
	ans[484] = 1;
	
	for (int i = 1; i <= 1000; i++) {
		ans[i] += ans[i - 1];
	}
	int t;
	int a, b;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> a;
		cin >> b;
		cout << "Case #" << i << ": " << ans[b] - ans[a - 1] << endl;
	}

	return 0;
}
