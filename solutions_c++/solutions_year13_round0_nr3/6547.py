#include<stdio.h>
#include<math.h>
#include<iostream>
#include<string.h>
using namespace std;

bool ispalindrom(long long int z)
{
	string s="";
	long long int p=z;
	char c;
	int i,flag=0;
	while(p)
	{
	int q=p%10;
	c=q+48;
	s=c+s;
	p=p/10;
	}
for(i=0;i<=(s.length()/2);i++)
{
if(s[i]!=s[s.length()-1-i])
{flag=1;
break;
}
}
if(flag==0)
return true;
return false;

	
}
int main()

{
	int test,counter=1;
	long long int a,b,count,i;
	scanf("%d",&test);
	while(test--)
	{
	count=0;
	scanf("%lld%lld",&a,&b);
	int x=(long long int)sqrt(a);
	int y=(long long int)sqrt(b);
	if(x*x==a)
	i=x;
	else
	i=x+1;
	for(;i<=y;i++)	
	if(ispalindrom(i)&&ispalindrom(i*i))	
	{
	count++;
}
	printf("Case #%d: %d\n",counter,count);
	counter++;
		
	}
	
	
 	return 0;
}

