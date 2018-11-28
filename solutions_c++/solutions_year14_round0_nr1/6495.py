#include<cstdio>
#include<cstring>

int T;
int R1,R2,Card[5][5];
int Hash[17];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++){
		memset(Hash,0,sizeof Hash);
		scanf("%d",&R1);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++)
				scanf("%d",&Card[i][j]);
			if(i==R1){
				for(int j=1;j<=4;j++)
					Hash[Card[i][j]] = 1;
			}
		}
		int cc = 0;
		int Ans = -1;
		scanf("%d",&R2);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++)
				scanf("%d",&Card[i][j]);
			if(i==R2){
				for(int j=1;j<=4;j++){
					if(Hash[Card[i][j]]==1){
						cc++;
						Ans = Card[i][j];
					}
				}
			}
		}
		printf("Case #%d: ",Case);
		if(cc==0){
			printf("Volunteer cheated!\n");
		}
		else if(cc==1){
			printf("%d\n",Ans);
		}
		else{
			printf("Bad magician!\n");
		}
	}
}
