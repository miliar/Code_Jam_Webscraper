#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("in.txt");
	int t;

//	cin.rdbuf(in.rdbuf());
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		string value;
		cin >> value >> value;

		int sum = value[0]-'0', ans = 0;
		for (int i = 1; i < value.size();)
		{
			if (i <= sum)
			{
				sum += value[i] - '0';
				i++;
			}
			else
			{
				sum++;
				ans++;
			}
		}

		cout << "Case #" << tc << ": " << ans << endl;
	}

	return 0;
}
