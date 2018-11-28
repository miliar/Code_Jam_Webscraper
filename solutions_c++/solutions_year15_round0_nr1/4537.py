#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;
int main()
{
	freopen("/Users/Erona/Downloads/A-large.in","r",stdin);
	freopen("/Users/Erona/Downloads/A-large.ans","w",stdout);

	int T;
	cin>>T;
	for(int Case=1;Case<=T;Case++)
	{
		int n;
		string s;
		cin>>n>>s;
		int sum=s[0]-'0';
		int ans=0;
		for(int i=1;i<s.length();i++)
		{
			if(i>sum)
			{
				ans+=i-sum;
				sum+=i-sum;
			}
			sum+=s[i]-'0';
		}
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	}
	return 0;
}