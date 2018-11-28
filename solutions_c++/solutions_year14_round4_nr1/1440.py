#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int T, n, x;
	int a[10010];
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%d %d", &n, &x);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
		}
		sort(a, a + n);
		int i = 0;
		int j = n - 1;
		int res = 0;
		while (true)
		{
			if(i > j)	break;
			else if(i == j){
				res++;
				break;
			}
			else{
				if(a[i] + a[j] <= x){
					res++;
					i++;
					j--;
				}
				else
				{
					res++;
					j--;
				}
			}
		}


		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}