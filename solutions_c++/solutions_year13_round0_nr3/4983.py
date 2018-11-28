#include<fstream.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<iomanip.h>
#include<ctype.h>
#include<process.h>
#include<stdio.h>
#include<stdlib.h>
#include<iostream.h>
int pal(int n)
{
int c=n,r=0,rev=0;
for(;c!=0;)
{r=c%10;
rev=rev*10+r;
c=c/10;
}

if(rev==n)

	{ c=sqrt(n),r=0,rev=0;
	for(;c!=0;)
		{r=c%10;
		rev=rev*10+r;
		c=c/10;
		}
	if((sqrt(n))==rev)
	return 1;
	else
	return 0;
	}
else
return 0;
}

//**********************************************************//

int first(int s,int e)
{
 int count=0;
 for(int i=s;i<=e;i++)
{ int j=pal(i);
 if(j==1)
 ++count;
 else
 count=count;
}
return count;
}

//*********************************************************//

void main()
{clrscr();


int num,a[100][2],b[100];
cin>>num;
for(int i=0;i<num;i++)
for(int j=0;j<2;j++)
cin>>a[i][j];
int k=0;



for(i=0;i<num;i++)
b[k++]=first(a[i][0],a[i][1]);

for(j=0;j<k;j++)
cout<<"case #"<<j+1<<":"<<b[j]<<endl;


getch();
}