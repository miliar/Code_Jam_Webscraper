#include "stdio.h"
#include "string.h"

int main(){
	int t;

	int A,B,K;
	int Ad[10],Bd[10];
	int two,win;
	int ans;
	FILE *fp;
	FILE *fp2;
	int tA,tB;

	fp=fopen("B-small-attempt0 (1).in","r");
	fp2=fopen("result.txt","w");
	fscanf(fp,"%d",&t);

	for(int i=0;i<t;i++){
		fscanf(fp,"%d %d %d",&A,&B,&K);
		ans=0;
		for(int j=0;j<A;j++){
			for(int k=0;k<B;k++){
				win=0;
				tA=j;tB=k;
				for(int l=0;l<10;l++){
					Ad[l]=0;
					Bd[l]=0;
				}
				if(tA>=512){
					Ad[9]=1;
					tA-=512;
				}
				if(tA>=256){
					Ad[8]=1;
					tA-=256;
				}
				if(tA>=128){
					Ad[7]=1;
					tA-=128;
				}
				if(tA>=64){
					Ad[6]=1;
					tA-=64;
				}
				if(tA>=32){
					Ad[5]=1;
					tA-=32;
				}
				if(tA>=16){
					Ad[4]=1;
					tA-=16;
				}
				if(tA>=8){
					Ad[3]=1;
					tA-=8;
				}
				if(tA>=4){
					Ad[2]=1;
					tA-=4;
				}
				if(tA>=2){
					Ad[1]=1;
					tA-=2;
				}
				if(tA>=1){
					Ad[0]=1;
					tA-=1;
				}
				if(tB>=512){
					Bd[9]=1;
					tB-=512;
				}
				if(tB>=256){
					Bd[8]=1;
					tB-=256;
				}
				if(tB>=128){
					Bd[7]=1;
					tB-=128;
				}
				if(tB>=64){
					Bd[6]=1;
					tB-=64;
				}
				if(tB>=32){
					Bd[5]=1;
					tB-=32;
				}
				if(tB>=16){
					Bd[4]=1;
					tB-=16;
				}
				if(tB>=8){
					Bd[3]=1;
					tB-=8;
				}
				if(tB>=4){
					Bd[2]=1;
					tB-=4;
				}
				if(tB>=2){
					Bd[1]=1;
					tB-=2;
				}
				if(tB>=1){
					Bd[0]=1;
					tB-=1;
				}
				two=1;
				for(int l=0;l<10;l++){
					if(Ad[l]==1&&Bd[l]==1){
						win+=two;
					}
					two=two*2;
				}
				if(K>win){
					ans++;
				}
			}
		}

		fprintf(fp2,"Case #%d: %d\n",i+1,ans);

	}

	fclose(fp);
	fclose(fp2);

	return 0;
}

