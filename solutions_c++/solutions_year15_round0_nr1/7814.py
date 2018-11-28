//in the name of God

#include <iostream>
#include <string>
using namespace std;

long long shy[1111];

int main()
{
	int t;
	cin >> t;
	for(int test = 1; test <=t; test++)
	{
		int n;
		string s;
		cin >> n >> s;
		
		for(int i=0; i<1111; i++)
			shy[i] = 0;

		for(int i=0; i<=n; i++)
			shy[i] = s[i]-'0';

		long long result = 0;
		long long tot = 0;

		for(long long i=0; i<=n; i++)
		{
			if(shy[i] == 0)
				continue;

			if(tot >= i)
			{
				tot += shy[i];
				continue;
			}

			result += i-tot;
			tot += i-tot+shy[i];
		}

		cout << "Case #" << test << ": " << result << endl;
	}

	return 0;
}