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
#define MXN 20010
using namespace std;
int T,n,X,a[MXN],total;
bool flag[MXN];
inline void Init() {
	scanf("%d%d",&n,&X);
	for(int i=1;i<=n;i++) scanf("%d",&a[i]);
}
inline bool cmp(int x,int y){return x>y;}
inline void solve(){
	scanf("%d",&T);
	for(int ii=1;ii<=T;ii++) {
		Init();
		sort(a+1,a+n+1,cmp);
		//for(int i=1;i<=n;i++) printf("%d ",a[i]);printf("\n");
		int tail=2;
		total=0;
		for(int i=1;i<=n;i++) flag[i]=0;
		for(int i=1;i<=n;i++) if(!flag[i]){
			int xx=0;
			for(int j=1;j<=n;j++) if(i!=j&&!flag[j]) {if(a[i]+a[j]<=X) {xx=j;break;}}
			flag[i]=flag[xx]=1;total++;
		}
		printf("Case #%d: %d\n",ii,total);
	}
}
int main(){
    freopen("gcjr2t1.in","r",stdin);freopen("gcjr2t1.out","w",stdout);
    solve();
    return 0;
}
