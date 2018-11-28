#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
int main()
{
	
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int r1;
		cin >> r1;
		set<int> row1;
		int dummy;
		for(int a = 0; a < 4; a++)
		{
			if(a == r1-1)
			{
				for(int b = 0; b < 4; b++)
				{
					int x;
					cin >> x;
					row1.insert(x);
				}				
			}
			else
			{
				cin >> dummy >> dummy >> dummy >> dummy;
			}
		}

		int r2;
		cin >> r2;
		set<int> row2;
		for(int a = 0; a < 4; a++)
		{
			if(a == r2-1)
			{
				for(int b = 0; b < 4; b++)
				{
					int x;
					cin >> x;
					row2.insert(x);
				}				
			}
			else
			{
				cin >> dummy >> dummy >> dummy >> dummy;
			}
		}
		vector<int> intersection(4);
		vector<int>::iterator it = set_intersection (row1.begin(), row1.end(), row2.begin(), row2.end(), intersection.begin());                                               
		intersection.resize(it-intersection.begin());
		cout << "Case #" << i+1 << ": ";
		int n = (int)intersection.size();
		if(n == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if(n == 1)
		{
			cout << intersection[0] << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
		}
	}
}