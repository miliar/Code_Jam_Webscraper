#include <iostream>
#include <cstdio>

using namespace std;

int a[2000];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n ;i++){
			scanf("%d", &a[i]);
		}
		int ans = 1000;
		for (int i = 1; i <= 1000; i++){
			int pans = 0;
			for (int j = 1; j <= n; j++){
				pans += (a[j] - 1) / i;
			}
			if (pans + i < ans) ans = pans + i;
		}
		
		printf("Case #%d: ", t);
		printf("%d\n",ans);
	}
	return 0;
}
