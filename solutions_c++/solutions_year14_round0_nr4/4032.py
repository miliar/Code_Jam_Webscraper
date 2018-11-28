#include<stdio.h>
int main(void){
	FILE *f1,*f2;
	f1=fopen("D-large.in","r");
	f2=fopen("output.txt","w");
	float naomi[1003],naomi2[1003];
	float ken[1003];
	float tmp;
	int i,j,n,t,tc;
	int norm,de,sorted;

	fscanf(f1,"%d",&t);

	for(tc=1;tc<=t;tc++){
		fscanf(f1,"%d",&n);
		for(i=0;i<n;i++){
			fscanf(f1,"%f",&naomi[i]);
		}
		for(i=0;i<n;i++){
			fscanf(f1,"%f",&ken[i]);
		}

		for(;;){
			sorted=0;
			for(i=0;i<n-1;i++){
				if(naomi[i]>naomi[i+1]){
					tmp=naomi[i];
					naomi[i]=naomi[i+1];
					naomi[i+1]=tmp;
					sorted=1;
				}
			}
			if(sorted==0){
				break;
			}
		}
		for(;;){
			sorted=0;
			for(i=0;i<n-1;i++){
				if(ken[i]>ken[i+1]){
					tmp=ken[i];
					ken[i]=ken[i+1];
					ken[i+1]=tmp;
					sorted=1;
				}
			}
			if(sorted==0){
				break;
			}
		}

		for(i=0;i<n;i++){
			naomi2[i]=naomi[i];		
		}

		norm=de=0;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(naomi2[j]!=999 && ken[i]<naomi2[j]){
					naomi2[j]=999;
					de++;
					break;
				}
			}
		}		
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(ken[j]!=999 && naomi[i]<ken[j]){
					ken[j]=999;
					norm++;
					break;
				}
			}
		}
		norm=n-norm;	
		fprintf(f2,"Case #%d: %d %d\n",tc,de,norm);
	}
	return 0;
}