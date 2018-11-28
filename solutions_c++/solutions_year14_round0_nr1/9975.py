#include<cstdio>

int main(){
	int t,card1[4][4],card2[4][4],k1,k2;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&k1);
		for(int l=0;l<4;l++)
			for(int m=0;m<4;m++){
				scanf("%d",&card1[l][m]);
			}
	        scanf("%d",&k2);
		for(int l=0;l<4;l++)
			for(int m=0;m<4;m++){
                                scanf("%d",&card2[l][m]);
                        }	
		int cas=0;
		int num = 0;
                k1--;k2--;
		for(int l=0;l<4;l++)
			for(int m=0;m<4;m++){
				if(card1[k1][l] == card2[k2][m]){
					num = card1[k1][l];
					cas++;
				}
			}
		printf("Case #%d: ",i);
                if(cas == 0){
			printf("Volunteer cheated!\n");
		}else if(cas == 1){
			printf("%d\n",num);
		}else {
			printf("Bad magician!\n");
		}
	}
}
