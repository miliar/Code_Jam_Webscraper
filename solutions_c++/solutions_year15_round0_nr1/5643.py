#include<iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int Smax, num, sum = 0, count = 0;
		char temp;
		cin >> Smax;
		for (int j = 0; j <= Smax; j++)//j´ú±íshy
		{
			do
			{
				cin >> temp;
			}
			while (isspace(temp));
			num = temp - '0';

			if (num != 0 && j > sum)
			{
				count = count + j - sum;
				sum = j;
			}
			sum += num;
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}