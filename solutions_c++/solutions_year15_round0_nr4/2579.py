#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<iostream>
#include<utility>
#define MOD 1000000009
#define LL long long int
#define gc getchar
#define pc putchar
#define pb push_back
#define mp make_pair
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define tr(container, it) \
for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end())
using namespace std;
int compare(const void *a,const void *b)
{
	return (*(int *)a-*(int *)b);


}
inline LL myscanf()
{
LL n=0;
int ch=gc();
while( ch < '0' || ch > '9' )
{
ch=gc();
}
while( ch >= '0' && ch <= '9' )
{
n = (n<<3)+(n<<1) + ch-'0';
ch=gc();
}
return n;
}
inline void myprintf(LL n)
{
	LL a[20];
	LL i=19,j,k;
	for(;;)
	{
		k=n%10;
		n=(n-k)/10;
		a[i--]=k;
		if(n==0)
		break;
	}
	for(j=i+1;j<=19;j++)
	pc(a[j]+'0');

	pc('\n');
}
int main()
{
int t,i,r,c,temp,x,min_1,x_cord,y_cord;
bool flag;
t=myscanf();
for(i=1;i<=t;i++)
{
	x=myscanf();
	r=myscanf();
	c=myscanf();
	if(x==1)
	{
		flag=true;
	}
	else
	{
		x_cord=min(r,c);
		y_cord=max(r,c);
		if(x_cord==1)
		{
			if(y_cord==1)
			{
				if(x==1)flag=true;
				else
				flag=false;
				
			}
			else if(y_cord==2)
			{
				if(x==1 || x==2)flag=true;
				else flag=false;
				
				
			}
			else if(y_cord==3)
			{
				if(x==1)flag=true;
				else
				flag=false;
				
			}
			else
			{
				if(x==1 || x==2)flag=true;
				else flag=false;
				
			}
			
			
		}
		else if(x_cord==2)
		{
			
			if(y_cord==2)
			{
				if(x==1 || x==2)flag=true;
				else flag=false;
				
				
			}
			else if(y_cord==3)
			{
				if(x==4)flag=false;
				else
				flag=true;;
				
			}
			else
			{
				if(x==1 || x==2)flag=true;
				else flag=false;
				
			}
			
			
		}
		else if(x_cord==3)
		{
			if(y_cord==3)
			{
				if(x==1 || x==3)flag=true;
				else
				flag=false;
				
			}
			else
			{
				flag=true;
				
			}
			
		}
		else
		{
			if(y_cord==4)
			{
				if(x==1 || x==2 || x==4)flag=true;
				else
				flag=false;
			}
			
		}
	}
	if(flag)
	printf("Case #%d: GABRIEL\n",i);
	else
	printf("Case #%d: RICHARD\n",i);
	
	
}

return 0;
}

