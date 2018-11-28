#define SMALL_DATA
#define LARGE_DATA

#include <stdio.h>
#include <string.h>

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for(int t=0; t<T; t++){
		int maxLev;
		int sumPep = 0;
		int invitePep = 0;

		scanf("%d", &maxLev);

		char str[10001];
		scanf("%s", str);

		for(int i=0; i<=maxLev; i++)
		{
			if(sumPep < i)
			{
				invitePep += i - sumPep;
				//sumPep += i-sumPep;
				str[i] = (str[i]-'0' + (i-sumPep)) + '0';
			}
			sumPep += str[i]-'0';
		}

		printf("Case #%d: %d\n", t+1, invitePep);

	}
	return 0;

}