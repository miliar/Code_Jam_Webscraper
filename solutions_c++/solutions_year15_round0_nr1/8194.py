//#include <iostream>
#include<bits/stdc++.h>
using namespace std;
//#define MAX 1000000
//#define MOD 100000007
//typedef long long LL;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,s,i,c,req,j;
	string st;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>s;

		cin>>st;
		req=0;c=0;
for(i=0;i<s;i++)
		{
c=c+(st[i]-'0');
//cout<<c<<endl;
if(c<i+1)
	{req = req+1;
	c = c+1;
	}
else
	continue;		
	//cout<<req<<endl;
}
//if(c>=s)
	cout<<"Case #"<<j<<": "<<req<<endl;
//else
	//cout<<"Case #"<<j<<" "<< s-c<<endl;

	}
	
	return 0;
}
