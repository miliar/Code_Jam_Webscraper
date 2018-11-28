#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std ;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >> n;
	for(int i=1 ; i <= n ; i++)
	{
		int c=0;
		string s;
		cin >> s;
		while(s[s.size()-1]=='+')
			s.erase(s.size()-1,1);
		s += "?";
		for(int i=0 ; i < (int)s.size()-1 ; i++)
		{
			if(s[i]!=s[i+1])
				c++;
		}
		printf("Case #%d: %d\n",i,c);
	}
}
