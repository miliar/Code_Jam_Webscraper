#include<bits/stdc++.h>
#define pf printf
using namespace std;
string s;
int main()
{
	int t;
	cin>>t;
	static int k = 1;
	while(t--)
	{
		cin>>s;
		int ans = 0;
		for(int i=0;i<s.length()-1;i++)
		{
			 if(s[i] != s[i+1])
			    ans++;
		}
		
		if(s[s.length()-1] == '-')
		  ans++;
		  
		  pf("Case #%d: ", k);  k++;
		  pf("%d\n", ans);
	}
	
}
