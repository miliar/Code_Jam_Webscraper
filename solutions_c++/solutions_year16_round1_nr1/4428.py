#include<stdio.h>
#include<string.h>
int main(void) {
	// your code goes here
	int t,o=1;
	scanf("%d",&t);
	while(t--)
	{
		char s[1000],c[2000];
		scanf("%s",s);
		int n,i,l=1000,h=1000;
		n=strlen(s);
		c[1000]=s[0];
		for(i=1;i<n;i++)
		{
			if(s[i]>=c[l])
			c[--l]=s[i];
			else
			c[++h]=s[i];
		}
		int m=0;
		for(i=l;i<=h;i++)
		c[m++]=c[i];
		c[h+1]='\0';
		printf("Case #%d: %s\n",o,c);
		o++;
	}
	return 0;
}

