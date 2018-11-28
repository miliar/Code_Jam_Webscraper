#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;
const int MAXN = 1030;
int a[MAXN],L,R,mid,n,ans,T;

bool chk(int k){
	bool flag;
	for(int cnt,mov = 1;mov < k;++ mov){
		cnt = 0; flag = true;
		for(int i = upper_bound(a,a + n,k - mov) - a;i < n;++ i)
		if(a[i] > k - mov){
			cnt += a[i] / (k - mov) - (a[i] % (k - mov) == 0);
			if(cnt > mov){
				flag = false; break;
			}
		}
		if(flag) return true;
	}
	return false;
}

int main(){
	freopen("input","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int cas = 1;cas <= T;++ cas){
		printf("Case #%d: ",cas);
		scanf("%d",&n);
		L = 1; R = 0;
		for(int i = 0;i < n;++ i){
			scanf("%d",&a[i]);
			if(a[i] > R) R = a[i];
		}
		sort(a,a + n);
		ans = a[n - 1];
		while(L <= R){
			mid = (L + R) >> 1;
			if(chk(mid)){
				ans = mid;
				R = mid - 1;
			}else
				L = mid + 1;
		}
		printf("%d\n",ans);
	}
	return 0;
}
