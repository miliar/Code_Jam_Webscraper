#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORI(i,b,a) for(int i=b;i>=a;--i)


int main()
{
	int t;
	scanf("%d", &t);
	string s;
	FOR(casenum,1,t+1)
	{
		cin>>s;
		if(s.size()==1)
		{
			if(s[0]=='+')printf("Case #%d: %d\n",casenum,0 );
			else printf("Case #%d: %d\n",casenum,1 );
			continue;
		}
		else
		{
			int swaps=0;
			FOR(i,0,s.size()-1)
			{
				if(s[i] != s[i+1]) swaps++;
			}
			if(s[s.size()-1] == '-') swaps++;
			printf("Case #%d: %d\n",casenum,swaps );
		}
	}
}