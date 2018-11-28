#include <bits/stdc++.h>

#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define pb push_back
#define LL long long
#define F first
#define S second
#define VPI vector< pair<int,int> >
#define VVI vector< vector<int> > 
#define BC(x) __builtin_popcount(x)

using namespace std;

int main()
{
	int t;
	icin(t);
	for(int tc=1; tc<=t; tc++)
	{
		string s;
		int k;
		cin >> s;
		icin(k);
		int cur = 0;
		bool ans = true;
		for(int i=0; i<s.length(); i++)
		{
			if(s[i] == '-')
			{
				cur++;
				if( (i+k-1) < s.length())
				{
					for(int j=i; j<i+k; j++)
					{
						if(s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
					}
				}
			}

		}
		for(int i=0; i<s.length(); i++)
		{
			if(s[i] == '-')
				ans = false;
		}
		
		if(ans == false)
			printf("Case #%d: IMPOSSIBLE\n",tc);
		else
			printf("Case #%d: %d\n",tc,cur);
	}
	return 0;
}