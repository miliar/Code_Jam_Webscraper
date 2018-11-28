#include "stdio.h"
#include "string.h"


int main(){
	int t;
	int N;
	double Nao[10],Ken[10];
	double Kend[10];
	double tmp;
	int w;

	FILE *fp;
	FILE *fp2;

	fp=fopen("D-small-attempt0.in","r");
	fp2=fopen("result.txt","w");
	fscanf(fp,"%d",&t);

	for(int i=0;i<t;i++){
		fscanf(fp,"%d",&N);
		switch(N){
		case 10:
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3],&Nao[4],&Nao[5],&Nao[6],&Nao[7],&Nao[8],&Nao[9]);
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3],&Ken[4],&Ken[5],&Ken[6],&Ken[7],&Ken[8],&Ken[9]);
			break;
		case 9:
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3],&Nao[4],&Nao[5],&Nao[6],&Nao[7],&Nao[8]);		
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3],&Ken[4],&Ken[5],&Ken[6],&Ken[7],&Ken[8]);
			break;
		case 8:
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3],&Nao[4],&Nao[5],&Nao[6],&Nao[7]);
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3],&Ken[4],&Ken[5],&Ken[6],&Ken[7]);
			break;
		case 7:
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3],&Nao[4],&Nao[5],&Nao[6]);
			fscanf(fp,"%lf %lf %lf %lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3],&Ken[4],&Ken[5],&Ken[6]);
			break;
		case 6:
			fscanf(fp,"%lf %lf %lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3],&Nao[4],&Nao[5]);
			fscanf(fp,"%lf %lf %lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3],&Ken[4],&Ken[5]);
			break;
		case 5:
			fscanf(fp,"%lf %lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3],&Nao[4]);
			fscanf(fp,"%lf %lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3],&Ken[4]);
			break;
		case 4:
			fscanf(fp,"%lf %lf %lf %lf",&Nao[0],&Nao[1],&Nao[2],&Nao[3]);
			fscanf(fp,"%lf %lf %lf %lf",&Ken[0],&Ken[1],&Ken[2],&Ken[3]);
			break;
		case 3:
			fscanf(fp,"%lf %lf %lf",&Nao[0],&Nao[1],&Nao[2]);
			fscanf(fp,"%lf %lf %lf",&Ken[0],&Ken[1],&Ken[2]);
			break;
		case 2:
			fscanf(fp,"%lf %lf",&Nao[0],&Nao[1]);
			fscanf(fp,"%lf %lf",&Ken[0],&Ken[1]);
			break;
		case 1:
			fscanf(fp,"%lf",&Nao[0]);
			fscanf(fp,"%lf",&Ken[0]);
			break;
			}
		for(int j=0;j<N;j++){
			for(int k=0;k<N;k++){
				if(Nao[j]<Nao[k]){
					tmp=Nao[k];
					Nao[k]=Nao[j];
					Nao[j]=tmp;
				}
				if(Ken[j]<Ken[k]){
					tmp=Ken[k];
					Ken[k]=Ken[j];
					Ken[j]=tmp;
				}
			}
		}
		for(int j=0;j<N;j++){
			Kend[j]=Ken[j];
		}
		//d war
		w=0;
		for(int j=0;j<N;j++){
			for(int k=N-1;k>0-1;k--){
				if(Nao[j]>Ken[k]){//win
					w++;
					Ken[k]=999;
					break;
				}
				if(k==0){
					for(int l=N-1;l>0-1;l--){
						if(Ken[l]!=999){
							Ken[l]=999;
							break;
						}
					}
				}
			}

		}
		for(int j=0;j<N;j++){
			Ken[j]=Kend[j];
		}
		fprintf(fp2,"Case #%d: %d",i+1,w);
		//war
		w=0;
		for(int j=N-1;j>0-1;j--){
			for(int k=0;k<N;k++){
				if(Nao[j]<Ken[k]){//loss	
					Ken[k]=-999;
					break;
				}
				if(k==N-1){
					for(int l=0;l<N;l++){
						if(Ken[l]!=-999){
							w++;
							Ken[l]=-999;
							break;
						}
					}
				}
			}
		}
		fprintf(fp2," %d\n",w);
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}