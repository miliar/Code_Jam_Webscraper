#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <time.h>
#define MXN 1010
using namespace std;
int T,n,total,total2;
double a[MXN],b[MXN];
bool flag[MXN];
inline void Init() {
	scanf("%d",&n);
	for(int i=1;i<=n;i++) scanf("%lf",&a[i]);
	for(int i=1;i<=n;i++) scanf("%lf",&b[i]);
}
inline void Find1() { //war
	int noww=1;
	for(int i=1;i<=n;i++) flag[i]=0;
	for(int i=1;i<=n;i++) {
		int tmp=0;
		while(noww<=n) {if(b[noww]>a[i]&&!flag[noww]) {tmp=noww;break;}noww++;}
		if(tmp) {
			noww++;
			flag[tmp]=1;
		}
		else total++;
	}
}
inline void Find2() { //deceitful
	int tail=1;
	for(int i=1;i<=n;i++) flag[i]=0;
	for(int i=1;i<=n;i++) if(a[i]>b[tail]) {
		total2++;tail++;
	}
}
inline bool cmp(double x,double y){return x<y;}
inline void solve(){
	scanf("%d",&T);
	for(int ii=1;ii<=T;ii++) {
		Init();
		sort(a+1,a+n+1,cmp);
		sort(b+1,b+n+1,cmp);
		//for(int i=1;i<=n;i++) printf("%.3lf ",a[i]);printf("\n");
		//for(int i=1;i<=n;i++) printf("%.3lf ",b[i]);printf("\n");
		total=total2=0;
		Find1();
		Find2();
		printf("Case #%d: %d %d\n",ii,total2,total);
	}
}
int main(){
	freopen("gcj14D.in","r",stdin);freopen("gcj14D.out","w",stdout);
	solve();
	return 0;
}
