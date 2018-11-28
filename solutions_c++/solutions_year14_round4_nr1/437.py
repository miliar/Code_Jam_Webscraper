///*
#include <algorithm>
#include <stdio.h>
#include <vector>
#include<set>

using namespace std;

int D[10005];
int cnt[705];
int N, X;

int solve()
{
	int ans = 0, tot = 0;
	for(int i = 1; i <= 700; i++){
		cnt[i] = 0;
	}
	for(int i = 1; i <= N; i++){
		cnt[D[i]]++;
		tot++;
	}
	while(tot != 0){
		int sum = X;
		ans++;
		for(int i = 700, pp = 0; i >= 1 && pp < 2; i--){
			if( cnt[i] == 0)continue;
			if( cnt[i] >= 2 && i * 2 <= sum && pp != 1){
				sum -= i * 2;
				tot -= 2;
				cnt[i] -= 2;
				pp += 2;
			}
			else if(cnt[i] >= 1 && i <= sum){
				cnt[i] -= 1;
				tot -= 1;
				sum -= i;
				pp++;
			}
		}
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d%d", &N, &X);
		for(int i = 1; i <= N; i++){
			scanf("%d", D + i);
		}
		sort(D + 1, D + N + 1);
		printf("%d\n", solve());
	}
	return 0;
}

//*/