#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>
void main()
{

	unsigned long long int a,b,c,d,y,t,compare,banyaknya;
	//int t,compare,banyaknya;
	char buffer[30],rev[30];
	scanf("%lli",&t);

	for(int n=1;n<=t;n++)
	{
		banyaknya=0;
		scanf("%lli %lli",&a,&b);
		c=sqrt(a);
		d=sqrt(b);
		for(unsigned long long int x=c;x<=d;x++)
		{
			sprintf(buffer,"%lli",x);
			strcpy(rev,buffer);
			strrev(rev);
			compare=strcmp(buffer,rev);
			if(compare==0)
			{
				y=x*x;
				sprintf(buffer,"%lli",y);
				strcpy(rev,buffer);
				strrev(rev);
				compare=strcmp(buffer,rev);
				//printf("buffer=%s rev=%s\n",buffer,rev);
				//printf("%i\n",compare);
				if(compare==0 && y>=a && y<=b)
				{
					banyaknya++;
				}
			}
		}
		printf("Case #%i: %lli\n",n,banyaknya);
	}
	//getch();
}