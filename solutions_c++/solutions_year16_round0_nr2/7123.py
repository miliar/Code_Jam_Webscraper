#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int t,case0=0;
	scanf("%d",&t);
	while(t--)
	{
		case0++;
		int count=0;
		string s,t="";
		cin>>s;
		for(int i=0;i<s.length()-1;i++)
		{
			if(s[i]!=s[i+1])
			{
				t="";
				int k=i+1;
				count++;
				while(k--)
				{
					t+=s[i+1];
				}
			}
		}
		t+=s[s.length()-1];
		if(t[0]=='-')
			cout<<"Case #"<<case0<<": "<<(count+1)<<endl;
		else
			cout<<"Case #"<<case0<<": "<<count<<endl;
	}
	return 0;
}
