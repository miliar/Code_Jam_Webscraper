#include <iostream>

using namespace std;

int main(void)
{
	int T, it, changes, i;
	string pancakes;

	while(cin >> T)
	{
		it = 0;
		while(it++ < T)
		{
			cout << "Case #" << it << ": ";
			cin >> pancakes;

			changes = 0;

			// Go to the most bottom sad pancake
			i = pancakes.size() - 1;
			while(i >= 0 && pancakes[i] == '+') i--;

			// All pancackes are happy
			if(i == -1)
			{
				cout << 0 << endl;
				continue;
			}

			changes++;
			i--;

			for(; i >= 0; i--)
			{
				// This is fine, go to next
				if(pancakes[i] == '+')
				{
					if(changes % 2)
					{
						changes++;
					}
				}
				else
				{
					if(changes % 2 == 0)
					{
						changes++;
					}
				}
			}

			cout << changes << endl;
		}
	}

	return 0;
}