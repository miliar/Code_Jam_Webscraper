/*
jai shree ram _/\_
A hacker from NITP
*/

#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int,char> msi;
typedef pair<int,int> pa;
typedef long long int ll;

char a[1004];
ll s,i,cnt,ans;
int main()
{
	freopen("alarge.in", "r", stdin);
  	freopen("anslarge.out", "w", stdout);
  	int t,p=1;
	cin>>t;
	while(t--)
	{
		cin>>s>>a;
		cnt=0; ans=0;
		for(i=0;i<=s;i++)
		{
			if(i>cnt)
			{
				ans+=(i-cnt);
				cnt=i;
			}
			cnt+=(a[i]-'0');
		}
		cout<<"Case #"<<p++<<": "<<ans<<"\n";
	}
	return 0;
}


