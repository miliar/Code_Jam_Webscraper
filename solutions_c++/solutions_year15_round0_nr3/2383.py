#include <stdio.h>
#include <string>
using namespace std;
long long int rsv=0;
char multiply(char a,char b)
{
		
	if(a==b)
	{
		rsv++;
		return '1';
	}
	switch (a)
		{
		case '1':
			{
			
					return b;
			}
		
		case 'i':
			{
				
				if(b=='j')
				return 'k';
				else
				{
						rsv++;
				return 'j';
				}
			}
		case 'j':
			{
					
				if(b=='k')
				return 'i';
				else
				{
					rsv++;
				return 'k';
				}
			
			}
		default:
			{
				if(b=='i')
				return 'j';
				else
				{
					rsv++;
					return 'i';	
				}
			
			}
		}
}
int main()
{
	freopen( "C-smal.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,sum,lol,l,x;
	char b,c;
	char a[10010];
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		rsv=0;sum=0;
		scanf("%lld%lld%s",&l,&x,&a[0]);
		b=a[0];
		for(i=1;;i++)
		{
			if(i==l)
			{
				if(x>1)
				{
					x--;i=0;
				}
				else break;
			}
			rsv=rsv%2;
			if(b=='i'&&rsv==0)
			{
				break;
			}
			b=multiply(b,a[i]);
			
		}
		if(i<l)b=a[i++];
		for(;;i++)
		{
			if(i==l)
			{
				if(x>1)
				{
					x--;i=0;
				}
				else break;
			}
			rsv=rsv%2;
			if(b=='j'&&rsv==0)
			{
				break;
			}
			b=multiply(b,a[i]);
		}
		if(i<l)
		{
			b=a[i++];sum=1;
		}
		for(;;i++)
		{
			if(i==l)
			{
				if(x>1)
				{
					x--;i=0;
				}
				else break;
			}
			b=multiply(b,a[i]);
		}
		rsv=rsv%2;
		if(sum==1&&b=='k'&&rsv==0)
		printf("Case #%lld: YES\n",lol);
		else
		printf("Case #%lld: NO\n",lol);
	}
}
