#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	int T; cin >> T;
	for (int k = 1; k <= T; k++)
	{
		int smax; cin >> smax;
		string input; cin >> input;
		long long sum = 0, needed = 0;
		for (int i = 0; i <= smax; i++)
		{
			if (sum < i)
			{
				needed += i - sum; sum = i;
			}
			int num = input.at(i) - '0';
			sum += num;
		}
		cout << "Case #" << k << ": " << needed << endl;
	}
	return 0;
}