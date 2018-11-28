#include<bits/stdc++.h>
using namespace std;
char s[100];
const int fac[10]={1,1,2,6,24};
bool gm[10],gp[10];
bool cal(int op,int now,int n){
	if(now==n) return true;
	bool res=true;
	for(int i=0;i<n;i++){
		if(!gp[i]){
			int c=0;
			gp[i]=true;
			for(int j=0;j<n;j++){
				if((op&(1<<i*n+j))&&!gm[j]){
					gm[j]=true;
					c++;
					if(!cal(op,now+1,n)) res=false;
					gm[j]=false;
				}
			}
			gp[i]=false;
			if(!c||!res) return false;
		}
	}
	return true;
}
int main(){
	int T,p[4]={0,1,2,3};
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int n,now=0,ans=16;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s",s);
			for(int j=0;j<n;j++){
				if(s[j]=='1') now|=1<<(i*n+j);
			}
		}
		for(int i=0;i<(1<<n*n);i++){
			if((i&now)!=now) continue;
			int cst=0;
			for(int j=0;j<n*n;j++){
				if((i^now)&(1<<j)) cst++;
			}
			if(cal(i,0,n)) ans=min(ans,cst);
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}