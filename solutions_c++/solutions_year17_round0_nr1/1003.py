#include<bits/stdc++.h>
using namespace std;
string s;
int k,n;
bool check()
{
	for(int i=n-k;i<n;i++)
		if(s[i]=='-') return false;
	return true;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,kase=1;
	cin>>T;
	while(T--)
	{
		cin>>s>>k;
		n=s.length();
		int ans=0;
		for(int i=0;i<=n-k;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=0;j<k;j++)
					s[i+j]=(s[i+j]=='+'?'-':'+');
			}
		}
		printf("Case #%d: ",kase++);
		if(check()) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
