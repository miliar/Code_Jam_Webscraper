#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	char str[1010];
	string ans;
	ll t,n,i,counter=1,l;
	cin>>t;
	while(t--)
	{
		cin>>str;
		ans="";
		ans+=str[0];
		for(i=1;i<strlen(str);++i)
		{
			if(str[i]>=ans[0])
			{
				string temp;
				temp="";
				temp+=str[i];
				temp+=ans;
				ans=temp;
			}
			else
				ans+=str[i];
		}
		cout<<"Case #"<<counter++<<": "<<ans<<endl;
	}
	return 0;
}