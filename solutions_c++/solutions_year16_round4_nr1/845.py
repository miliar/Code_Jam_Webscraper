#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<time.h>
typedef long long lnt;
const lnt mod=1e9+7;
int a[16][4],n;
char ans[16][10000],tmp;
void Sort(int L,int R){
	int M,k,d;
	if(R==L) return;
	M=(L+R)/2;
	d=(R-L+1)/2;
	Sort(L,M);
	Sort(M+1,R);
	int in=-1;
	for(k=L;k<=M;k++){
		if(ans[n][k]<ans[n][k+d]) in=0;
		if(ans[n][k]>ans[n][k+d]) in=1;
	}
	if(in==0) return;
	for(k=L;k<=M;k++){
		tmp=ans[n][k];
		ans[n][k]=ans[n][k+d];
		ans[n][k+d]=tmp;
	}
	return;
}
int main(){
	freopen("pA.in","r",stdin);
	freopen("pA.txt","w",stdout);
	int T,k,R,P,S,t=0,in,i,j;
	scanf("%d",&T);
	while(T--){
		t++;
		scanf("%d%d%d%d",&n,&R,&P,&S);
		in=0;
		for(k=1;k<=3;k++){
			a[0][1]=a[0][2]=a[0][3]=0;
			a[0][k]=1;
			for(i=1;i<=n;i++){
				a[i][1]=a[i-1][1]+a[i-1][2];
				a[i][2]=a[i-1][2]+a[i-1][3];
				a[i][3]=a[i-1][3]+a[i-1][1];
			}
			if(a[n][1]==R&&a[n][2]==P&&a[n][3]==S){
				in=k;
				break;
			}
		}
		printf("Case #%d: ",t);
		if(in==0){
			printf("IMPOSSIBLE\n");
			continue;
		}
		if(in==1) ans[0][0]='R';
		if(in==2) ans[0][0]='P';
		if(in==3) ans[0][0]='S';
		for(k=0;k<n;k++){
			for(i=0;i<(1<<k);i++){
				if(ans[k][i]=='R'){
					ans[k+1][2*i]='R';
					ans[k+1][2*i+1]='S';
				}
				if(ans[k][i]=='P'){
					ans[k+1][2*i]='P';
					ans[k+1][2*i+1]='R';
				}
				if(ans[k][i]=='S'){
					ans[k+1][2*i]='S';
					ans[k+1][2*i+1]='P';
				}
			}
		}
		Sort(0,(1<<n)-1);
		for(k=0;k<(1<<n);k++) printf("%c",ans[n][k]);
		puts("");
	}
}
