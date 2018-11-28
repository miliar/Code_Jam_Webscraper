#include<stdio.h>

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);

	int num[16];
	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++){
		int row;

		scanf("%d",&row);
		for(int i=0;i<16;i++){
			int n;
			scanf("%d",&n);
			if((row-1)*4 <= i && i < row*4){
				num[n-1]=1;
			}else {num[n-1]=0;}
		}

		scanf("%d",&row);
		for(int i=0;i<16;i++){
			int n;
			scanf("%d",&n);
			if((row-1)*4 <= i && i < row*4)num[n-1]++;
		}

		int gn=0,g;
		for(int i=0;i<16;i++){
			if(num[i]==2){
				g=i+1;
				gn++;
				if(gn==2)break;
			}
		}
		if(gn==1) printf("Case #%d: %d\n",t,g);
		else if(gn==0) printf("Case #%d: Volunteer cheated!\n",t);
		else printf("Case #%d: Bad magician!\n",t);
	}
}
