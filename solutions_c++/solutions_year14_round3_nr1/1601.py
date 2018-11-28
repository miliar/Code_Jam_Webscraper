#include "stdio.h"
#include "string.h"

int main(){
	int t;

	double P,Q;
	double tQ;
	double PQ;
	int two;
	bool ok;
	int ans;
	FILE *fp;
	FILE *fp2;

	fp=fopen("A-large.in","r");
	fp2=fopen("result.txt","w");
	fscanf(fp,"%d",&t);

	for(int i=0;i<t;i++){
		ans=0;
		ok=0;
		fscanf(fp,"%lf/%lf",&P,&Q);
		PQ=P/Q;
		while(PQ<1){
			PQ=PQ*2;
			ans+=1;
		}

		for(int j=0;j<1000000;j++){
			PQ=PQ*2;
			if(PQ==(double)((int)PQ)){
				ok=1;
				break;
			}

		}

		if(ok){
			fprintf(fp2,"Case #%d: %d\n",i+1,ans);
		}else{
			fprintf(fp2,"Case #%d: impossible\n",i+1);
		}
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}