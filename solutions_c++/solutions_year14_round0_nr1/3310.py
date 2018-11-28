#include <iostream>
#include <set>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int k=1; k<=T; k++)
	{
		set<int> s;
		s.clear();
		int r, x;
		cin >> r;
		for (int i=1; i<=4; i++)
		{
			if (i==r)
			{
				for (int j=0; j<4; j++)
				{
					cin >> x;
					s.insert(x);
				}
			}
			else
				for (int j=0; j<4; j++)
					cin >> x;
		}
		cin >> r;
		int n = 0, res = 0;
		for (int i=1; i<=4; i++)
		{
			if (i==r)
			{
				for (int j=0; j<4; j++)
				{
					cin >> x;
					if (s.find(x)!=s.end())
					{
						n++;
						res = x;
					}
				}
			}
			else
				for (int j=0; j<4; j++)
					cin >> x;
		}
		if (n==0)
			cout << "Case #" << k << ": Volunteer cheated!" << endl;
		else
			if (n==1)
				cout << "Case #" << k << ": " << res << endl;
			else
				cout << "Case #" << k << ": Bad magician!" << endl;
	}
	return 0;
}