#include <bits/stdc++.h>

using namespace std;

int main()
{
	int testcases;
	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		string x;
		cin >> x;

		int flips = 0;
		int limit = x.length();
		while(limit > 0 && x[limit - 1] == '+')
			limit--;
		do
		{
			// cout << "\t" << x << endl;

			int temp = 0;
			while(x[temp] == '+' && temp < limit)
				temp++;
			if(temp == limit)
				break;

			// cout << "\t" << temp << endl;

			if(temp != 0)
				flips++;
			for(int j = 0; j < temp; j++)
				x[j] = '-';

			while(x[temp] == '-')
				temp++;

			reverse(x.begin(), x.begin() + limit);

			flips++;
			for(int j = 0; j < limit; j++)
				x[j] = ((x[j] == '+')?'-':'+');

			limit -= temp;
			// cout << "\t" << x << "\t" << limit << endl;
		}
		while(limit != 0);

		cout << "Case #" << i + 1 << ": " << flips << endl;
	}
}