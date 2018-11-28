#include <stdio.h>

void main(void){

	FILE *fp,*fp2;
	int times;
	int i=0;
	int j,k,result;
	int matchNum;
	int missNum;
	int row_1;
	int board_1[4][4];
	int row_2;
	int board_2[4][4];
	char *message_1 = "Bad magician!";
	char *message_2 = "Volunteer cheated!";

	fp = fopen("A-small-attempt0.in","r");
	fp2 = fopen("test.out","w");
	if(!fp){
		printf("error.");
		return;
	}
	if(!fp2){
		printf("error.");
		return;
	}

	fscanf(fp,"%d", &times);

	while(times--){
		if(feof(fp)){
				break;
		}
		matchNum=0;
		missNum=0;
		fscanf(fp, "%d", &row_1);
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				fscanf(fp, "%d", &board_1[j][k]);
				
			}		
			
		}
		fscanf(fp, "%d", &row_2);
		
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				fscanf(fp, "%d", &board_2[j][k]);		
			}			
		}		
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){			
				if(board_1[row_1-1][j]==board_2[row_2-1][k]){				
					matchNum++;
					result = board_1[row_1-1][j];
					
				}
				
			}		
		}
		i++;
		if(matchNum==0){
			fprintf(fp2,"Case #%d: %s\n",i, message_2);
		}
		else if(matchNum==1){
			fprintf(fp2,"Case #%d: %d\n",i, result);
		}
		else{
			fprintf(fp2,"Case #%d: %s\n",i, message_1);
		}
		
	
		
		
	}
	
	fclose(fp);

	fclose(fp2);

}