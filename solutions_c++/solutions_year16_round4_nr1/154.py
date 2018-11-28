#include <bits/stdc++.h>
using namespace std;
int Test,N,M;
int a[3],b[3];
int res[10010],ans[10010];
bool check(){
	memset(b,0,sizeof(b));
	for (int i=1;i<=M;i++)
		b[res[i]]++;
	for (int i=0;i<3;i++)
		if (b[i]!=a[i])return 0;
	return 1;
}
bool small (int *A,int *B,int len){
	for (int i=0;i<len;i++){
		if (A[i]<B[i])return 1;
		if (A[i]>B[i])return 0;
	}
	return 0;
}
void work(int l,int r,int now){
	if (l==r){res[l]=now;return;}
	int mid=(l+r)>>1;
	work(l,mid,now);
	work(mid+1,r,(now+1)%3);
	if (small(res+mid+1,res+l,r-mid))
		for (int i=l;i<=mid;i++)
			swap(res[i],res[i-l+mid+1]);
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		printf("Case #%d: ",tt);
		scanf("%d%d%d%d",&N,&a[1],&a[0],&a[2]);
		M=1<<N;
		bool haveans=0;
		work(1,M,0);
		if (check()&&(!haveans||small(res+1,ans+1,M)))
			memcpy(ans,res,sizeof(ans)),haveans=1;
		work(1,M,1);
		if (check()&&(!haveans||small(res+1,ans+1,M)))
			memcpy(ans,res,sizeof(ans)),haveans=1;
		work(1,M,2);
		if (check()&&(!haveans||small(res+1,ans+1,M)))
			memcpy(ans,res,sizeof(ans)),haveans=1;
		if (haveans){
			for (int i=1;i<=M;i++){
				if (ans[i]==0)printf("P");
				if (ans[i]==1)printf("R");
				if (ans[i]==2)printf("S");
			}
			printf("\n");
		}
		else printf("IMPOSSIBLE\n");
	}
}