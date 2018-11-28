#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
int main(void){

	int t,n,flag;
	int i,j,pick;
	int chk[10]={0,};
	int mult,result;
	FILE *f1,*f2;
	f1=fopen("A-large.in","r+");
	f2=fopen("output.txt","w+");

	fscanf(f1,"%d",&t);
	int cnt=1;
	while(t--){		
		fprintf(f2,"CASE #%d:",cnt++);
		n=mult=pick=flag=0;
		fscanf(f1,"%d",&n);
		for(i=0;i<10;i++){
			chk[i]=0;
		}
		//===
		for(i=1; ;i++){
			result=mult=n*i;		
			for(;mult!=0;){
				pick=mult%10;
				mult/=10;
				chk[pick]=1;
			}
			for(flag=1,j=0;j<10;j++){
				if(chk[j]==0){
					flag=0;
				}
			}
			if(flag==1){
				//printf("i= %d",i);
				fprintf(f2," %d\n",result);			
				break;
			}
			if(n==0||i>7000){
				fprintf(f2," INSOMNIA\n");
				break;
			}
		}
	}
	return 0;
}