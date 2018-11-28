#include<iostream>

using namespace std;

int main(){
	static int ncases,ans1,ans2,arrangement1[4][4],arrangement2[4][4],prediction,pcnt;
	FILE *infile;
	infile=fopen("in.txt","r");
	FILE *outfile;
	outfile=fopen("out.txt","w");
	fscanf(infile,"%d",&ncases);
	for(int caseno=1;caseno<=ncases;caseno++){
		pcnt=0;

		//read 1st answer
		fscanf(infile,"%d",&ans1);
		ans1--;

		//read 1st arrangement
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				fscanf(infile,"%d",&arrangement1[i][j]);
		}

		//read 2nd answer
		fscanf(infile,"%d",&ans2);
		ans2--;

		//read 2nd arrangement
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				fscanf(infile,"%d",&arrangement2[i][j]);
		}

		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arrangement1[ans1][i]==arrangement2[ans2][j]){
					prediction=arrangement2[ans2][j];
					pcnt++;
				}
			}
		}

		if(pcnt==0)
			fprintf(outfile,"Case #%d: Volunteer cheated!\n",caseno);
		else if(pcnt==1)
			fprintf(outfile,"Case #%d: %d\n",caseno,prediction);
		else
			fprintf(outfile,"Case #%d: Bad magician!\n",caseno);
	}
	fclose(infile);
	fclose(outfile);
	getchar();
}