#include<stdio.h>

void append(char result[], char strChar, int size)
{
	int i=0;
	for(i=size;i>=1;i--)
	{
		result[i] =  result[i-1];
	}
	result[0] = strChar;
}
int main()
{
	int t = 0,i,len;
	char str[1000],result[1000];
	scanf("%d",&t);
	len =1;
	while(len <= t)
	{
	scanf("%s",str);
	result[0] =  str[0];
	for(i= 1;i<str[i] != '\0';i++)
	{
		if(str[i] >=  result[0])
		{
			append(result, str[i],i);
		}
		else
		 {
		 	result[i] = str[i];
		 } 
	}
	result[i] ='\0';
	printf("Case #%d: ",len);
	printf("%s\n",result);
	
	len++;
    }
	return 0;
}
