#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int fsize[11111];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);
		int N = 0;
		int X = 0;
		scanf("%d %d",&N,&X);
		for(int i = 0;i < N;i++) scanf("%d",&fsize[i]);
		sort(fsize,fsize+N);
		
		int ans = 0;
		int l = 0;
		int r = N-1;
		while(l <= r)
		{
			ans++;
			if(l < r && fsize[r] + fsize[l] <= X) l++;
			r--;
		}
		printf("%d\n",ans);
	}
	return 0;
}