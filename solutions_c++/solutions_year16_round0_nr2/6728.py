#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

	string s;
	int i,j,k,cnt,l;

	void flip_it();
	
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w+",stdout);
	
	int t,k;
	cin>>t;
	
	for(k=1;k<=t;k++)
	{	
		cin>>s;
		l=s.length();
		reverse(s.begin(),s.end());
		//cout<<s;
		cnt=0;
		for(i=0;i<=l;i++)
		{
			if(s[i]=='-' && s[i+1]=='+')
			{
				cnt++;
				flip_it();
			}
			if(i==(l-1) && s[i]=='-')
			cnt++;
		}	
		
		cout<<"Case #"<<k<<": "<<cnt<<endl;
	}
}

void flip_it()
{
	int l=s.length();
	int	i;
	for(i=0;i<l;i++)
	{
		if(s[i]=='+')
		s[i]='-';
		else
		s[i]='+';
	}
	
}