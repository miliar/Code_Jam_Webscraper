#include <iostream>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, k, c, s, j;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> k >> c >> s;
		cout << "Case #" << i << ":";
		for(j = 1; j <= s; j++)
			cout << " " << j;
		cout << endl;
	}
	return 0;
}

