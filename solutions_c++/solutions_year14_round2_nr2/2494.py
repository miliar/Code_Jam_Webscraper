#include <bits/stdc++.h>
using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;

int main() 
{ 
	
	int t; cin >> t;
	for (int tt = 0; tt < t; ++tt)
	{
	
		int a,b,k; cin >> a >> b >> k;

		int ans=0;
		for (int i = a-1; i >= 0; --i)
		{
			for (int j = b-1; j >=0 ; --j)
			{

				if ((i & j) < k)
				{
					ans++;
				}
			}
		}
		
		cout << "Case #" << tt + 1<< ": " <<ans << endl;

	}

	return 0;
} 
