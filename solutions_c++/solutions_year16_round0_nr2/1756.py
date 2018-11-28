#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve(string s)
{
	bool d=1;
	int cnt=0;
	for(int i=s.size()-1;i>=0;i--)
	{
		if(d)
			if(s[i]=='-')
				d=!d, cnt++;
		if(!d)
			if(s[i]=='+')
				d=!d, cnt++;	
	}
	return cnt;
}

int main()
{
	int t;
	string s;
	scanf("%d", &t);
	for(int tc=1;tc<=t;tc++)
	{
		cin>>s;
		printf("Case #%d: %d\n", tc, solve(s));
	}
	return 0;
}