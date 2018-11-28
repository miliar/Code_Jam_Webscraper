#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int t,n,a,b,c,g;
int d[5000],e[5000],f[5000];
int u[15];
int abc(int w,int x,int y,int z,int l,int r){
	if (w==0){
		if (x==1) f[r]=1;
		else if (y==1) f[r]=2;
		else if (z==1) f[r]=3;
		return 1;
	}else{
		if (w%2==1){
			if (x==u[w]-1){
				abc(w-1,u[w-1],u[w-1]+1,u[w-1],l,l+(r-l)/2);
				abc(w-1,u[w-1],u[w-1],u[w-1]+1,l+(r-l)/2+1,r);
			}else if (y==u[w]-1){
				abc(w-1,u[w-1]+1,u[w-1],u[w-1],l,l+(r-l)/2);
				abc(w-1,u[w-1],u[w-1],u[w-1]+1,l+(r-l)/2+1,r);
			}else{
				abc(w-1,u[w-1],u[w-1]+1,u[w-1],l,l+(r-l)/2);
				abc(w-1,u[w-1]+1,u[w-1],u[w-1],l+(r-l)/2+1,r);
			}
		}else{
			if (x==u[w]+1){	
				abc(w-1,u[w-1],u[w-1],u[w-1]-1,l,l+(r-l)/2);
				abc(w-1,u[w-1],u[w-1]-1,u[w-1],l+(r-l)/2+1,r);
			}else if (y==u[w]+1){
				abc(w-1,u[w-1],u[w-1],u[w-1]-1,l,l+(r-l)/2);
				abc(w-1,u[w-1]-1,u[w-1],u[w-1],l+(r-l)/2+1,r);
			}else{
				abc(w-1,u[w-1]-1,u[w-1],u[w-1],l,l+(r-l)/2);
				abc(w-1,u[w-1],u[w-1]-1,u[w-1],l+(r-l)/2+1,r);
			}
		}
	}
}
int main(){
	scanf("%d",&t);
	for (int i=0;i<=12;i++)
		u[i]=(1<<i)/3+(i%2);
	for (int I=1;I<=t;I++){
		scanf("%d%d%d%d",&n,&a,&b,&c);
		printf("Case #%d: ",I);
		if ((a==u[n])+(b==u[n])+(c==u[n])==2){
			abc(n,a,b,c,1,1<<n);
			for (int i=1;i<=(1<<n);i++)
				if (f[i]==1) printf("R");
				else if (f[i]==2) printf("P");
				else printf("S");
			printf("\n");
		}else printf("IMPOSSIBLE\n");		
	}
    return 0;
}

