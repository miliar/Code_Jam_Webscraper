#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 0; i < numCases; ++i)
	{
		int row1;
		cin >> row1;
		unordered_set<int> s;
		int a, b, c, d;

		for (int j = 1; j <= 4; ++j)
		{
			cin >> a >> b >> c >> d;
			if (j == row1)
			{
				s.insert(a);
				s.insert(b);
				s.insert(c);
				s.insert(d);
			}
		}

		int numUnique = 0;
		int card;
		int row2;
		cin >> row2;

		for (int j = 1; j <= 4; ++j)
		{
			cin >> a >> b >> c >> d;
			if (j == row2)
			{
				if (s.count(a) > 0)
				{
					numUnique++;
					card = a;
				}
				if (s.count(b) > 0)
				{
					numUnique++;
					card = b;
				}
				if (s.count(c) > 0)
				{
					numUnique++;
					card = c;
				}
				if (s.count(d) > 0)
				{
					numUnique++;
					card = d;
				}
			}
		}

		cout << "Case #" << i << ": ";
		if (numUnique == 1)
		{
			cout << card << endl;
		}
		else if (numUnique == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
		}
	}
}