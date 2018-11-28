#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		string s;
		cin>>s;
		int count=0;
		if(s[s.length()-1]=='-')
			count++;
		for(int i=0;i<s.length()-1;i++)
		{
			
			if(s[i]!=s[i+1])
				count++;
		}
		cout<<"Case #"<<j<<": "<<" "<<count<<"\n";
	}
	return 0;
}
