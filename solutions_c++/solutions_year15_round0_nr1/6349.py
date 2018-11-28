#include <iostream>
using namespace std;

#define SIZE 1001 

int main()
{
	int tc;
	char ch;
	cin >> tc;
	int invite[101];
	int s[SIZE];
	int a[SIZE];
	for (int t = 0; t < tc; ++t)
	{
		int smax;
		cin >> smax;
		int audSum = 0;
		invite[t] = 0;
		for (int i = 0; i <= smax; ++i)
		{
			cin >> ch;
			s[i] = ch - '0';
			a[i] = 0;
		}
		a[0] = a[1] = s[0];
		for (int i = 2; i <= smax; ++i)
		{
			a[i] = a[i-1] + s[i-1];
		}
		
		for (int i = 1; i <= smax; ++i)
		{
			int needed = (i > a[i]) ? 1 : 0;
			if (needed)
			{
				invite[t]++;
				for (int k = i + 1; k <= smax;k++)
					a[k]++;
			}
			
		}
	}
	for (int i = 0; i < tc; ++i)
		cout << "Case #" << (i+1) << ": " << invite[i] <<endl;
	
	return 0;
}
