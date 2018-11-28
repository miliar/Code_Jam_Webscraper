#include <cstring>
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
double a[10005];
double b[10005];
int T,n;
inline bool cmp(const double  &x,const double  &y){
	return x>y;
}
int main(){
	//freopen("D-large.in","r",stdin);
	//	freopen("D-large.out","w",stdout);
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%lf",&a[i]);
		sort(a,a+n);
		for (int i=0;i<n;i++) scanf("%lf",&b[i]);
		sort(b,b+n);
		int now=0;
		int ans2=0;
		for (int i=0;i<n;i++){
			if(now>=n) break;
			while(now<n&&b[now]<a[i]) now++;
			if(now<n) {ans2++;now++;}
			if(now>=n) break;
		}
		ans2=n-ans2;
		int ans1=0;
		now=0;
		for (int i=0;i<n;i++){
			if(now>=n) break;
			while(now<n&&a[now]<b[i]) now++;
			if(now<n) {ans1++;now++;}
			if(now>=n) break;
		}
		printf("Case #%d: %d %d\n",ca++,ans1,ans2);
	}
	return 0;
}

