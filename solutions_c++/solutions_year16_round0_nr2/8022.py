#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
	//freopen("result.txt","w",stdout);
	int cas;
	scanf("%d ",&cas);
	for(int i=0;i<cas;i++)
	{
		char s[120];
		gets(s);
		int move=0;
		int len=strlen(s);
		for(int j=0;j<len-1;j++)
		{
			if(s[j]!=s[j+1])
			{
				for(int k=0;k<=j;k++)
					s[k]=s[j+1];
				move++;
			}
		}
		if(s[0]=='-')
			move++;
		printf("Case #%d: %d\n",i+1,move);
	}
	return 0;
}
