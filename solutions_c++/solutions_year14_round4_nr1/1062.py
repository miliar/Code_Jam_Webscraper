#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int a[10001];
int main()
{
	//freopen("PA.txt", "r", stdin);

	freopen("A-large.in", "r", stdin);
	freopen("PA-large.out", "w", stdout);
	int TN, N, ca=1, ans, i, j, K;
	scanf("%d", &TN);
	while(TN--){
		scanf("%d%d", &N, &K);
		for(i=0;i<N;i++){
			scanf("%d", &a[i]);
		}
		sort(a, a+N);
		i=0;j=N-1;
		ans=0;
		while(i<=j){
			if(i==j){
				ans++;break;
			}
			if(a[j]+a[i]>K){
				ans++;j--;
			}
			else if(a[j]+a[i]<=K){
				ans++;i++;j--;
			}
		}
		printf("Case #%d: %d\n", ca++, ans);
	}

	return 0;
}