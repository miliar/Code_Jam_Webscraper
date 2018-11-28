#include <stdio.h>
#include <conio.h>
#include <string.h>

int main()
{
	int T,cas=1;
	scanf("%i\n",&T);
	while(T--)
	{
		char stack[102],current;
		int panjang=0,count=0,i;
		scanf("%s\n",stack);
		panjang=strlen(stack);
		if(stack[0]=='-')
		{
			current='-';
			count++;
		}
		else current='+';
		for (i=1;i<panjang;i++)
		{
			if(current=='+'&&stack[i]=='+');
			else if(current=='-'&&stack[i]=='+')current='+';
			else if(current=='+'&&stack[i]=='-')
			{
				current='-';
				count=count+2;
			}
		}
		printf("Case #%i: %i\n",cas++,count);
	}
}
