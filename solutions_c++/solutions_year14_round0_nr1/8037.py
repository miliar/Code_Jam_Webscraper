#include <iostream>

using namespace std;

int main(void)
{
	int test_size;

	cin >> test_size;

	for(int counter = 1; counter <= test_size; counter++)
	{
		int ans_first, ans_next, chose_first[4], chose_next[4];
		cin >> ans_first;

		for(int row = 1; row <= 4; row++)
		{
			for(int j = 0; j < 4; j++)
			{
				int number;
				cin >> number;
				if(row == ans_first)
					chose_first[j] = number;
			}
		}

		cin >> ans_next;

		for(int row = 1; row <= 4; row++)
		{
			for(int j = 0; j < 4; j++)
			{
				int number;
				cin >> number;
				if(row == ans_next)
					chose_next[j] = number;
			}
		}
		int found = 0;
		int answer = 0;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(chose_first[i] == chose_next[j])
				{
					answer = chose_first[i];
					found++;
				}
			}
		}

		if(found > 1)
			cout << "Case #" << counter << ": Bad magician!\n";
		else if(found == 0)
			cout << "Case #" << counter << ": Volunteer cheated!\n";
		else if(found == 1)
			cout << "Case #" << counter << ": " << answer << endl;
	}
	return 0;
}
