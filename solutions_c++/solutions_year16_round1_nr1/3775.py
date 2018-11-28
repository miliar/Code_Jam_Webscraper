#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	string s;
	scanf("%d",&t);
	for(int test=1;test<=t;++test)
	{
		string ans;
		cin>>s;
		//ans.append(s[0]);
		ans.insert(0,s,0,1);
		char start;
		start=s[0];
		//last=s[0];
		for(unsigned int i=1;i<s.length();++i)
		{
			if((char)s[i]>=start)
			{
				ans.insert(0,s,i,1);
				//ans.append(s[i],i,1);
				start=s[i];
				//curr++;
			}
			else
			{
				//ans.append(s[i],i,1);
				ans.insert(ans.length(),s,i,1);
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<"\n";
	}
	return 0;
}

