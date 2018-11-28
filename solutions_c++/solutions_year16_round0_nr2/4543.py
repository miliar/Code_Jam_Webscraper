#include <iostream>
using namespace std;

int main()
{
	int t,count,n;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		string s;
		cin>>s;
		count=0;
		n=s.length();
		for(int i=0;i<n-1;i++)
		{
			if(s[i]!=s[i+1])
				count++;
		}
		if(s[n-1]=='-')
			count++;
		cout<<"Case #"<<z<<": "<<count<<endl;
	}
	return 0;
}
