#include <stdio.h>

void main(void)
{

	int count=0,i=0;
	FILE *input, *output;

	input=fopen("A-small-attempt0.in","rt");
	output=fopen("output.txt","wt");

	fscanf(input,"%d",&count);
	//scanf("%d",&count);

	for(;i<count;i++){
		int first_row,second_row,first_cards[4][4],second_cards[4][4],j,k,correct_card;
		int card_count=0;

		fscanf(input,"%d",&first_row);
		//scanf("%d",&first_row);
		for(j=0;j<4;j++){
			fscanf(input,"%d %d %d %d",&first_cards[j][0],&first_cards[j][1],&first_cards[j][2],&first_cards[j][3]);
			//scanf("%d %d %d %d",&first_cards[j][0],&first_cards[j][1],&first_cards[j][2],&first_cards[j][3]);
		}
		
		fscanf(input,"%d",&second_row);
		//scanf("%d",&second_row);
		for(j=0;j<4;j++){
			fscanf(input,"%d %d %d %d",&second_cards[j][0],&second_cards[j][1],&second_cards[j][2],&second_cards[j][3]);
			//scanf("%d %d %d %d",&second_cards[j][0],&second_cards[j][1],&second_cards[j][2],&second_cards[j][3]);
		}

		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				if(first_cards[first_row-1][j]==second_cards[second_row-1][k]){
					card_count++;
					correct_card=first_cards[first_row-1][j];
				}
			}
		}
		
		if(card_count==1){
			fprintf(output,"Case #%d: %d\n",i+1,correct_card);
			//printf("Case #%d: %d\n",i+1,correct_card);
		}else if(card_count==0){
			fprintf(output,"Case #%d: Volunteer cheated!\n",i+1);
			//printf("Case #%d: Volunteer cheated!\n",i+1);
		}else{
			fprintf(output,"Case #%d: Bad magician!\n",i+1);
			//printf("Case #%d: Bad magician!\n",i+1);
		}
	}

	fclose(input);
	fclose(output);

	return;
}