#include <iostream>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	const int DIGITS_COUNT = 10;
	int t, i, n, j, count, temp1, temp2;
	bool d[DIGITS_COUNT];
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> n;
		if(n == 0)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else
		{
			for(j = 0; j < DIGITS_COUNT; j++)
				d[j] = false;
			count = 0;
			temp1 = 0;
			do
			{
				temp1 += n;
				temp2 = temp1;
				while(temp2 != 0)
				{
					if(!d[temp2 % 10])
					{
						d[temp2 % 10] = true;
						count++;
					}
					temp2 /= 10;
				}
			}
			while(count < DIGITS_COUNT);
			cout << "Case #" << i << ": " << temp1 << endl;
		}
	}
	return 0;
}

