#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output2.out","w",stdout);
	int t,i,count=0;
	cin>>t;
	while(t--)
	{
		count++;
		char ch[100];
		memset(ch,'\0',sizeof(ch));
		cin>>ch;
		ll ans=0;
		for(i=1;i<strlen(ch);i++)
		{
			if(ch[i]!=ch[i-1])
			{
				for(int j=0;j<i;j++)
					ch[j]=ch[i];
				ans++;
			}
		}
		if(ch[0]=='-')
			ans++;
		cout<<"Case #"<<count<<": "<<ans<<endl;
	}
	return 0;
}
