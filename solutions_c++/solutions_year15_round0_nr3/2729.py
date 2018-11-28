#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;
char str[10005];
int a[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
int flag[4][4];
int getid(char x){
	if(x=='i') return 1;
	else if(x=='j') return 2;
	else return 3;
}
int main(){
	freopen("E:C-small-attempt0.in","r",stdin);
	freopen("E:C-small-attempt0.out","w",stdout);
	flag[1][1]=1;
	flag[1][3]=1;
	flag[2][1]=1;
	flag[2][2]=1;
	flag[3][2]=1;
	flag[3][3]=1;
	int i,j,n,m,T,vcase=0,l,x,tmp,now,vans;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&x);
		scanf("%s",str+1);
		for(i=1;i<x;i++){
			for(j=1;j<=n;j++){
				str[i*n+j]=str[j];
			}
		}
		now=0;tmp=0;vans=0;
		for(i=1;i<=n*x;i++){
			tmp^=flag[now][getid(str[i])];
			now=a[now][getid(str[i])];
			if(vans==0){
				if(tmp==0 && now==1) vans=1;
			}
			else if(vans==1){
				if(tmp==0 && now==3) vans=2;
			}
		}
		if(vans==2 && tmp==1 && now==0) printf("Case #%d: YES\n",++vcase);
		else printf("Case #%d: NO\n",++vcase);
	}
	return 0;
}