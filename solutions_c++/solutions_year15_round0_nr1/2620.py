#include <stdio.h>
#include <string>

using namespace std;

int main()
{
	int T,c = 1;
	scanf("%d",&T);
	while(T--)
	{
		int n;
		int current = 0;
		int needed = 0;
		char buf[1002];
		scanf("%d%s",&n,buf);

		for(int i=0;i<n+1;i++)
		{
			if(i <= current)
			{
				current += buf[i] - '0';
			}
			else
			{
				if(buf[i] != '0')
				{
					needed += i - current;
					current += buf[i] - '0' + i - current;
				}
			}
		}

		printf("Case #%d: %d\n",c++,needed);
	}
	return 0;
}