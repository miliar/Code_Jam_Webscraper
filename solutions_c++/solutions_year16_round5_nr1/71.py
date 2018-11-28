#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define ll long long
char s[20010];
stack<char> st;
int main()
{
	// freopen("A1.in","r",stdin);
	// freopen("A1.out","w",stdout);
	
	int t,i;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		ss(s);
		int n=strlen(s);
		while(!st.empty())
			st.pop();
		int ans=0;
		for(i=0;i<n;++i)
		{
			bool f=0;
			if(!st.empty())
			{
				if(st.top() == s[i])
				{
					st.pop();
					f=1;
					ans+=10;
				}
			}
			if(!f)
				st.push(s[i]);
		}
		ans+=(5*((int)st.size())/2);
		printf("Case #%d: %d\n",tt,ans);
	}
}