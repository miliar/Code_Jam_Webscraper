#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Oh1.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s,res="";
		cin>>s;
		for(int j=0;j<s.length();j++)
		{
			if(j==0)	res += s[j];
			else
			{
				if(s[j]>=res[0])
					res=s[j]+res;
				else
					res=res+s[j];
			}
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}
