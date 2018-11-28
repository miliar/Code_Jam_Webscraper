#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int n, test1_row_num, test2_row_num;
	int test1_row[4], test2_row[4];
	int ignore;
	cin >> n;
	for (int i = 1; i <= n; ++i)
	{
		cin >> test1_row_num;
		for (int j = 1; j <= 4; ++j)
		{
			if (j == test1_row_num)
			{
				cin >> test1_row[0] >> test1_row[1] >> test1_row[2] >> test1_row[3];
			}
			else
			{
				cin >> ignore >> ignore >> ignore >> ignore;
			}
		}
		cin >> test2_row_num;
		for (int j = 1; j <= 4; ++j)
		{
			if (j == test2_row_num)
			{
				cin >> test2_row[0] >> test2_row[1] >> test2_row[2] >> test2_row[3];
			}
			else
			{
				cin >> ignore >> ignore >> ignore >> ignore;
			}
		}
		int count = 0, answer;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if (test1_row[j] == test2_row[k])
				{
					++count;
					answer = test2_row[k];
					break;
				}
			}
			if (count>1)
			{
				break;
			}
		}
		if (count == 0)
		{
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		else if (count > 1)
		{
			cout << "Case #" << i << ": Bad magician!" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << answer << endl;
		}
	}
	return 0;
}