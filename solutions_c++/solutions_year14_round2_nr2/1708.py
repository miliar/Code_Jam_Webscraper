#include <bits/stdc++.h>
using namespace std;

#define lli long long int

int main()
{
	int T, t;
	cin >> T;
	for(t = 1; t <= T; ++t)
	{
		int a,b,k;
		cin >> a >> b >> k;
		int i, j, ans = 0;
		for(i = 0; i < a; ++i)
			for(j = 0; j < b; ++j)
				if((i & j) < k) ++ans;
		printf("Case #%d: ", t); 
		cout << ans << endl;
	}
	return 0;
}
