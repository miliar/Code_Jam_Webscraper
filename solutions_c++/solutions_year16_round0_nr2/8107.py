#include <bits/stdc++.h>
using namespace std;

int findToggle(string str)
{
	int l=str.length();char c=str[0];
	for(int i=0;i<l-1;i++)
	{
		if(str[i]!=str[i+1])
		{
			return i;
		}
	}
	if(c=='+')
	{
		return -1;
	}
	else
	{
		return l-1;
	}
}	

bool check(string pancakes)
{
	int l=pancakes.length();
	for( int i=0;i<l;i++)
	{
		if(pancakes[i]=='-')
		return false;
	}
	return true;
}

int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		string pancakes;
		cin>>pancakes;
		
		int c=0,p;
		while(!check(pancakes))
		{
			p=findToggle(pancakes);
			for(int i=0;i<=p;i++)
			{
				if(pancakes[i]=='+')
				{
					pancakes[i]='-';
				}
				else
				{
					pancakes[i]='+';
				}
			}
			c++;
		}
		cout<<"Case #"<<k<<": "<<c<<endl;
	}
	
}
