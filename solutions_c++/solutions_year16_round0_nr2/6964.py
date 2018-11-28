#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int T = t;
	while(t--)
	{
		string s;
		cin>>s;
		int n= s.length();
		int count=0;
		for(int i=0;i<n-1;i++)
		{
			if(s[i]!=s[i+1])count++;
		}
		if(s[n-1]=='-')count++;
		cout<<"Case #"<<(T-t)<<": "<<count<<"\n";
	}
}