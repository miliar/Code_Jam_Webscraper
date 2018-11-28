#include<stdio.h>

int main()
{
	int n;
	scanf("%d",&n);
	int casenum=1;
	while(n--)
	{
		int k;
		scanf("%d",&k);
		char str[k+1];
		scanf("%s",&str);
		int answer=0,current=str[0]-'0';
		for(int i=1;i<k+1;i++)
			{
				//printf("%d %d\n", answer, current);
				if(str[i]!='0' and i > current)
					{
					answer += i-current;
					current += (i-current);
					}
				current += (str[i]-'0');
				
			}
		printf("Case #%d: %d\n", casenum ,answer);
		casenum++;
	}
	return 0;
}
