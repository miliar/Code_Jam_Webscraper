#include<iostream>
using namespace std;
int main()
{
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		long n,ppl=0,ans=0;
		string s;
		cin>>n>>s;
		ppl = (int)(s[0]-'0');
		for(int i=1;i<=n;i++)
		{
			if(ppl < i && s[i]!='0')
			{
				ans += i-ppl;
				ppl += ans+(int)(s[i]-'0');
			}
			else
				ppl += (int)(s[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
return 0;
}
