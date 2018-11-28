		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

long long b[N], have[N];

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int n = in(), k = in();
		fill(have, have + n, 0);
		for(int i = 0; i < n; i++)
			b[i] = in();
		long long l = 0, r = 1e18;
		long long cnt;
		while(r - l > 1)
		{
			long long mid = (l + r)/2;
			cnt = 0;
			for(int i = 0; i < n; i++)
				cnt += (mid / b[i] + 1);
			if(cnt >= k)
				r = mid;
			else
				l = mid;
		}
		int x = -1;
		for(int i = 0; i < n; i++)
			cnt += (r / b[i] + 1);
		long long cnt2 = 0;
		r--;
		for(int i = 0; i < n; i++)
			cnt2 += (r / b[i] + 1);
		while(cnt2 >= k)
		{
			r--;
			cnt2 = 0;
			for(int i = 0; i < n; i++)
				cnt2 += (r / b[i] + 1);
		}
		assert(cnt >= k);
		assert(cnt2 < k);
		for(int i = 0; i < n; i++)
		{
			assert(cnt2 <= k);
			if((r + 1) % b[i] == 0)
			{
				cnt2++;
				if(cnt2 == k)
				{
					x = i;
					break;
				}
			}
		}
		assert(cnt2 >= k);
		assert(x != -1);
		cout << 1 + x << "\n";
	}
}
