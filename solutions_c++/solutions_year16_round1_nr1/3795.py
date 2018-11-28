#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	int test_case;
	char s[1001];
	int po[1001];
	int len;
	scanf("%d", &test_case);
	for(int i=1;i<=test_case;i++)
	{
		
		scanf("%s", s);
		len=strlen(s);
		po[0]=1;
		char start=s[0];
		for(int i=1;i<len;i++)
		{
			if(s[i]>=start)
			{
				po[i]=1;
				start=s[i];
			}
			else
				po[i]=0;
		}
		
		printf("Case #%d: ", i);
		for(int i=len-1;i>=0;i--)
		{
			if(po[i]==1)
				printf("%c", s[i]);
		}
		for(int i=0;i<len;i++)
		{
			if(po[i]==0)
				printf("%c", s[i]);
		}
		printf("\n");
	}
	return 0;
}
