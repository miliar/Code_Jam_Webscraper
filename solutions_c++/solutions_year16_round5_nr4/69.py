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
map<string,int> mapp;
int main()
{
	// freopen("D.in","r",stdin);
	// freopen("D.out","w",stdout);
	int t,i;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		mapp.clear();
		int n,l;
		sd(n);sd(l);
		string s;
		for(i=0;i<n;++i)
		{
			cin>>s;
			mapp[s]=1;
		}
		cin>>s;
		if(mapp[s])
		{
			printf("Case #%d: IMPOSSIBLE\n",tt);
			continue;
		}
		if(l==1)
		{
			printf("Case #%d: 0 ?\n",tt);
			continue;
		}
		string s1="",s2="";
		for(i=0;i<l-1;++i)
			s1+='?';
		for(i=0;i<50;++i)
		{
			if(i%2==0)
				s2+='1';
			else
				s2+='0';
		}
		s2+='?';
		for(i=0;i<50;++i)
		{
			if(i%2==0)
				s2+='1';
			else
				s2+='0';
		}
		printf("Case #%d: ",tt);
		cout<<s1<<' '<<s2<<'\n';
	}
}