#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("input-large.txt","r",stdin);
	freopen("output-large.txt","w",stdout);
	int t;
	cin >> t;
	int count=0;
	while(count<t)
	{
		count++;
		cout << "Case #" << count << ": " ;
		string s;
		cin >> s;
		int len=s.size();
		int cnt=0;
		string ans="";
		ans=ans+s[0];
		for(int i=1;i<len;i++)
		{
			if(s[i]>=ans[0])
			{
				ans=s[i]+ans;
			}
			else
			{
				ans=ans+s[i];
			}
		}
		cout << ans << endl;
	}
	return 0;
}
