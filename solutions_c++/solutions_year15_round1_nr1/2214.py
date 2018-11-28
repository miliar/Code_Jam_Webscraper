#include<stdio.h>
int main(){
	freopen("in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	while(scanf("%d",&T)!=EOF){
		for(int i=1;i<=T;i++){
			int a,ta[10001],max=0,ans1=0,ans2=0;
			scanf("%d%d",&a,&ta[1]);
			for(int j=2;j<=a;j++){
				scanf("%d",&ta[j]);
				if(ta[j-1]>ta[j]){
					ans1+=ta[j-1]-ta[j];
					if(ta[j-1]-ta[j]>max){
						max=ta[j-1]-ta[j];
					}
				}
			}
			for(int j=1;j<a;j++){
				if(max>=ta[j])ans2+=ta[j];
				if(max<ta[j])ans2+=max;
				
			}
			
			printf("Case #%d: %d %d\n",i,ans1,ans2);
			
		}
	}
	return 0;
} 
