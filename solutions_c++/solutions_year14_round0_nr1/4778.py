#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int test = 1; test <= T; test++)
	{
		int numbers[17];
		memset(numbers, 0, 17*sizeof(int));

		for (int i = 0; i < 2; i++)
		{
			int answer;
			cin >> answer;

			for (int j = 1; j <= 4; j++)
			{
				for (int k = 1; k <= 4; k++)
				{
					int number;
					cin >> number;

					if (j == answer)
						numbers[number]++;
				}
			}
		}

		int histogram[3];
		memset(histogram, 0, 3*sizeof(int));

		for (int i = 1; i <= 16; i++)
		{
			histogram[numbers[i]]++;
		}

		cout << "Case #" << test << ": ";

		if (histogram[2] > 1)
		{
			cout << "Bad magician!" << endl;
		} else if (histogram[2] == 1)
		{
			for (int i = 1; i <= 16; i++)
			{
				if (numbers[i] == 2)
				{
					cout << i << endl;
					break;
				}
			}
		} else
		{
			cout << "Volunteer cheated!" << endl;
		}
	}

	return 0;
}

