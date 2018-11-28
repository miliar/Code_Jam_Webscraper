#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int nCases;
	cin >> nCases;
	for(int t = 1; t <= nCases; t++)
	{
		int r1, r2;
		cin >> r1;
		bool pos[20];
		memset(pos, false, sizeof pos);
		for(int r = 1; r <= 4; r++)
		{
			for(int c = 1; c <= 4; c++)
			{
				int n;
				cin >> n;
				if(r != r1) continue;
				pos[n] = true;
			}
		}

		cin >> r2;
		for(int r = 1; r <= 4; r++)
		{
			for(int c = 1; c <= 4; c++)
			{
				int n; 
				cin >> n;
				if(r == r2)
				{
					if(pos[n])
						pos[n] = true;
				}
				else
				{
					pos[n] = false;
				}
			}
		}

		/*cout << endl <<  "After first run: " << endl;
		for(int i = 0; i < 20; i++)
			cout << pos[i];
		cout << endl;*/

		int count = 0;
		int last = 0;
		for(int i = 0; i < 17; i++)
		{
			if(pos[i])
			{
				count++;
				last = i;
			}
		}

		/*cout << endl << "After second run: " << endl;
		for(int i = 0; i < 20; i++)
			cout << pos[i];
		cout << endl;

		cout << "r1 = " << r1 << "; r2 = " << r2 << endl;*/

		if(count == 0)
			cout << "Case #" << t << ": Volunteer cheated!" << endl;
		else if(count == 1)
			cout << "Case #" << t << ": " << last << endl;
		else
			cout << "Case #" << t << ": Bad magician!" << endl;

	}
}