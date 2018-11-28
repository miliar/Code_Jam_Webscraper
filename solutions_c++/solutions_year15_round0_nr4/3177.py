#include <iostream>
using namespace std;

int main()
{
	int numcases;
	int x, r, c;
	//0 = R
	//1 = G
	int three[7][7] = { 
					{-1, -1, -1, -1, -1, -1, -1}, 
					{-1, 0, 0, 0, 0, 0, 0}, 
					{-1, -1, 0, 1, 0, 0, 1},
					{-1, -1, -1, 1, 1, 1, 1}, 
					{-1, -1, -1, -1, 0, 0, 1},
					{-1, -1, -1, -1, -1, 0, 1}, 
					{-1, -1, -1, -1, -1, -1, 1}
				   };
	
	int four[7][7] = { 
					{-1, -1, -1, -1, -1, -1, -1}, 
					{-1, 0, 0, 0, 0, 0, 0}, 
					{-1, -1, 0, 0, 0, 0, 0},
					{-1, -1, -1, 0, 1, 0, 0}, 
					{-1, -1, -1, -1, 1, 1, 1},
					{-1, -1, -1, -1, -1, 0, 0}, 
					{-1, -1, -1, -1, -1, -1, 0}
				   };
	
	cin >> numcases;
	
	for (int casenum = 1; casenum <= numcases; casenum++)
	{
		cin >> x >> r >> c;
		
		//can't fill field regardless of piece choice Richard wins
		if ( (r * c) % x != 0)
		{
			cout << "Case #" << casenum << ": RICHARD" << endl;
		}
		//field can maybe be filled, have to try all possible
		else
		{
			//make c larger
			if (r > c)
			{
				int temp = r;
				r = c;
				c = temp;
			}
			if (x == 1)
				cout << "Case #" << casenum << ": GABRIEL" << endl;
			else if (x == 2)
				cout << "Case #" << casenum << ": GABRIEL" << endl;
			else if (x == 3)
			{
				if (three[r][c] == 0)
					cout << "Case #" << casenum << ": RICHARD" << endl;
				else
					cout << "Case #" << casenum << ": GABRIEL" << endl;
			}
			else if (x == 4)
			{
				if (four[r][c] == 0)
					cout << "Case #" << casenum << ": RICHARD" << endl;
				else
					cout << "Case #" << casenum << ": GABRIEL" << endl;
			}
		}
	}
}
