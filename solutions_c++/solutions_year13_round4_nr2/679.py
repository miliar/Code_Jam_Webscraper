#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;
typedef long long ll;

int check(ll mid,ll p,int n)
{
	ll t=mid,ans=0;
	while(t){
		n--;
		ans+=(1LL<<n);
		t=(t-1)/2;
	}
	if(ans<p) return 1;
	return 0;
}

int solve(ll mid,ll p, int n)
{
	ll t=(1LL<<n)-mid-1,ans=0;
	while (t) {
		n--;
		t = (t - 1) / 2;
	}
	ans=1LL<<n;
	if(ans<=p) return 1;
	return 0;
}
int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,n,ri=1;
	ll p;
	scanf("%d",&T);
	while(T--){
		scanf("%d%lld",&n,&p);
		ll left=0,right=(1LL<<n)-1,mid,si;
		while(left<=right){
			mid=(left+right)/2;
			if(check(mid,p,n)){
				si=mid;
				left=mid+1;
			}else right=mid-1;
		}
		left = 0, right = (1LL << n) - 1;
		ll sj;
		while (left <= right) {
			mid = (left + right) / 2;
			if (solve(mid, p, n)) {
				sj = mid;
				left = mid + 1;
			} else
				right = mid - 1;
		}
		printf("Case #%d: %lld %lld\n",ri++,si,sj);
	}
}
