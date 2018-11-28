#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<iostream>
using namespace std;
__int64 a[1005],ll,rr,mid,now,b[1005],ans;
int vn;
int main(){
	freopen("E:B-large.in","r",stdin);
	freopen("E:B-large.out","w",stdout);
	int i,j,n,m,T,vcase=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){
			scanf("%I64d",&a[i]);
		}
		ll=0,rr=1LL*1e9*1e5;
		ans=-1;
		while(ll<=rr){
			mid=(ll+rr)/2;
			vn=0;
			now=0;
			for(i=1;i<=n;i++){
				now+=(mid+a[i]-1)/a[i];
				if(mid%a[i]==0){
					b[++vn]=i;
				}
			}
			if(now>m-1) rr=mid-1;
			else if(now+vn<m){
				ll=mid+1;
			}
			else{
				ans=b[m-now];
				break;
			}
		}
		printf("Case #%d: %I64d\n",++vcase,ans);
	}
	return 0;
}