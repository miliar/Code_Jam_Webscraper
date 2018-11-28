#include <cmath>
#include <cstdio>#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int calculate( string z,int x,int y)
{
	int count =0; int maxi =0;
	for(int a=x;a<=y;a++)
	{
		//cout<<z[a];
		if(z[a]!='a' && z[a]!='e' && z[a]!='i' && z[a]!='o' && z[a]!='u' )
			count++;
		else
		{
			if(count>maxi)
				maxi=count;
			count =0;
		}
	}
	if(count !=0 && count>maxi)
		maxi =count;
	//cout<<maxi<<endl;
	return maxi;
}

int main() 
{
	int kase =0;
	cin>>kase;
	int first = 1;
	string dum;
	//getline(cin,dum);
	while(first <=kase)
	{
		string s;
		int k;
		cin>>s;
		cin>>k;
		int ans=0;
		for(int i=0;i<s.size();i++)
		{
			for(int j=i;j<s.size();j++)
				if(calculate(s,i,j)>=k)
					ans++;
		}
		cout<<"Case #"<<first<<": "<<ans<<endl;
		first++;
	}
    return 0;
}

