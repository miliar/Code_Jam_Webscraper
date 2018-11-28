#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;

int a;
int tab[101];
int war;
bool ch[12];
int x;
string licz;

void zap()
{
	
	int rem=war;
	while(rem>0)
	{	
		ch[rem%10]=true;
		rem/=10;
	}
}

bool tr()
{
	for(int i=0;i<10; )
	{
		if(ch[i]==false)
		{
			return 0;
		}
		i++;
	}
	return 1;
}

void zero()
{
	for(int i=0;i<10;i++)
	{
		ch[i]=0;
	}
}
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "wyjscie.txt", "w", stdout );
cin>>a;	
	for(int i=1;i<=a;i++)
	{
		cin>>tab[i];
		war=tab[i];
		
		if(tab[i]==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}	
		else
		{
			for(int j=1 ; ; j++ )
			{	
				war*=j;
				zap();
				if( tr()==1 )
				{
					cout<<"Case #"<<i<<": "<<war<<endl;
					zero();
					break;
				}
				war=tab[i];
			}

		}
		
	}	
return 0;	
}
