#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<memory>
#include<map>
#include<queue>
#include<limits>
#include<iomanip>
#include<fstream>
using namespace std;

int main()
{
	freopen("2_large.in","r",stdin);
	freopen("2_olarge.out","wt",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<tc<<": ";
		if(s.length()==1)
		{
			if(s[0]=='+')
			cout<<"0"<<endl;
			else
			cout<<"1"<<endl;
		}
		else
		{
		int m=s.length()-1,count=0;
		while(m>=0)
		{
			if(s[m]=='-')
			{
			count++;
			for(int i=0;i<=m;i++)
			{
				if(s[i]=='-')
					s[i]='+';
				else
					s[i]='-';
			}
			}
			m--;
		}
		cout<<count<<endl;		
		}
		
		//cout<<endl;
	}
	return 0;
}
