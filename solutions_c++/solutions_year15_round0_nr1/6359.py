#include<bits/stdc++.h>
using namespace std;
int main()
{	

	ios_base::sync_with_stdio(false);
	int test;
	cin>>test;

	for(int case_no=1;case_no<=test;++case_no)
		{
			int n;
			string s;
			cin>>n>>s;

			long long total_standing_till_now=0,ans=0;

			for(int i=0;i<=n;i++)
			{	
				if(s[i]=='0')
					continue;
				if(total_standing_till_now<i)
				{
					int friends_needed_this_time=i - total_standing_till_now;
					ans+= friends_needed_this_time;
					total_standing_till_now+= (int)(s[i]-'0')+friends_needed_this_time;

				}
				else
				{
					total_standing_till_now+= (int)(s[i]-'0');
				}

				
			}

			cout<<"Case #"<<case_no<<": "<<ans<<endl;
		}
	
return 0;
}
