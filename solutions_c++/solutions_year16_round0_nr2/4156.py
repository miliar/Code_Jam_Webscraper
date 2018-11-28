#include<iostream>
#include<map>
#include<set>
#include<stdio.h>
using namespace std;
int main() 
{
	freopen("B-large.in","r",stdin);  
	freopen("B-large.out","w",stdout); 
	int T;
	scanf("%d",&T);
	getchar();
	int j=1;
	while(T--)
	{
		char s[100+1];
		gets(s);
		char *str=s;
		int sum=0;
		while(*(str+1)!='\0')
		{
			if (*str!=*(str+1))
				sum++;
			str++;
		}
		if(*str!='+')
		sum++;
		printf("Case #%d: %d\n",j++,sum);
		
	}
}
