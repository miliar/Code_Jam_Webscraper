#include<cstdio>
#include<algorithm>
#define MX 10000000
using namespace std;
int tmp[MX];
int rev(int a) {
	int x=0;
	for(;a;) {
		x*=10;
		x+=a%10;
		a/=10;
	}
	return x;
}
int main () {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<MX;i++) tmp[i]=0;
		tmp[1]=1;
		for(int i=1;i<=n;i++) {
			if(tmp[i]) {
				if(tmp[i+1]==0) tmp[i+1]=tmp[i]+1;
				else tmp[i+1]=min(tmp[i]+1,tmp[i+1]);
				int x=rev(i);
				if(tmp[x]==0) tmp[x]=tmp[i]+1;
				else tmp[x]=min(tmp[i]+1,tmp[x]);
			}
		}
		printf("Case #%d: %d\n",t+1,tmp[n]);
	}
	return 0;
}