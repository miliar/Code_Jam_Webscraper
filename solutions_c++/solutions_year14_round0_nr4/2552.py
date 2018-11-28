#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#define eps 1e-7

using namespace std;
double N1[1005], N2[1005];

int work1(int l, int n)
{
	int ans = 0;
	for (int i=l+1, j=1; i<=n && j<=n-l; i++, j++)
	{
		while (N2[j] < N1[i]) j++;
		if (j<=n-l) ans ++ ;
	}
	return n - l - ans;
}

int work2(int l, int n)
{
	int ans = 0;
	for (int i=l+1, j=1; i<=n && j<=n-l; i++, j++)
	{
		while (N2[j] > N1[i]) i++;
		if (i<=n) ans ++ ;
	}
	return ans;
}

int main()
{
	freopen("1.txt", "r", stdin);	
	freopen("2.txt", "w", stdout);	
	int cas, T;
	
	for (cas=scanf("%d", &T); cas<=T; cas++)
	{
		int n;
		cin >> n;
		for (int i=1; i<=n; i++) scanf("%lf", &N1[i]);
		for (int i=1; i<=n; i++) scanf("%lf", &N2[i]);
		
		sort(N1+1, N1+n+1);
		sort(N2+1, N2+n+1);
		
		int ans2 = work1(0, n), ans1 = work2(0, n);
		for (int i=1; i<=n; i++)
			if (N1[i] < N2[n-i+1])
				ans1 = max(ans1, work2(i, n));
				
		printf("Case #%d: %d %d\n", cas, ans1, ans2);
	}
    return 0;
}
