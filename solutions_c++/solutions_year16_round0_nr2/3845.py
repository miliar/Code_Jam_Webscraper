#include<iostream>
#include<map>
#include<string>
#include<vector>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i<<": ";
		if((int)s.size()==1)
		{
			if(s[0]=='+')
				cout<<"0\n";
			else cout<<"1\n";
			continue;
		}
		int count=0;
		for(int j=1;j<(int)s.size();j++)
			if(s[j]!=s[j-1])
				count++;
		if(s[(int)s.size()-1]=='-')
			cout<<count+1<<"\n";
		else cout<<count<<"\n";
	}
	return 0;
}
