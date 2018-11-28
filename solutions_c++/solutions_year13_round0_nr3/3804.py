#include <stdio.h>
//#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
bool perfsquare( int a)
{
bool flag=0;
for(int i=1; i<=31; i++)
{
if(i*i==a)
{
flag=1;
break;
}
}

return flag;
}
bool pal(int a)
{
if(a==10 || a==1000)
return 0;

if(a/10==0)
return 1;

int b[3];
b[0]=a%10;
a=a/10;

b[1]=a%10;
a=a/10;

if(a==0)
{
if(b[0]==b[1])
return 1;
else return 0;
}

else
{
b[2]=a%10;
a=a/10;
if(b[0]==b[2])
return 1;
else return 0;
}
}
main()
{
int test;
//printf("enter the no of test cases=>");
FILE *file, *out;
file=fopen("inputashu.txt", "r");
out=fopen("outputashu.txt", "w");
fscanf(file,"%d", &test);
int a,b;
for(int t=1; t<=test; t++)
{
//printf("enter A=");
fscanf(file,"%d", &a);

//printf("enter B=");
fscanf(file,"%d", &b);

bool x=perfsquare(a);
//bool y=perfsquare(b);

int i, j;
if(x==1)
i=sqrt(a);
else
i= sqrt(a)+1;

//if(y==1)
j=sqrt(b);
//else
//j= sqrt(b)+1;

int count=0;
for(int z=i; z<=j; z++)
{
if( pal(z))
{
if( pal(z*z))
count=count+1;
}
}
fprintf(out,"Case #%d: %d\n", t, count);
}



//getch();
}
