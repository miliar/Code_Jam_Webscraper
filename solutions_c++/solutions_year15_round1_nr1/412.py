		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int x[N];

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int n = in();
		for(int i = 0; i < n; i++)
			x[i] = in();
		long long ans1 = 0, ans2 = 0;
		int rate = 0;
		for(int i = 1; i < n; i++)
		{
			ans1 += max(0, x[i - 1] - x[i]);
			rate = max(rate, x[i - 1] - x[i]);
		}
		for(int i = 1; i < n; i++)
			ans2 += min(x[i - 1], rate);
		cout << ans1 << " " << ans2 << "\n";
	}
}
