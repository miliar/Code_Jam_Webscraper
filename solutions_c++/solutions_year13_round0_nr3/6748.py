#include <stdio.h>
#include <stdlib.h>
#define MAXN 100

int len,mark[MAXN];

int test(int num){
	int t,nt;

	t=0,nt=num;
	while(nt){
		t=t*10+nt%10;
		nt/=10;
	}
	if(t==num) return 1;
	return 0;
}

void solve(){
	int i,j,t;

	len=0;
	for(i=1;i<400;i++){
		t=i*i;
		if(test(t)==1&&test(i)==1)
			mark[len++]=t;
	}
	return;
}

int main(){
	int i,j,nt,left,right,cnt;

	solve();
	freopen("d:\C-small-attempt2.in","r",stdin);
	freopen("d:\C-small-attempt2.out","w",stdout);
	scanf("%d",&nt);
	for(i=1;i<=nt;i++){
		scanf("%d%d",&left,&right);
		if(left>right){
		    left =left^right;
			right=left^right;
			left =left^right;
		}
		j=0,cnt=0;
		while(j<len){
		    if(mark[j]>=left) break;
			j++;
		}
		while(j<len){
			if(mark[j]>right) break;
			cnt++;
			j++;
		}
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}