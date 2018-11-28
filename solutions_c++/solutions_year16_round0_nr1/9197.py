#include<bits/stdc++.h>
using namespace std;

#define MAXN 1000000

long long run(int n)
{
	bool vis[10] = {0};
	long long N = n, temp;
	int i, cnt = 0;
	while (N > 0)
	{
		temp = N;
		while (temp) 
		{
			if (!vis[temp%10]) vis[temp%10] = true, ++cnt;
			temp /= 10;
		}
		if (cnt == 10) break;
		N += n; 
		while (N > 1000000000000LL);
	}
	while (cnt != 10);
	return N;
}

int main()
{
	freopen("Ainhard.txt", "r", stdin);
	freopen("Aouthard.txt", "w", stdout); 
	int t,T,N;
	scanf("%d", &T);
	for (t=1; t<=T; ++t)
	{
		scanf("%d", &N);
		if (N == 0) printf("Case #%d: INSOMNIA\n", t);
		else printf("Case #%d: %lld\n", t,run(N));
	}
	return 0;
}