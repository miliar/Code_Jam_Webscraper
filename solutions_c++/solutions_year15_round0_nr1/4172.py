#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main() 
{
	string s;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long T,t,i,j,n,x,sum;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n;
		cin>>s;
		x=0;
		sum=s[0]-'0';
		for(i=1;i<s.size();i++)
		{
			if(s[i]=='0')
			continue;
			if(sum<i)
			{
				x+=i-sum;
				sum=i+s[i]-'0';
			}
			else
			sum=sum+s[i]-'0';
		}
		cout<<"Case #"<<t<<": "<<x<<"\n";
	}
	return 0;
}
