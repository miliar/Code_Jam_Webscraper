#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	int m=t;
	while(t--)
	{
		string s;
		cin>>s;
		long long sum=0;
		for(int i=0;i<s.length();i++)
		{	int j=i;
			if(s[i]=='-')
			{
			while(s[i]=='-')
			{
				i++;
			}
			if(j==0)
			sum+=1;
			else
			sum+=2;}
		}
			cout<<"Case #"<<m-t<<": "<<sum<<"\n";
		}
	}

