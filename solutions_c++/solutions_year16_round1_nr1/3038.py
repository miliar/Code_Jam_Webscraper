#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large(1).in","r",stdin);
	freopen("outputlarge.out","w",stdout);
	int t,count=0;
	cin>>t;
	while(t--)
	{
		count++;
		string s;
		cin>>s;
		int l=s.length();
		string str="";
		str+=s[0];
		for(int i=1;i<l;i++)
		{
			string s1,s2;
			s1=str+s[i];
			s2=s[i]+str;
			if(s1>=s2)
				str=s1;
			else
				str=s2;
		}
		cout<<"Case #"<<count<<": "<<str<<endl;
	}
	return 0;
}
