#include <iostream>
#include <string>

using namespace std;

int main() 
{
	int x,y,n,t,i,j;

	cin >> t;
	for (int tt = 0; tt < t; ++tt)
	{
		int len;
		cin >> len;
		string s;
		cin >> s;
		j = 0;
		n = 0;
		for (i = 0; i < len + 1; ++i)
		{
			if (i > j)
			{
				n += (i - j);
				j = i;
			}
			x = s[i] - '0';
			j += x;
		}
		cout << "Case #" << tt + 1 << ": " << n << endl;
	}
	return 0;
}