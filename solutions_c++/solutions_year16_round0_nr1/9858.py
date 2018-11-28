#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <tuple>
#include <map>
#include <unordered_map>
#include <set>
#include <iostream>

using namespace std;
int n;
int main()
{
	int tc;
	cin >> tc;


	for(int j=1; j<=tc; j++)
	{
		int n = 2;
		cin >> n;
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", j);
			continue;
		}
		int making[10] = {0,};
		for(int i=1; ;i++)
		{
			int s = n * i;
			while(s)
			{
				making[s % 10] = 1;
				s /= 10;
			}
			//if(i % 50 == 0)
			{
				bool allMaking = true;
				for(int j=0; j<10; j++)
				{
					if(making[j] == 0)
					{
						allMaking = false;
						break;
					}
				}

				if(allMaking)
				{
					printf("Case #%d: %d\n", j, n*i);
					//cout << n*i << endl;
					break;
				}

			}

		}
	}
	//while(true)
	{
	}

	return 0;
}
