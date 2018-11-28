#include <bits/stdc++.h>
 
 
 
#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define LL long long
#define F first
#define S second
#define pb push_back
#define mod (LL)(1e9+7)
#define LL long long
#define VVI vector< vector<int> >
#define MAXN 100000
#define MAXL 18
#define pii pair<int,int>
#define vpi vector< pair<int,int> >
#define vvpi vector< vector<pair<int,int>> >

using namespace std;
 


int main()
{
	int t;
	icin(t);
	int x=0;
	while(t--)
	{
		x++;
		string s;
		int ans=0;
		cin >> s;
		int cnt=0;
		int cur=-2;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				if(i-cur>1)
					cnt++;
				cur=i;
			}
		}
		if(cnt==0)
		ans=0;
		else if(s[0]=='+')
		ans =  2*(cnt);
		else
		ans = 1 + 2*(cnt-1);
		printf("Case #%d: %d\n",x,ans);
	}

} 