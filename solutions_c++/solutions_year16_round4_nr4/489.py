#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int T,n,ans;
char a[10][10];
int b[10][10],c[10],temp,fail,d[10];
void cde(int x){
	if (x==n+1) return;
	int dd=0;
	for (int i=1;i<=n;i++)
		if (b[c[x]][i] && d[i]==0){
			dd=1;
			d[i]=1;
			cde(x+1);
			d[i]=0;
		}
	if (dd==0) fail=1;
}
void bcd(int x){
	if (x==n+1){
		cde(1);
	}else{
		for (int i=x;i<=n;i++){
			temp=c[i];c[i]=c[x];c[x]=temp;
			bcd(x+1);
			temp=c[i];c[i]=c[x];c[x]=temp;
		}
	}
}
void abc(int x,int y,int z){
	if (z>=ans) return;
	if (x==n+1){
		fail=0;
		bcd(1);
		if (!fail) ans=min(ans,z);
	}else{
		if (a[x][y]=='1'){
			b[x][y]=1;
			if (y==n) abc(x+1,1,z);
			else abc(x,y+1,z);
		}else{
			b[x][y]=0;
			if (y==n) abc(x+1,1,z);
			else abc(x,y+1,z);
			b[x][y]=1;
			if (y==n) abc(x+1,1,z+1);
			else abc(x,y+1,z+1);
		}
	}
}
int main(){
	scanf("%d",&T);
	for (int I=1;I<=T;I++){
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%s",a[i]+1);
		ans=n*n;
		for (int i=1;i<=n;i++) c[i]=i;
		abc(1,1,0);
		printf("Case #%d: %d\n",I,ans);
	}
    return 0;
}

