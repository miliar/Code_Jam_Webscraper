#include <bits/stdc++.h>
using namespace std;
#define int long long
main()
{
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	int a; cin >> a;
	for (int g=0; g<a; g++)
	{
		int b; cin >> b;
		string c; cin >> c;
		int last=0; 
		long long answer=0; 
		vector <int> t; 
		for (int y=0; y<c.length(); y++)
		{
			for (int z=0; z<c[y]-'0'; z++)
			{
				t.push_back(y); 
			}
		}
		for (int y=0; y<t.size(); y++)
		{
			if (last>=t[y])
			{
				last++; continue; 
			}
			answer+=t[y]-last; 
			last=t[y]+1; 
		}
		cout <<"Case #" << g+1 << ": " << answer << '\n';
	}
	return 0; 
}
