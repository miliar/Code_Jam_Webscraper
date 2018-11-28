#include "stdio.h"
#include <list>
#include "string.h"
#include <string>
using namespace std;
     
list<long long> mylist;
list<long long>::iterator iter;
int main()
{
	long long t,i,a,b,c;
	void fairnsq();
	fairnsq();
	scanf("%lld",&t);
	for(i=0;i<t;i++)
	{
		scanf("%lld %lld",&a,&b);	
		c=0;
		for(iter=mylist.begin();iter != mylist.end(); iter++)
		{
			if(*iter >= a && *iter <= b)
				c++;
		}
		printf("Case #%lld: %lld\n",(i+1),c);
	}
	return 0;
}
void fairnsq()
{
	long long i,l,j,s;
	char x[20],y[20];
	string x1,y1;
	for(i=0;i<=10000000;i++)
	{
		sprintf(x, "%lld", i);
		l=strlen(x)-1;
		for(j=l;j>=0;j--)
		{
			y[l-j]=x[j];			
		}
		x1=x;
		y1=y;
		if(x1.compare(y1) == 0)
		{
			s=i*i;
			sprintf(x, "%lld", s);
			l=strlen(x)-1;
			for(j=l;j>=0;j--)
			{
				y[l-j]=x[j];			
			}
			x1=x;
			y1=y;
			if(x1.compare(y1) == 0)
			{
				mylist.push_back(s);	
			}
		}
		for(j=0;j<20;j++)
		{
			x[j]='\0';
			y[j]='\0';
		}
	}
}
