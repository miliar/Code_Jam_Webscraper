#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
char s[250];

int main()
{
	int tc;
	while(scanf("%d",&tc)==1)
	{
		for(int i=1;i<=tc;++i)
		{
			memset(s,0,sizeof(s));
			scanf("%s",s);
			
			int countt=0;

			if(strlen(s) == 1)
			{
				if(s[0]=='-')
					printf("Case #%d: 1\n",i);
				else printf("Case #%d: 0\n",i);
				continue;
			}

			for(int j=0;j<strlen(s)-1;++j)
			{
				char c[250];
				memset(c,0,sizeof(c));

				if(s[j] != s[j+1])
				{			
					for(int k=0;k<j+1;++k)
						c[k]=s[k];
					for(int k=strlen(c)-1,y=0;k>=0;--k,++y)
					{
						if(c[k]=='-')
							s[y]='+';
						else
							s[y]='-';
					}
					++countt;
					j=0;
				}
			}
			if(s[0]=='-')
				++countt;
			
			printf("Case #%d: %d\n",i,countt);
		}
	}
}
