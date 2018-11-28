#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

string str;
int len;

int main()
{
	int t;
	scanf("%d",&t);
	int case1=1;
	while(t--)
	{
		cin>>str;
		len = str.length();
		char pre = str[0];
		int flips = 0;
		int counter=0;
		for(int i=1;i<len;i++)
		{
			char cur = str[i];
			if(pre!=cur)
			{
				flips++;
			}
			pre = cur;
		}
		if(pre == '-')
			flips++;
		printf("Case #%d: %d\n",case1,flips);
		case1++;
	}
}