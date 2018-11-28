#include<stdio.h>
#include<stdlib.h>
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int in=1;in<=T;in++){
		int n,m;
		scanf("%d",&n);
		int ary[100000];
		int ans1=0,big=0;
		for(int i=0;i<n;i++){
			scanf("%d",&ary[i]);
			if(i>0 && ary[i-1]>ary[i]){
				ans1+=(ary[i-1]-ary[i]);
				big=max(big,ary[i-1]-ary[i]);
		//		printf("big=%d\n",big);
			}
		}
		int ans2=0;
		for(int i=0;i<n-1;i++){
			ans2+=min(big,ary[i]);
		}
		printf("Case #%d: %d %d\n",in,ans1,ans2); 
	}
	return 0;
}
