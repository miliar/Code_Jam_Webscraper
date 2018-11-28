#include<stdio.h>
#include<string.h>
int T;
int t;
int ansline;
int card[4][4];
int ansline2;
int card2[4][4];
bool s;
bool f;
int Ans;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		Ans=0;
		s=false;
		f=false;
		scanf("%d",&ansline);
		
		scanf("%d %d %d %d",&card[0][0],&card[0][1],&card[0][2],&card[0][3]);
		scanf("%d %d %d %d",&card[1][0],&card[1][1],&card[1][2],&card[1][3]);
		scanf("%d %d %d %d",&card[2][0],&card[2][1],&card[2][2],&card[2][3]);
		scanf("%d %d %d %d",&card[3][0],&card[3][1],&card[3][2],&card[3][3]);

		scanf("%d",&ansline2);
		
		scanf("%d %d %d %d",&card2[0][0],&card2[0][1],&card2[0][2],&card2[0][3]);
		scanf("%d %d %d %d",&card2[1][0],&card2[1][1],&card2[1][2],&card2[1][3]);
		scanf("%d %d %d %d",&card2[2][0],&card2[2][1],&card2[2][2],&card2[2][3]);
		scanf("%d %d %d %d",&card2[3][0],&card2[3][1],&card2[3][2],&card2[3][3]);
		
		for(int j=0; j<4; j++){
			if(s==true){
				break;
			}
			for(int i=0; i<4; i++){
				if(card[ansline-1][i] == card2[ansline2-1][j]){
					if(Ans == 0){
					Ans = card[ansline-1][i];
					f=true;
					}else{
					printf("Case #%d: Bad magician!\n",t);
					s = true;
					break;
					}
				}
			}
		}
		if(s==false && f==true){
			printf("Case #%d: %d\n",t,Ans);
		}
		if(f==false){
			printf("Case #%d: Volunteer cheated!\n",t);
		}
	}
}