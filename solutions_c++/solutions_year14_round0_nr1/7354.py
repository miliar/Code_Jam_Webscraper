#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(void)
{
	freopen("temp.in", "r", stdin);
	freopen("temp.out", "w", stdout);
	int T, line1, line2, non_sense;
	int num1[4], num2[4];

	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		cin >> line1;
		for (int j = 1; j <= 4; ++j)
		{
			for (int k = 1; k <= 4; ++k)
			{
				if (j == line1)
				{
					cin >> num1[k - 1];
				}
				else
				{
					cin >> non_sense;
				}
			}
		}
		cin >> line2;
		for (int j = 1; j <= 4; ++j)
		{
			for (int k = 1; k <= 4; ++k)
			{
				if (j == line2)
				{
					cin >> num2[k - 1];
				}
				else
				{
					cin >> non_sense;
				}
			}
		}

		vector<int> num_count(16, 0);

		for (int j = 0; j < 4; ++j)
		{
			++num_count[num1[j] - 1];
			++num_count[num2[j] - 1];
		}

		int result_count = 0, result_num = -1;
		for (int j = 0; j < 16; ++j)
		{
			if (num_count[j] == 2)
			{
				++result_count;
				result_num = j + 1;
			}
		}
		
		if (result_count == 1)
		{
			cout << result_num << endl;
		}
		else if (result_num > 1)
		{
			cout << "Bad magician!" << endl;
		}
		else
		{
			cout << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}