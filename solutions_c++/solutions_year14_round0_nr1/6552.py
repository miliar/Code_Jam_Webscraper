#include<stdio.h>

int main(){
	int card_mat[4][4],cases=1,prev_ans[4],t,ans,i,j,magnum;
	scanf("%d",&t);
	while(cases++<=t){
		scanf("%d",&ans);
		int matches=0;
		//Scan Card Matrix
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				scanf("%d",&card_mat[i][j]);
		}
/*
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				printf("%d ",card_mat[i][j]);
			printf("\n");
		}
*/
		//Store the 1st answer array.
		for(i=0;i<4;i++){
				prev_ans[i]=card_mat[ans-1][i];
		}
		//Get next answer from volunteer
		scanf("%d",&ans);
		//Scan the second card matrix
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				scanf("%d",&card_mat[i][j]);
		}
/*
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				printf("%d ",card_mat[i][j]);
			printf("\n");
		}
*/
		//Check for overlaps in the rows corresponding to the two answers
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				if(card_mat[ans-1][i]==prev_ans[j]){
							matches++;
							magnum=prev_ans[j];//Magic Number
			}
		}
		//printf("Case #%d:Match=%d\t Magnum=%d\n",cases-1,matches,magnum);
		//No match is found in the two rows.Magician you are of no use
		if(matches==0)
			printf("Case #%d: Volunteer cheated!\n",cases-1);
		//Match Found.Magician,good work
		else if(matches==1)
			printf("Case #%d: %d\n",cases-1,magnum);
		//More than one match found.Magician,learn probability and check your odds of winning.	
		else
			printf("Case #%d: Bad magician!\n",cases-1);
	}
	return 0;
}
