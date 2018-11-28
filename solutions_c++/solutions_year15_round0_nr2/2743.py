#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ft first
#define sc second
#define INF (int)1e9
typedef long long LL;
using namespace std;

int arr[1005];

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t, n, mx, now, ans;
	scanf("%d",&t);
	for(int tc = 1; tc <= t; tc++ ){
		mx = 0;
		ans = INF;
		scanf("%d",&n);
		for(int i = 0; i < n; i++ ){
			scanf("%d",&arr[i]);
			mx = max(mx,arr[i]);
		}
		for(int i = 1; i <= mx; i++ ){
			now = 0;
//			printf("try %d\n",i);
			for(int j = 0; j < n; j++ ){
				if(arr[j]>i){
					now += (arr[j]-1)/i;
				}
			}
//			printf("%d\n",now+i);
			ans = min(ans,now+i);
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}


