#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	int r;
	int c;
	int a;
	
	string s;
	int S;
	
	cin >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		r = 0;
		
		cin >> S >> s;
		
		c = s[0] - '0';
		
		for (int j = 1; j <= S; ++j)
		{
			a = s[j] - '0';
			
			if (c < j)
			{
				r += j-c;
				c = j+a;
			}
			else
			{
				c += a;
			}
		}
		
		cout << "Case #" << i << ": " << r << endl;
	}
}
