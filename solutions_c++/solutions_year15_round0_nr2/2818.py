#include<iostream>
#include<queue>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>

using namespace std;

int a[2000];

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++cas){
		int n;
		scanf("%d",&n);
		for(int i = 1;i <= n;++i)
			scanf("%d",&a[i]);
		int ans = 0x3f3f3f3f;
		for(int i = 1;i <= 1000;++i){
			int sum = i;
			for(int j = 1;j <= n;++j){
				int t = ceil(a[j] * 1.0 / i) - 1;
				sum += t;
			}
			ans = min(ans,sum);
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

