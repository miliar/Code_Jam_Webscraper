#include<stdio.h>
#include<conio.h>
#include<math.h>
int pen(long int n)
{
int temp,rem,reverse=0;
temp=n;
while(temp!=0)
{
rem=temp%10;
reverse=reverse*10+rem;
temp/=10;
}
if(reverse==n)
return 1;
return 0;
}
main()
{
FILE *fp,*op;
clrscr();
fp=fopen("input.txt","r");
op=fopen("output.txt","w");
int T,set=0;
fscanf(fp,"%d",&T);
for(set=0;set<T;set++)
{

int i,y=0;
float u;
long int start,end,start1,end1,j;
fscanf(fp,"%ld %ld",&start,&end);
end1=sqrt(end);
start1=sqrt(start);
u=sqrt(start);
//printf("%ld %ld \n",end1,start1);
if(u==start1);
else start1++;
for(;start1<=end1;start1++)
{

i=pen(start1);
if(i==1)
{j=start1*start1;
i=pen(j);
if(i==1)y++;
}
}
printf("%d",y);

	       fprintf(op,"Case #%d: %d",set,y);
}
getch();
fclose(fp);
fclose(op);
}