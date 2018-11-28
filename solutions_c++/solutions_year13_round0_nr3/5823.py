
#include <stdio.h>
#include<math.h>
long count=0;
void pall(long i)
{
long rem,sum=0,temp;
temp=i;
while(i)
{
rem=i%10;
sum=(sum*10)+rem;
i=i/10;
if (temp==sum)
count++;
}

}
void pal(long i)
{
long rem,sum=0,temp;
temp=i;
while(i)
{
rem=i%10;
sum=(sum*10)+rem;
i=i/10;
}
if(temp==sum)
{
float b=sqrt(temp);
long c=sqrt(temp);
if(b==c)
pall(c);

}
}
int main()
{
freopen("A.txt","r",stdin);
freopen("ap.txt","w",stdout);
long beg,end,i,t;
scanf("%d",&t);
for(int j=0;j<t;j++)
{
    count=0;
scanf("%d%d",&beg,&end);
for(i=beg;i<=end;i++)
pal(i);
printf("Case #%d: %d\n",j+1,count);

}
}
