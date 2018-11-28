#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <map>

using namespace std;

int main()
{
	int T, count, i;
	char pan[110];
	bool happy;

	scanf("%d", &T);

	for(int t = 1; t <= T; ++t)
	{
		scanf("%s", pan);
		count = 0;
		
		while(true)
		{
			happy = true;

			//find lowest upside down
			for(i = (int)strlen(pan)-1; i >= 0; --i)
			{
				if(pan[i] == '-')
				{
					happy = false;
					break;
				}
			}
			
			//turn around
			if(!happy)
			{
				++count;
				for(int j = 0; j <= i; ++j)
				{
					pan[j] = (pan[j] == '-' ? '+' : '-');
				}
			}
			else
			{
				printf("Case #%d: %d\n", t, count);
				break;
			}
			
		}
	}
	return 0;
}