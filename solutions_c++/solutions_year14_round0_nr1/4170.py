#include<stdio.h>
int main(void){
	FILE *f1,*f2;
	f1=fopen("A-small-attempt0.in","r");
	f2=fopen("output.txt","w");
	int deck_1[4][4];
	int deck_2[4][4];
	int tc,t,ans_1,ans_2;
	int i,j,count,result;

	fscanf(f1,"%d",&t);

	for(tc=1;tc<=t;tc++){
		count=0;
		fscanf(f1,"%d",&ans_1);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				fscanf(f1,"%d",&deck_1[i][j]);
			}
		}
		fscanf(f1,"%d",&ans_2);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				fscanf(f1,"%d",&deck_2[i][j]);
			}
		}
		ans_1--;
		ans_2--;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){			
				if(deck_1[ans_1][i] == deck_2[ans_2][j]){
					count++;
					result=deck_1[ans_1][i];
				}
			}
		}
		if(count==1){
			fprintf(f2,"Case #%d: %d\n",tc,result);
		}
		else if(count>1){
			fprintf(f2,"Case #%d: Bad magician!\n",tc);
		}
		else {
			fprintf(f2,"Case #%d: Volunteer cheated!\n",tc);
		}
	}
	return 0;	
}