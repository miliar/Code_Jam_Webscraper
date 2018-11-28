#include <stdio.h>
#include <string.h>

using namespace std;

int main(void)
{
	int cases, l = 1;
	scanf("%d", &cases);
	while(cases--)
	{
		int n, sum = 0, answer=0;
		scanf("%d", &n);
		char plateia[n+5];
		scanf("%s", plateia);
		for(int i=0;i<strlen(plateia);i++)
		{
			if((plateia[i] - '0') == 0)continue;
			while(sum<i)
			{
				sum++;
				answer++;
			}
			sum+=(plateia[i]-'0');
		}
		printf("Case #%d: %d\n", l++, answer);
	}
	return 0;
}
