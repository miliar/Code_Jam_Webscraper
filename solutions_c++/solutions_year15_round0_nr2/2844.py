#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	// freopen("1.in", "r", stdin);
	// freopen("1.out", "w", stdout);
	int ttt;
	scanf("%d", &ttt);
	for (int ca = 1; ca <= ttt; ca++)
	{
		int n;
		scanf("%d", &n);
		priority_queue<int> ori, a;
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			ori.push(x);
		}
		int l = 0, r = 1001;
		while (l <= r)
		{
			int mid = (l + r) / 2;
			bool flag = false;
			for (int cut = 0; cut <= mid; cut++)
			{
				a = ori;
				int share = mid - cut;
				for (int i = 0; i < cut; i++)
				{
					int tmp = a.top();
					a.pop();
					if (tmp <= share)
						break;
					a.push(share);
					a.push(tmp - share);
				}
				if (a.top() <= share)
				{
					flag = true;
					break;
				}
			}
			if (flag)
				r = mid - 1;
			else
				l = mid + 1;
		}
		printf("Case #%d: %d\n", ca, l);
	}
	return 0;
}