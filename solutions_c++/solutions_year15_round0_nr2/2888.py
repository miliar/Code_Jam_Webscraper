#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
using namespace std;

const int N = 1005;
const int inf = 1e8;
int n;
int a[N];
int main(){
	freopen("input.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T, Cas = 1; scanf("%d", &T);
	while (T--){
		scanf("%d", &n);
		int mx = 0;
		for(int i = 1; i <= n; i++)scanf("%d", &a[i]), mx = max(a[i], mx);
		int ans = mx;
		for(int i = 1;i < ans && i <= mx; i++){
			int tmp = i;
			for(int j = 1; j <= n; j++)
				if(a[j]>i)
				{
					tmp += a[j]/i-(a[j]%i==0);
					if(tmp>=ans)break;
				}			
			ans = min(ans, tmp);
		}
	
		printf("Case #%d: ", Cas++);
		printf("%d\n",ans);
	}
	return 0;
}
