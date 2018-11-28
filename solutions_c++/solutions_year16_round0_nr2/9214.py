#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int a;
string tab;
int wyn;
bool zm;

bool szN()
{
	for(int x=0;x<tab.size();x++)
	{
		if(tab[x]!='-')
		{
			return 1;
		}
	}
	return 0;
}

bool szP()
{
	for(int x=0;x<tab.size();x++)
	{
		if(tab[x]!='+')
		{
			return 1;
		}
	}
	return 0;
}

void cChP( int c )
{
	for(int i=-1;i<=c;i++)
	{
		tab[i]='+';
	}
}

void cChN( int c )
{
	for(int i=-1;i<=c;i++)
	{
		tab[i]='-';
	}
}

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "wyj.txt", "w", stdout );	
	
cin>>a;
	
	for(int i=0;i<a;i++)
	{
		cin>>tab;
		for(int j=0;j<tab.size()+1;j++)
		{
			if(szN()==0)
			{
				wyn++;
				break;
			}
			
			if(szP()==0)
			{
				break;
			}
			
			
			if(tab[j]=='-')
			{
				if(tab[j+1]!='-')
				{
					cChP(j);
					wyn++;
				}
			}
			else
			{
				if(tab[j+1]!='+')
				{
					cChN(j);
					wyn++;
				}
			}
		}
	cout<<"Case #"<<i+1<<": "<<wyn<<endl;
	wyn=0;
	}

return 0;
}
