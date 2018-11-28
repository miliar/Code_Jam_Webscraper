#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
int main()
{
	int t=0,i,top,count,m;
	char array[106];
	cin>>t;
	m=t;
	while(t--)
	{
		scanf("%s",array);
		int len=strlen(array);
		i=len-1;
		top=0;
		count=0;
		while(i>=top)
		{
			if(array[i]=='-')
			{
				count++;
				for(int j=0;j<=i;j++)
				{
					if(array[j]=='-')
					{
						array[j]='+';
					}
					else if(array[j]=='+')
						array[j]='-';
				}
			}
			i--;
		}
		printf("Case #%d: %d\n",m-t,count);
	}
	return 0;
}