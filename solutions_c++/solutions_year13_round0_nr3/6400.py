#include<stdio.h>
#include<math.h>
#include<conio.h>
void main()
{
	int p,q,i,j,k,n;
	clrscr();
	scanf("%d",&n);
	FILE *f1=fopen("def.txt","r");
	for(i=0;i<n;i++)
	{
		int count=0;
		fscanf(f1,"%d",&p);
		//getc(f1);
		fscanf(f1,"%d",&q);
		//getc(f1);
		//printf("p %d q %d",p,q);
		for(int m=p;m<=q;m++)
		{
		//printf("\n");
			j=sqrt(m);
		     //	printf("%d\n\n",j);
			if(m==j*j)
			{

				int x=m%10;

				int y=m;
				y=y/10;
				if(y>0)
				{
				x=x*10;
				x=x+(y%10);
				//if(y>0)
				y=y/10;
				if(y>0){
				x=x*10;
				x=x+(y%10);
				//if(y>0)
				//{
				y=y/10;
				if(y>0){
				x=x*10;
				x=x+(y%10);
				}}}
				//printf("%d ",x);
				if(x==m)
				{
				int x=j%10;
				int y=j;
				y=y/10;
				if(y>0)
				{
				x=x*10;
				x=x+(y%10);
				y=y/10;
				if(y>0){
				x=x*10;
				x=x+(y%10);
				//if(y>0)
				//{
				y=y/10;
				if(y>0){
				x=x*10;
				x=x+(y%10);
				}}}
				//printf("%d ",x);
				if(j==x)
				count++;
				}

			}
		}
		printf("Case #%d: %d\n",i+1,count);
		getch();
	}
	getch();
}
				//fscanf
