#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,ii=1;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		string s2="";
		s2+=s[0];
		for(int i=1;i<s.length();i++)
		{
			if(s[i]>=s2[0])
				s2=s[i]+s2;
			else
				s2=s2+s[i];
		}
		cout<<"Case #"<<ii++<<": "<<s2<<endl;
	}
	return 0;
}