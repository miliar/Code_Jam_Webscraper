#include <iostream>
#include <vector>

using namespace std;

const int card_num = 16;

bool find_elem(vector<int>& row, int the_card)
{
	for (int i = 0; i < row.size(); i++)
	{
		if (the_card == row[i])
		{
			return true;
		}
	}

	return false;
}

int main(void)
{
	int cases;
	cin >> cases;

	int first_row;
	int second_row;
	int card;

	vector<int> row;

	for (int i = 0; i < cases; i++)
	{
		row.clear();
		int count = 0;
		int the_card;
		cin >> first_row;
		for (int j = 0; j < card_num; j++)
		{
			cin >> card;

			if (j >= 4*(first_row-1) && j <= 4*first_row-1)
			{
				row.push_back(card);
			}
		}

		cin >> second_row;
		for (int j = 0; j < card_num; j++)
		{
			cin >> card;

			if (j >= 4*(second_row-1) && j <= 4*second_row-1)
			{
				if (find_elem(row, card))
				{
					++count;
					the_card = card;
				}
			}
		}

		cout <<"Case #"<<i+1<<": ";

		if (0 == count)
		{
			cout << "Volunteer cheated!";
		}
		else if(count > 1)
		{
			cout << "Bad magician!";
		}
		else
		{
			cout << the_card;
		}

		cout << endl;
	}
	return 0;
}
