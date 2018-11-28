#include <bits/stdc++.h>

using namespace std;

int T,S;
string s;
int main()
{
	int TT=0;
	cin>>T;
	while(T--)
	{
		cin>>S>>s;
		int x=s[0]-'0';
		int ans=0;
		for(int i=1;i<S+1;i++)
		{
			if(x<i)
			{
				ans+=i-x;
				x=i;
			}
			x+=s[i]-'0';
		}
		TT++;
		cout<<"Case #"<<TT<<": ";
		cout<<ans<<endl;
	}
	return 0;
}