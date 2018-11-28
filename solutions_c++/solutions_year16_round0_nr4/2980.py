#include<iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		int k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << i << ": ";
		for (int j = 1; j <=k; j++)	cout << j << " ";
		cout << "\n";
	}
}
