#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int T,n,k,c[200],d[200];
double p[200],ans,t;
void bcd(int x,int y,double z){
	if (x==k+1){
		if (y==k/2)
		t+=z;
	}else{
		if (y+n-x+1==k/2){
			bcd(x+1,y+1,z*p[c[x]]);
		}else if (y==k/2){
			bcd(x+1,y,z*(1-p[c[x]]));
		}else{
			bcd(x+1,y+1,z*p[c[x]]);
			bcd(x+1,y,z*(1-p[c[x]]));
		}
	}
}
void abc(int x,int y){
	if (x==n+1){
		if (y==k){
			t=0;
			bcd(1,0,1);
			ans=max(ans,t);
		}
	}else{
		if (y+n-x+1==k){
			c[y+1]=x;
			abc(x+1,y+1);
		}else if (y==k){
			abc(x+1,y);
		}else{
			c[y+1]=x;
			abc(x+1,y+1);
			c[y+1]=0;
			abc(x+1,y);
		}
	}
}
int main(){
	scanf("%d",&T);
	for (int I=1;I<=T;I++){
		scanf("%d%d",&n,&k);
		for (int i=1;i<=n;i++) scanf("%lf",&p[i]);
		ans=0;
		abc(1,0);
		printf("Case #%d: %.8f\n",I,ans);
	}
    return 0;
}

