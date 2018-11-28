#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<b;++i)
#define m 1000000007
#define rev(i,a,b) for(i=a;i>b;--i)
#define ll long long int
using namespace std;
int main()
{
	ll test,t,count,i,len;
	char s[1000];
	cin>>t;
	test=1;
	while(t--)
	{
		scanf("%s",s);
		count=0;
		len=strlen(s);
		rep(i,0,len)
		{
			if(s[i]=='-')
			{
				if(s[i+1]=='+' || s[i+1]=='\0')
					count++;
			}
			else
			{
				if(s[i+1]=='-')
					count++;
			}
		}
		cout<<"Case #"<<test<<": "<<count<<endl;
		test++;
	}
	return 0;
}
