#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#define int64 long long
using namespace std;
int64 p,l,r,mid;
int T,tim,n;
bool check1(int64 mid){
	int i;
	int64 x=mid-1,rank=0;
	for(i=n-1;i>=0;--i){
		if(x)x--,rank+=1ll<<i;
		x/=2;
	}
	return rank+1<=p;
}
bool check2(int64 mid){
	int i;
	int64 x=(1ll<<n)-mid,rank=0;
	for(i=n-1;i>=0;--i){
		if(x)x--;
		else rank+=1ll<<i;
		x/=2;
	}
	return rank+1<=p;
}
int main(){
	freopen("2B.in","r",stdin);
	freopen("2B.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d%I64d",&n,&p);
		tim++;
		l=1; r=1ll<<n;
		while(l<=r){
			mid=(l+r)/2;
			if(check1(mid))l=mid+1;
			else r=mid-1;
		}
		printf("Case #%d: %I64d",tim,l-1-1);
		l=1; r=1ll<<n;
		while(l<=r){
			mid=(l+r)/2;
			if(check2(mid))l=mid+1;
			else r=mid-1;
		}
		printf(" %I64d\n",l-1-1);
	}
}
