#include<stdio.h>
#include<algorithm>
using namespace std;
int s[1100];
int L[1100];
int R[1100];
int tmp[1100];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		for(int i=0;i<1100;i++)s[i]=L[i]=R[i]=tmp[i]=0;
		int N,K;
		scanf("%d%d",&N,&K);
		for(int i=0;i<=N-K;i++){
			scanf("%d",s+i);
		}
		for(int i=0;i<K;i++)L[i]=R[i]=0;
		for(int i=1;i<=N-K;i++){
			tmp[i-1]=s[i]-s[i-1];
			if(i-1>=K)tmp[i-1]+=tmp[i-1-K];
		}
		for(int i=0;i<N-K;i++){
			L[i%K]=min(L[i%K],tmp[i]);
			R[i%K]=max(R[i%K],tmp[i]);
		}
	//	for(int i=0;i<K;i++)printf("%d %d\n",L[i],R[i]);
		int use=0;
		for(int i=0;i<K;i++){
			use=(use-L[i])%K;
			R[i]-=L[i];
		}
		int rem=(s[0]%K+K)%K-use;
		if(rem<0)rem+=K;
		while(rem){
			int at=0;
			int val=1000000000;
			for(int i=0;i<K;i++){
				if(R[i]<val){
					at=i;val=R[i];
				}
			}
			R[at]++;
			rem--;
		}
		int ret=0;
		for(int i=0;i<K;i++)ret=max(ret,R[i]);
		printf("Case #%d: %d\n",t,ret);
	}
}