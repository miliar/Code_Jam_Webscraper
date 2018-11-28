#include <bits/stdc++.h>

using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
   	freopen("input.txt", "rt", stdin);
   	freopen("output.txt", "wt", stdout);
	#endif
	int t;
	int n;
   	string g;
   	cin >> t;
	for (int cas = 0; cas < t; ++cas)
	{
		cin >> n;
   		cin >> g;
   		n++;
	   	int s = 0;
   		int ans = 0;
   		for (int i = 0; i < n-1; ++i)
   		{
   			if( s >= i ) s+=g[i]-'0';
   			else s+=(g[i]-'0')+1,ans++;
   		}
   		if( s < n-1 ) ans++;
   		cout<<"Case #"<<cas+1<<": "<<ans<<endl;
    }
}