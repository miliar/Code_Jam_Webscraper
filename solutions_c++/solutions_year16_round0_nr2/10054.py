#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
ll ans;

void convert(string s,int st,int end)
{
	while(s[end-1]=='+')
		end--;
	if(st==end)
		return;
	ll i,j,k,ptr,ct;
	// cout << s << "\n";
	if(s[0]=='+')
	{
		i=0;
		while(s[i]=='+' && i<end)
		{
			s[i]='-';
			i++;
		}
		ans++;
		convert(s,st,end);
	}
	else
	{
		i=0;ct=0,ptr=0;
		while(s[i]=='-' && i<end)
		{
			i++;
			ct++;
		}
		for(i=0;i<end;i++)
		{
			if(s[i]=='+')
				s[i] = '-';
			else
				s[i] = '+';
		}
		reverse(s.begin(),s.begin()+end);
		ans++;
		convert(s,st,end-ct);
	}
	return;
}
int main()
{
	string s;
	ll i,j,k,l,m,n,t;
	cin >> t;
	for(i=1;i<=t;i++)
	{
		cin >> s;
		ans = 0;
		if(s.size()==0)
			cout << "Case #" << i << ": " << 0 << "\n";
		else
		{
			convert(s,0,s.size());
			cout << "Case #" << i << ": " << ans << "\n";
		}
	}
	return 0;
}	