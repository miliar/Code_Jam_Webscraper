#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
	string s;
	long long a,count=0;
	cin>>s;
	a=s.length()-1;
	for(int i=a;i>-1;i--)
	{
		if(s[i]=='-')
		{
			for(int j=0;j<=i;j++)
			{
				if(s[j]=='-')
				{
					s[j]='+';
				}
				else
				{
					s[j]='-';
				}
			}
			count++;
		}
		
	
	}
	cout<<"Case #" <<k<<": "<<count<<endl;
	}
	
	
	

	return 0;
}
