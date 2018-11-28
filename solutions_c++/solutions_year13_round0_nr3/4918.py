#include <stdio.h>
#include <math.h>
#include <string.h>

bool palindrome(long long num)
{
	char temp[100];

	sprintf(temp,"%lld",num);

	if (temp[strlen(temp)-1]=='0') return false;
	else
	{
		for (int i=0;i<strlen(temp)/2;i++)
		{
			if (temp[i]!=temp[strlen(temp)-1-i]) return false;
		}
	}

	return true;
}

int main()
{
	int T=0;
	long long a,b,bot,top,count;

	scanf("%d",&T);
	
	for (int i=1;i<=T;i++)
	{
		a=b=count=0;
		scanf("%lld %lld",&a,&b);
		bot = sqrt((double)a);
		top = sqrt((double)b);
		
		if (bot*bot<a) bot++;

		for (int j=bot;j<=top;j++)
		{
			if (palindrome(j))
			{
				if(palindrome(j*j)) count++; 
			}
		}


		printf("Case #%d: %lld\n",i,count);
	}

	return 0;
}