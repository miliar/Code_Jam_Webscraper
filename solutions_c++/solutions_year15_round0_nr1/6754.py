#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int cti(char x)
{
	return x - '0';
}

int main()
{
	int tt, hi;
	cin >> tt;
	string s;
	
	for(int t = 1; t <= tt; t++)
	{
		cin >> hi >> s;
		
		int cnt = 0, sf = cti(s[0]), x;
		
		for(int i = 1; i < (int)s.size(); i++)
		{
			x = cti(s[i]);
			
			if(x == 0)
				continue;
			else 
			{
				if(sf < i)
				{
					cnt += abs(sf - i);
					sf += abs(sf - i);
				}
			}
			sf += x;
		}
				
		cout << "Case #" << t << ": " << cnt << '\n';
	}
	return 0;
}
