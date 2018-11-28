#include<stdio.h>
#include<algorithm>
int dat[10001];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, TT;
	scanf("%d", &T);
	for(TT = 1; TT<=T; TT++)
	{
		int n, X, i, ans;
		scanf("%d%d", &n, &X);
		for(i=1; i<=n; i++)scanf("%d", dat+i);
		std::sort(dat+1, dat+1+n);
		ans = n;
		int j = n;
		for(i=1; i<=n && i<j; i++)
		{
			while(X-dat[j] < dat[i] && i<j)j--;
			if(i>=j) break;
			ans--;
			j--;
		}
		printf("Case #%d: %d\n", TT, ans);
	}
	return 0;
}