#include <iostream>
#include<algorithm>
#include<vector>
using namespace std;

string fun(int x)
{
	if (x == 0) return "ZERO";
	if (x == 1) return "ONE";
	if (x == 2) return "TWO";
	if (x == 3) return "THREE";
	if (x == 4) return "FOUR";
	if (x == 5) return "FIVE";
	if (x == 6) return "SIX";
	if (x == 7) return "SEVEN";
	if (x == 8) return "EIGHT";
	if (x == 9) return "NINE";
}

bool inc(int x)
{
	int lastdig = 20;
	while (x > 0)
	{
		if (x % 10 > lastdig)
			return false;
		lastdig = x % 10;
		x /= 10;
	}
	return true;
}

int main()
{
	ios_base::sync_with_stdio(0);

	int tes;
	cin >> tes;
	for (int t = 1; t <= tes; t++)
	{
		string a;
		cin >> a;
		sort(a.begin(), a.end());
		
//		cout << a << " = a\n";

		bool todo = true;

		for (int zeros = 0; zeros <= 6 and todo; zeros++)
		{
			string zerosstr = "";
			for (int k = 0; k < zeros; k++)
				zerosstr += fun(0);
			for (int i = 0; i <= 1000000 and todo; i++)
			{
				if (!inc(i)) continue;
			
				string b = zerosstr;
				int num = i;
				while (num > 0)
				{
					b += fun(num % 10);
					num /= 10;
				}
				sort(b.begin(), b.end());
				
//				cout << "zeros, i = " << zeros << ", " << i << "\n";
//				cout << b << " = b\n";
				
				if (a == b)
				{
					todo = false;
					cout << "Case #" << t << ": ";
					for (int k = 0; k < zeros; k++)
						cout << 0;
					if (i != 0) cout << i << "\n";
					else cout << "\n";
				}
			}
		}
		

	}






	return 0;
}
