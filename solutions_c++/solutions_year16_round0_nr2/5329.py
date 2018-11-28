#include<iostream>
#include<stdio.h>
#include <string.h>
#define allplus 1
using namespace std;

int main()
{
	int test;
	scanf("%d", &test);
	for(int t=0;t<test;t++)
	{
		char str[100];
		scanf("%s", str);
		int strlength = strlen(str);
		int count = 0;
		int flag = 0;
		while(flag!=1)
		{
			char top = str[0];
			int currentLength = 0;
			for(int j=0;j<strlength;j++)
			{
				if(str[j] == top)
				{
					currentLength++;
					if(top == '+')
						str[j] = '-';
					else
						str[j] = '+';
				}
				else if(str[j]!=top)
				{
					break;
				}
			}
			if((currentLength == strlength)&&(top == '+'))
				flag = 1;
			else{
				flag = 0;
				count++;
			}
		}
		printf("Case #%d: %d\n",t+1, count);
	}
return 0;
}

