#include<iostream>
#include"stdlib.h"
#include"stdio.h"

using namespace std;
void checkcd(int cd,int* cl);

int clFull(int* cl);

main(void){
	unsigned char t;
	unsigned long n;
	FILE *fpin = NULL, *fpout = NULL;
	
	fpin = fopen("sin.txt","r");
	fpout = fopen("s1out.txt","w");
	
	//cin>>t;
	fscanf(fpin, "%d", &t);
	for(short i=1;i<=t;i++){
		int j=1,numd,num,cd;
		//cin>>n;
		fscanf(fpin, "%d", &n);
	
		int cl[10]={0,};
		while(!clFull(cl)){
			if(n==0){
			//cout<<"case #"<<i<<": INSOMNIA\n";
			fprintf(fpout, "Case #%d: INSOMNIA\n",i);
			break;
			}
			num=j*n;
			numd=num;
			while(num!=0){
				cd=num%10;
				num=num/10;
				checkcd(cd,cl);
		
			}
			
			j++;	
		}
		if(n!=0)
		{
			//cout<<"case#"<<i<<": "<<numd<<"\n";		
			fprintf(fpout, "Case #%d: %d\n", i, numd);
		}
			
	}
	
	fclose(fpin);
	fclose(fpout);

}
int clFull(int* cl){
	int i=0;
	while(i<10){
		if(cl[i]!=1){
			return 0;
		
		}	
		i++;
	}
	return 1;
}
void checkcd(int cd,int* cl){
	cl[cd]=1;
}
