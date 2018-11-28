#include <iostream>
#include <fstream>

using namespace std;
int main()
{
	//ifstream cin("test2.in");
	//ofstream cout("test.out");
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test)
	{
		int n;
		cin >> n;
		cin.ignore(1);
		int total = 0;
		int friends = 0;
		for (int i = 0; i <= n; ++i)
		{
			char qi;
			cin >> qi;
			qi -= '0';
			if (total < i)
			{
				friends += i - total;
				total = i;
			}
			total += qi;
		}
		cout << "Case #" << test+1 << ": " << friends << '\n';
	}
	return 0;
}