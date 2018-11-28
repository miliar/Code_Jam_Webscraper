#include <cstdio>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in.txt", "r", stdin);
	freopen("mt.out", "w", stdout);
	set<int> cards;
	set<int>::iterator found;
	int tmp, t, row, foundCount, result;
	cin >> t;
	for(int ti = 1; ti <= t; ti++)
	{
		cin >> row;
		for(int r = 1; r <= 4; r++)
		{
			for(int c = 1; c <= 4; c++)
			{
				cin >> tmp;
				if(r == row)
				{
					cards.insert(tmp);
				}
			}
		}
		cin >> row;
		foundCount = 0;
		for(int r = 1; r <= 4; r++)
		{
			for(int c = 1; c <= 4; c++)
			{
				cin >> tmp;
				if(r == row)
				{
					found = cards.find(tmp);
					if(found != cards.end())
					{
						result = *found;
						foundCount++;
					}
				}
			}
		}
		if(foundCount == 0)
		{
			cout << "Case #" << ti << ": Volunteer cheated!\n";
		}
		else if(foundCount == 1)
		{
			cout << "Case #" << ti << ": " << result << "\n";
		}
		else
		{
			cout << "Case #" << ti << ": Bad magician!\n";
		}
		cards.clear();
	}
	return 0;
}