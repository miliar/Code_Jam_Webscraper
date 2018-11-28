#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 1001

int main()
{
	int T;
	cin >> T;

	for(int Case=1; Case<=T; Case++)
	{
		int n;
		char data[MAXN+1];
		
		cin >> n >> data;

		int aud = 0;
		int result = 0;

		for(int i=0; i<=n; i++)
		{
			if(data[i] > '0' && aud < i)
			{
				result += i - aud;
				aud += i - aud;
			}
			aud += data[i] - '0';
		}

		cout << "Case #" << Case << ": " << result << endl;
	}

	return 0;
}