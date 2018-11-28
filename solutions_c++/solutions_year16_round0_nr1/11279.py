#include "stdio.h"
int sub[10]={0,1,2,3,4,5,6,7,8,9};
int flag[10];
void aa(FILE *fp2,int n,int ncase);
int main(){
	int T,n,ncase=1;
	FILE *fp1,*fp2;
	fp1=fopen("d:\\A-small-attempt1.in","r");
	fp2=fopen("d:\\A-small-attempt1.out","w+");
	fscanf(fp1,"%d",&T);
	while(T--){
		fscanf(fp1,"%d",&n);
		if(n==0){
			fprintf(fp2,"Case #%d: INSOMNIA\n",ncase++);
			continue;
		}
		aa(fp2,n,ncase++);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}
void aa(FILE *fp2,int n,int ncase){
	int i,sum,j,sum1,k,num=0;
	for(i=1;;i++){
		sum=n*i;
		sum1=sum;
		while(sum>0){
			k=sum%10;
			for(j=0;j<10;j++){
				if(flag[j]==1) continue;
				if(k==sub[j]){
					flag[j]=1;
					break;
				}
			}
			sum=sum/10;
		}
		for(j=0;j<10;j++){
			if(!flag[j]) break;
		}
		if(j>9) break;
	}
	for(i=0;i<10;i++) flag[i]=0;
	fprintf(fp2,"Case #%d: %d\n",ncase,sum1);
}
