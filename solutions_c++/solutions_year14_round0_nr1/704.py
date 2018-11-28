#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for( int loop=0; loop<t; loop++ )
	{	
		int candidate[4];
		int row, input;
		int ans = -1, ans_count = 0;

		cin >> row;
		for (int yloop = 0; yloop < 4; yloop++)
			for (int xloop = 0; xloop < 4; xloop++)
			{
				cin >> input;
				if (yloop == row-1) candidate[xloop] = input;
			}

		cin >> row;
		for (int yloop = 0; yloop < 4; yloop++)
			for (int xloop = 0; xloop < 4; xloop++)
			{
				cin >> input;
				if (yloop == row-1)
				{
					if (input == candidate[0] || input == candidate[1] || input == candidate[2] || input == candidate[3])
					{
						ans = input;
						ans_count++;
					}
				}
			}

		if (ans_count == 1) cout << "Case #" << loop+1 << ": " << ans << endl;
		else if (ans_count > 1) cout << "Case #" << loop + 1 << ": Bad magician!" << endl;
		else cout << "Case #" << loop + 1 << ": Volunteer cheated!" << endl;
	}
	return 0;
}