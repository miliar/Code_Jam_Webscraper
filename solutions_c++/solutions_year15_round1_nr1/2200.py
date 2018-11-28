#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	//ifstream infile("in.txt");
	//cin.rdbuf(infile.rdbuf());

	//ofstream outfile("out.txt");
	//cout.rdbuf(outfile.rdbuf());

	//for (int i = 0; i < 1000; i++)
	//{
	//	if (i & 1)
	//		cout << 0 << ' ';
	//	else
	//		cout << 10000 << ' ';
	//}

	int t, n;

	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		int first = 0, second = 0, n;
		cin >> n;
		vector<int> data(n);
		for (int i = 0; i < n; i++)
		{
			cin >> data[i];
		}

		for (int i = 1; i < n; i++)
		{
			if (data[i] < data[i - 1])
				first += data[i - 1] - data[i];
		}

		for (int speed = 0; speed <= 50000; speed++)
		{
			int i;
			second = 0;
			for (i = 1; i < n; i++)
			{
				int rem = data[i - 1] - speed;

				if (data[i] < rem)
					break;

				if (rem >= 0)
					second += speed;
				else
				{
					second += data[i - 1];
				}
			}

			if (i == n)
			{
//				cout << speed << endl;
				break;
			}
		}

		cout << "Case #" << tc << ": " << first << ' ' << second << endl;
	}

	return 0;
}
