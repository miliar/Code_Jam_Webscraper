#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t)
	{
		ll N;
		cin >> N;
		ll res;
		if (N == 0)
		{
			res = -1;
		}
		else
		{
			vector<int> f(11,0);
			int found = 0;
			ll B = N;
			bool done = false;
			while(found < 10)
			{
				ll _N = N;
				while (_N != 0)
				{
					if(f[_N%10] == 0)
					{
						found ++;
						f[_N%10] = 1;
						if(found == 10)
						{
							done = true;
							break;
						}
					}
					_N /= 10;
				}
				if(done)
				{
					break;
				}
				N += B;
			}
			res = N;
		}

		if (res == -1)
		{
			cout << "Case #" << t << ": INSOMNIA\n";	
		}
		else
		{
			cout << "Case #" << t << ": " << res << "\n";
		}
	}


	return 0;
}