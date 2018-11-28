#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int n;
double a[1010],b[1010];
void solve(int T){
	printf("Case #%d: ",T);
	scanf("%d",&n);
	for(int i=1;i<=n;++i)scanf("%lf",&a[i]);
	sort(a+1,a+n+1);
	for(int i=1;i<=n;++i)scanf("%lf",&b[i]);
	sort(b+1,b+n+1);
	int ans=0,l=1,r=n,ll=1,rr=n;
	while(l<=r){
		if(a[r]>b[rr]){
			--r;--rr;
			++ans;
		}else if(a[l]>b[ll]){
			++l;++ll;
			++ans;
		}else if(a[l]<b[ll]){
			++l;--rr;
		}
	}
	printf("%d ",ans);
	ans=0;l=ll=1;r=rr=n;
	for(int i=1;i<=n;++i)swap(a[i],b[i]);
	while(l<=r){
		if(a[r]>b[rr]){
			--r;--rr;
			++ans;
		}else if(a[l]>b[ll]){
			++l;++ll;
			++ans;
		}else if(a[l]<b[ll]){
			++l;--rr;
		}
	}
	printf("%d\n",n-ans);
} 
int main(){
	freopen("Dlarge.in","r",stdin);
	freopen("Dlarge.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int i=1;i<=test;++i)solve(i);
	return 0;
} 
