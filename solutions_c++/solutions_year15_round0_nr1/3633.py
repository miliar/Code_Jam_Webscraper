#include <iostream>
#include <fstream>

#define inf 1000000000

using namespace std;

long long n, m, s, t, ans = 0,k;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output2.txt");

	cin >> t;
	for (short i = 0; i < t; i++)
	{
		char c;
		cin >> k;
		short r = 0, s = 0;
		for (short i = 0; i <= k; i++)
		{
			cin >> c;
			if (s < i && c != '0')
			{
				r += (i - s);
				s += (i - s) + (c - '0');
			}
			else
			{
				s += (c - '0');
			}
		}
		cout << "Case #" << i + 1 << ": " << r << "\n";
	}
	//system("pause");
}