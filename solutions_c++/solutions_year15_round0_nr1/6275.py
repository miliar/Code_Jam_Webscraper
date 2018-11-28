#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int k=1;k<=t;++k)
	{
		int n;
		string s;
		cin>>n>>s;
		int ans=0;
		int cur=0;
		cur=s[0]-'0';
		for(int i=1;i<s.size();++i)
		{
			if( cur>=i)
				cur+= (s[i]-'0');
			else
			{
				ans+=i-cur;
				cur=i;
				--i;
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}

}