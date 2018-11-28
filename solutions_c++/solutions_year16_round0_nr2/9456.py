#include <bits/stdc++.h>
#define ll long long
#define sz(a) a.size()
#define pb push_back
#define mp make_pair
#define srt(v) sort(v.begin(),v.end())
#define srtC(v,comp) sort(v.begin(),v.end(),comp)
#define FORI(i,x,n) for(int i=x;i<n;++i)
#define FORD(i,n) for(int i=n-1;i>=0;--i)

using namespace std;



int main()
{
	int T,count = 1;
	string s;
	freopen("B-large.in", "r", stdin);
	freopen("fileName.out", "w", stdout);
		scanf("%d",&T);
		while(T--)
		{
			int flip = 0, p = 0, n = 0;
			bool flag = false;
			cin>>s;
			for(int i = sz(s)-1;i>=0;--i)
			{
				if(!flag && s[i]=='-')
				{
					while(s[i]=='-')
						--i;

					++flip,++i;
					flag = true;
				}
				else if(flag && s[i] == '+')
				{
					while(s[i]=='+')
						--i;
					++flip,++i;
					flag = false;
				}
				else if (flag && s[i] == '+' && i==0)
					++flip;
				else if (!flag && s[i] == '-' && i==0)
					++flip;
			}
			if(p == 0 && n>0)
				flip=1;
			printf("Case #%d: %d\n",count,flip);
			++count;
		}


	return 0;
}
