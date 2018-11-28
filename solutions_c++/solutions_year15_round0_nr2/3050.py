#include<stdio.h>
#include<windows.h>
#include<queue>
#include<vector>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		int N, ans=1, max=0, top;
		int q[1100] = {0,};
		scanf("%d", &N);
		if(tc == 83)
			tc = tc;
		for(int i = 1; i <= N; i++){
			scanf("%d", &q[i]);
			if(max < q[i]) max = q[i];
		}
		ans = max;
		for(int i = 1; i <= max; i++){
			int tmp = i;
			for(int j = 1; j <= N; j++){
				if(i >= q[j]) continue;
				tmp += q[j] / i;
				if(q[j] % i != 0) tmp++;
				tmp--;
			}
			if(ans > tmp) ans = tmp;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}