#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.txt","r",stdin);
	freopen("B-large_sol.txt","w",stdout);
	int t;
	cin >> t;
	int count=0;
	while(count<t)
	{
		count++;
		cout << "Case #" << count << ": ";
		string s;
		cin >> s;
		int cnt_minus=0,cnt_plus=0;
		int ans=0;
		int len=s.size();
		bool flag=0;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='+')
			{
				if(cnt_minus>0)
				{
					if(flag==0)
						ans+=1;
					else
						ans+=2;
				}
				cnt_minus=0;
				flag=1;
			}
			else
			{
				cnt_minus++;
			}
		}
		if(s[len-1]=='-'&&flag==1)
			ans+=2;
		else if(s[len-1]=='-')
			ans++;
		cout << ans << endl;
	}
	return 0;
}
