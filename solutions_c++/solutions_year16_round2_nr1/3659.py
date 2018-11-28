#include<stdio.h>
int main(void)
{
	int z=0,w=0,u=0,g=0,x=0,f=0,o=0,v=0,h=0,i=0;
	int a0=0,a1=0,a2=0,a3=0,a4=0,a5=0,a6=0,a7=0,a8=0,a9=0;
	char c[2000];
	int t,len;
	scanf("%d",&t);
	int qi,j;
	for(qi=0;qi<t;qi++)
	{
		z=0,w=0,u=0,g=0,x=0,f=0,o=0,v=0,h=0,i=0;
	a0=0,a1=0,a2=0,a3=0,a4=0,a5=0,a6=0,a7=0,a8=0,a9=0;
		scanf("%s",&c);
		
		for(len=0;c[len]!='\0';++len);
		for(j=0;j<len;j++)
		{
			if(c[j]=='Z')++z;
			if(c[j]=='W')++w;
			if(c[j]=='U')++u;
			if(c[j]=='G')++g;
		if(c[j]=='X')++x;
		if(c[j]=='F')++f;
		if(c[j]=='O')++o;
		if(c[j]=='V')++v;
		if(c[j]=='H')++h;
		if(c[j]=='I')++i;
		}
		printf("Case #%d: ",qi+1);
	a0=z;
	a2=w;
	a4=u;
	a8=g;
	a6=x;
	a5=f-u;
	a1=o-w-u-z;
	a7=v-a5;
	a3=h-g;
	a9=i-g-a5-x;
	for(j=0;j<a0;j++)
	printf("0");
	for(j=0;j<a1;j++)
	printf("1");
	for(j=0;j<a2;j++)
	printf("2");
	for(j=0;j<a3;j++)
	printf("3");
	for(j=0;j<a4;j++)
	printf("4");
	for(j=0;j<a5;j++)
	printf("5");
	for(j=0;j<a6;j++)
	printf("6");
	for(j=0;j<a7;j++)
	printf("7");
	for(j=0;j<a8;j++)
	printf("8");
	for(j=0;j<a9;j++)
	printf("9");
	printf("\n");
	}
	return 0;
	
}
