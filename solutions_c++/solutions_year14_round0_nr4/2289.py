#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int N=1005;
int T,n,ans1,ans2;
double a[N],b[N];
void calc1(){
	int h1=1,h2=1,r1=n,r2=n;
	while(r1>=h1 && r2>=h2){
		if(a[r1]>b[r2])	r1--,r2--,ans1++;
		else h1++,r2--;
	}
}
void calc2(){
	int h1=1,h2=1,r1=n,r2=n;
	while(r1>=h1 && r2>=h2){
		while(a[h1]>b[h2] && r1>=h1 && r2>=h2)	h2++,r1--;
		if(r1<h1 || r2<h2)	break;
		h1++,h2++,ans2++;
	}
	ans2=n-ans2;
}
int main(){
	scanf("%d",&T);
	for(int tt=1;tt<=T;++tt){
		printf("Case #%d: ",tt);
		ans1=ans2=0;
		scanf("%d",&n);
		for(int i=1;i<=n;++i)	scanf("%lf",&a[i]);
		for(int i=1;i<=n;++i)	scanf("%lf",&b[i]);
		sort(a+1,a+n+1),sort(b+1,b+n+1);
		calc1(),calc2();
		printf("%d %d\n",ans1,ans2);
	}	
	return 0;
}
