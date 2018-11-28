#include <iostream>
#include <vector>
#include <string>

using namespace std;

void main() {

	FILE *str, *abc;
	freopen_s(&str, "input.txt", "r", stdin);
	freopen_s(&abc, "out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		
		int n;
		int w[3000] = {};
		cin >> n;

		for (int j = 0; j<2*n-1; j++)
			for (int i = 0; i < n; i++)
			{
				int a;
				cin >> a;
				w[a]++;
			}

		vector<int> ans;

		for (int i = 0; i < 3000; i++)
			if (w[i] % 2) ans.push_back(i);

		for (int i = 0; i < n; i++)
			cout << ans[i] << " ";
		cout << endl;
	}
	

}