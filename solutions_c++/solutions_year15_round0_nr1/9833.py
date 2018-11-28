#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main() {
	int t;
	cin>>t;
	int n,diff, ans, cnt=1;
	string ip;
	while(t--)
	{
		cin>>n>>ip;
		diff=(a[0]-'0');ans=0;
		for(int i=1;i<=n;i++)
		{
			if(diff>=i)
			{
				diff=diff+(ip[i]-'0');
			}
			else
			{
				ans=ans+(i-diff);
				diff=diff+(i-diff)+(ips[i]-'0');
			}
		}
		cout<<"Case #"<<cnt++<<": "<<ans<<endl;
	}
	return 0;
}
