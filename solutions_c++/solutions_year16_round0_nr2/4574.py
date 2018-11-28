#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	int test = 0;
	while(scanf("%d",&test) != EOF)
	{
		char s[200];
		int break_point[200];
		for(int i=0;i<test;++i)
		{	
			memset(s,0,sizeof(s));
			scanf("%s",&s);
			int tmp = 0,answer = 0;

			if(strlen(s) > 1)
			{
				for(int j=1;j<strlen(s);++j)
				{
					if(s[j] != s[j-1])
					{
						char temp[200];
						for(int k=j-1;k>=0;k--)
						{
							if(s[k] == '+')
								temp[j-1-k] = '-';
							else
								temp[j-1-k] = '+';
						}
						for(int k=0;k<j;++k)
						{
							s[k] = temp[k];
						}
						answer++;
						j = 0;
					}
				}
				if(s[0] == '-')
					answer++;
			}
			else
			{
				if(s[0] == '+')
					answer = 0;
				else
					answer = 1;
			}

			printf("Case #%d: %d\n",i+1,answer);
		}
	}
	return 0;
}
