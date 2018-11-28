#include<stdio.h>
#include<stdlib.h>

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T, i,j,k,cnt=0;
	scanf("%d",&T);
	while(cnt<T){
		int a[17];
		int b[17];
		int r1,r2;
		scanf("%d",&r1);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&k);
				a[k]=i+1;
			}
		}
		scanf("%d",&r2);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&k);
				b[k]=i+1;
			}
		}
		int num=0, k1;
		for(k=1;k<=16;k++){
			if(a[k]==r1&&b[k]==r2){
				num++;
				k1=k;
			}
		}
		printf("Case #%d: ",cnt+1);
		if(num==0) printf("Volunteer cheated!\n");
		else if(num==1) printf("%d\n",k1);
		else if(num>1) printf("Bad magician!\n");
		cnt++;
	}
	return 0;
}
