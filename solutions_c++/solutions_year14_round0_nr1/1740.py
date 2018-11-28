#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, ans, num, caseno = 1;
	cin >> t;

	while(t--)
	{
		int grid[17] = {0};

		// answer 1
		cin >> ans;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> num;
				if(i+1 == ans)
					grid[num]++;
			}
		}

		// answer 2
		cin >> ans;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> num;
				if(i+1 == ans)
					grid[num]++;
			}
		}

		int pos = 0;
		for(int i=0; i<17; i++)
			if(grid[i] == 2)
			{
				pos++;
				ans = i;
			}
		if(pos == 1)
			cout << "Case #" << caseno << ": " << ans << endl;
		else if(pos > 1)
			cout << "Case #" << caseno << ": Bad magician!" << endl;
		else
			cout << "Case #" << caseno << ": Volunteer cheated!" << endl;
		caseno++;
	}
	return 0;
}