#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		char str[105];
		cin>>str;
		int l=strlen(str);
		int count=0;
		
		for(int i=1;i<l;i++)
		{
			if(str[i]!=str[i-1])
			count++;
		}
		
		int ans;
		if(count&1)
		{
			if(str[0]=='+')
			ans=count+1;
			else
			ans=count;
		}
		else
		{
			if(str[0]=='+')
			ans=count;
			else
			ans=count+1;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
