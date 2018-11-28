#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("gcj1.txt","rt",stdin);
	freopen("gcj2.txt","wt",stdout);
int t;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		int add=0,nop=0,s;
		char str[1002];
		cin>>s;
		cin>>str;
		//cout<<str<<endl;
		nop+=str[0]-'0';
	//	cout<<nop<<endl;
		for(int i=1;i<=s;i++)
	{
		//cout<<nop<<endl;
		if(str[i]!='0')
		{
		
		if(nop<i)
		{
			add+=i-nop;
			nop=i;
			//cout<<add<<endl;
		}
		nop+=str[i]-'0';
	
	}
	}
	cout<<"Case #"<<x<<": "<<add<<endl;	
	}
	return(0);
}
