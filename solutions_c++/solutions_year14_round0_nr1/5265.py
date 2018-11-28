#include <iostream>
using namespace std;

int main(void)
{
	int T;
	cin >> T;
	
	for (int c = 1; c <= T; c++)
	{
		cout << "Case #"<< c << ": ";
		int r;
		int set = (1<<17) - 2;
		cin >> r;
		for (int i = 1; i <= 4; i++)
		{
			int val;
			int row = 0;
			for (int j = 0; j < 4; j++)
			{
				cin >> val;
				row |= 1<<val;
			}
			if (i == r)	set &= row;
		}
		cin >> r;
		for (int i = 1; i <= 4; i++)
		{
			int val;
			int row = 0;
			for (int j = 0; j < 4; j++)
			{
				cin >> val;
				row |= 1<<val;
			}
			if (i == r)	set &= row;
		}
		if (__builtin_popcount(set) == 0)
			cout << "Volunteer cheated!" << endl;
		else if (__builtin_popcount(set) == 1)
			cout << __builtin_ctz(set) << endl;
		else 
			cout << "Bad magician!" << endl;
			
	}
	return 0;
}
