#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<functional>
#include<numeric>

using namespace std;

int main()
{
	int cases;
	cin >> cases;

	for(int i=1; i<=cases; i++)
	{
		string pancake;
		cin >> pancake;

		string goal(pancake.size(), '+');

		int flips = 0;
		while(pancake != goal)
		{
			size_t flip = pancake.find_last_of('-') + 1;
			size_t plus = 0;

			if(pancake[plus] == '+')
			{
				size_t plusFlip = 0;
				while(pancake[plus++] == '+')
				{
					plusFlip++;
				}
				flip = plusFlip;
			}
			reverse(pancake.begin(), pancake.begin() + flip);
			for(size_t j=0; j<flip; j++)
			{
				if(pancake[j] == '-')
				{
					pancake[j] = '+';
				}
				else
				{
					pancake[j] = '-';
				}
			}
//			cerr << "Pancake: " << pancake << " last at: " << flip << endl;
			flips++;
		}


		cout << "Case #" << i << ": " << flips << endl;
	}

	return 0;
}
