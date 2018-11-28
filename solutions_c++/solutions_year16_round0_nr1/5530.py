#include <iostream>
#include <vector>
#include <sstream>
#include <cstdio>

using namespace std;

int main (void)
{
	int t;

	cin >> t;

	int c = 1;

	while (t --)
	{
		int n;

		cin >> n;

		if (n == 0)
			cout << "Case #" << c ++ << ": INSOMNIA\n";
		else
		{
			vector<int> digitis;
			digitis.assign(10, 0);
			int contDigitis = 0;
			int m = 1;
			int x;

			while (contDigitis < 10)
			{
				x = n * m;
				stringstream convert;
				convert << x;

				string number = convert.str();

				for (int i = 0; i < number.size(); i ++)
				{
					if (digitis[(number[i] - '0')] == 0)
					{
						digitis[(number[i] - '0')] = 1;
						contDigitis ++;
					}
				}

				m ++;
			}

			cout << "Case #" << c++ << ": " << x << '\n';
		} 
	}
	return 0;
}