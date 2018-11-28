#include "stdio.h"
#include "string.h"


int main(){
	int t;
	int a;
	int b[2][4];
	int c[4];
	int i;
	int h;
	int r;

	FILE *fp;
	FILE *fp2;

	fp=fopen("A-small-attempt0.in","r");
	fp2=fopen("result.txt","w");
	fscanf(fp,"%d",&t);

	for(i=0;i<t;i++){
		h=0;
		fscanf(fp,"%d",&a);
		for(int j=0;j<a-1;j++){
			fscanf(fp,"%d %d %d %d",&c[0],&c[1],&c[2],&c[3]);
		}
		fscanf(fp,"%d %d %d %d",&b[0][0],&b[0][1],&b[0][2],&b[0][3]);
		for(int j=0;j<4-a;j++){
			fscanf(fp,"%d %d %d %d",&c[0],&c[1],&c[2],&c[3]);
		}


		fscanf(fp,"%d",&a);
		for(int j=0;j<a-1;j++){
			fscanf(fp,"%d %d %d %d",&c[0],&c[1],&c[2],&c[3]);
		}
		fscanf(fp,"%d %d %d %d",&b[1][0],&b[1][1],&b[1][2],&b[1][3]);
		for(int j=0;j<4-a;j++){
			fscanf(fp,"%d %d %d %d",&c[0],&c[1],&c[2],&c[3]);
		}



		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(b[0][j]==b[1][k]){
					h++;
					r=b[0][j];
				}
			}
			
		}
		if(h==0){
			fprintf(fp2,"Case #%d: Volunteer cheated!\n",i+1);
		}else if(h>=2){
			fprintf(fp2,"Case #%d: Bad magician!\n",i+1);
		}else{
			fprintf(fp2,"Case #%d: %d\n",i+1,r);
		}
			
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}