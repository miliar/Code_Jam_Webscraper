#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	int t;
	ifstream fcin("A-large.in");
	ofstream fcout("out1.txt");
	fcin >> t;
	int c = 1;
	while (c <= t)
	{
		int level;
		string s;
		fcin >> level >> s;
		int ans = 0;
		int sum = 0;
		for (int i = 0; i <= level; i++)
		{
			if (sum < i)
			{
				ans += (i - sum);
				sum = i;
			}
			sum += (s[i] - '0');
		}
		fcout << "Case #" << c << ": " << ans << endl;
		c++;
	}
	return 0;
}