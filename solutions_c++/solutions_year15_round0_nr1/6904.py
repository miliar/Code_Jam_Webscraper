#include<iostream>
#include<string>

using namespace std;

main()
{
	int t,c;
	cin>>t;
	c=1;
	while(t--)
	{
		int res=0;
		int n;
		cin>>n;
		string s;
		cin>>s;
		int sm=0;
		for(int i=0;i<s.length();i++)
		{
			if(i>sm&&s[i]!='0')
			{
				
				res+=i-sm;
				sm=i+s[i]-'0';
				continue;
			}
			sm+=s[i]-'0';
		}
		cout<<"Case #"<<c++<<": "<<res<<endl;
	}
}