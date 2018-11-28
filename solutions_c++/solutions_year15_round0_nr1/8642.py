#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t; cin >> t;
	
	int cont=0;
	while(t--)
	{
		int n; cin >> n;
		string s;
		cin >> s;
		

		int v[n+1];
		for(int i=0; i<=n; i++) v[i] = s[i]-'0';

		cont++;
		cout << "Case #" << cont << ": ";
		
//		for (int i=0; i<=n; i++)
//			cout << v[i] << "***\n";

		int ac=v[0], ans=0;
		
		for(int i=1; i<=n; i++)
		{
			if(!v[i]) continue;
			if(ac<i) {ans += i-ac; ac += i-ac;}
			ac += v[i];
		}

		if(n) cout << ans << '\n';
		else cout << 0 << '\n';
	}
	return 0;
}
