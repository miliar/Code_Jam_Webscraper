#include <iostream>
#include<stdio.h>
using namespace std;

int main() 
{
int T,i,k,count,set;
char str[102];
scanf("%d",&T);
for(i=1;i<=T;i++)
{
scanf("%s",str);
count=0;
set=1;
k=1;
if(str[0]=='-')
{
count=1;
set=0;
}
while(str[k]!='\0')
{
if(str[k]=='-'&&set==1)
{
count=count+2;
set=0;
}
if(str[k]=='+')
{
set=1;
}
k++;
}
printf("Case #%d: %d\n",i,count);
    
}

	// your code goes here
	return 0;
}
