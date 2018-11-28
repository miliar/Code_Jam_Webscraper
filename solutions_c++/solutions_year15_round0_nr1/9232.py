#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int n;
		cin >> n;
		string str;
		cin >> str;

		int added = 0;
		int sum = str[0]-'0';

		for(int i = 1; i <= n; i++)
		{
			added = added + max(0, i-sum-added);
			sum += str[i]-'0';
		}

		cout << "Case #" << t << ": " << added << endl;
	}

	return 0;
}
