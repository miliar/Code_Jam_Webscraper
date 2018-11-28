#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
typedef long long int64;
const int maxn=1000100, oo=1000100000;
//const int64 oo64=10000000000000LL;
int64 floordiv(int64 x, int64 y);
int64 ceildiv(int64 x, int64 y) {
	return x>0? (x-1)/y+1: -floordiv(-x,y);
}
int64 floordiv(int64 x, int64 y) {
	return x>=0? x/y: -ceildiv(-x,y);
}

int n,m;
int64 sum[maxn];

int64 coef[maxn], lb[maxn], ub[maxn];
bool check(int pos, int64 diff) {
	//printf("check %d %I64d\n",pos,diff);
	fill(coef+1,coef+n+1,0LL);
	int64 psum=0;
	for(int i=pos+m;i<=n;i++) {
		//sum[i-m]-psum == sum[i+1-m]-(psum-coef[i-m]+coef[i])
		//sum[i-m]==sum[i+1-m]+coef[i-m]-coef[i]
		coef[i] = sum[i+1-m]+coef[i-m]-sum[i-m];
		psum = psum-coef[i-m]+coef[i];
	}
	psum=0;
	for(int i=pos-1;i>=1;i--) {
		//sum[i]-(psum-coef[i+m]+coef[i]) == sum[i+1]-psum
		//sum[i]+coef[i+m]-coef[i]==sum[i+1]
		coef[i] = sum[i]+coef[i+m]-sum[i+1];
		psum = psum-coef[i+m]+coef[i];
	}
	
	//for(int i=1;i<=n;i++)
	//	printf("%lld ",coef[i]);puts("");
	
	for(int i=1;i<=n;i++) {
		int var=((i-pos)%m+m)%m+1;
		lb[var]=-coef[i];
		ub[var]=diff-coef[i];
		//printf("%I64d<=x[%d]-x[1]<=%I64d\n",-coef[i],var,diff-coef[i]);
	}
	for(int i=1;i<=n;i++) {
		int var=((i-pos)%m+m)%m+1;
		lb[var]=max(lb[var], -coef[i]);
		ub[var]=min(ub[var], diff-coef[i]);
		//printf("%I64d<=x[%d]-x[1]<=%I64d\n",-coef[i],var,diff-coef[i]);
	}
	//for(int i=1;i<=m;i++)
	//	printf("%I64d<=x[%d]-x[1]<=%I64d\n",lb[i],i,ub[i]);
	//lb[var]+x[1]<=x[var]<=ub[var]+x[1]
	//x[1]+..+x[m]=sum[pos]

	if(!(lb[1]<=0 && 0<=ub[1]))
		return false;
	int64 slb=0, sub=0;
	for(int i=2;i<=m;i++) {
		if(lb[i]>ub[i])
			return false;
		slb+=lb[i], sub+=ub[i];
	}

	//printf("%lld<=%lld\n",ceildiv(sum[pos]-sub,m), floordiv(sum[pos]-slb,m));
	//slb+m*x[1] <= sum[pos] <= sub+m*x[1]
	return ceildiv(sum[pos]-sub,m) <= floordiv(sum[pos]-slb,m);
}
bool check(int64 diff) {
	for(int i=1;i+m-1<=n;i++)
		if(check(i,diff))
			return true;

	reverse(sum+1, sum+n-m+2);
	bool ans=false;
	for(int i=1;i<=m && !ans;i++)
		if(check(i,diff))
			ans=true;
	reverse(sum+1, sum+n-m+2);
	return ans;
	//return false;
}
void testcase() {
	scanf("%d%d",&n,&m);
	//printf("XX");
	for(int i=1;i<=n-m+1;i++) {
		int x;
		scanf("%d",&x);
		//printf("x=%d\n",x);
		sum[i]=x;
	}
	int64 low=0, high=1000000000;
	while(low<high) {
		int64 mid=(low+high)/2;
		if(check(mid))
			high=mid;
		else
			low=mid+1;
	}
	printf("%I64d\n",low);
	//check(5,5);
}
int main() {

	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		testcase();
	}
	scanf("%*s");
	return 0;
}
