#include <iostream>
#include <vector>

using namespace std;


bool found(vector<bool> & seen)
{
	for (int i = 0; i < 10; i++)
	{
		if (!seen[i])
			return false;
	}

	return true;
}

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 1; i <= numCases; i++)
	{
		int num;
		cin >> num;

		cout << "Case #" << i << ": ";

		if (num == 0)
		{
			cout << "INSOMNIA\n";
		}
		else 
		{
			vector<bool> seen(10, false);

			for (int j = 1; ; j++)
			{
				int num2 = num * j;
				for ( ; num2 > 0; num2 /= 10)
				{
					seen[num2 % 10] = true;
				}

				if (found(seen))
				{
					cout << num * j << endl;
					break;
				}
			}
		}
	}
	return 0;
}
