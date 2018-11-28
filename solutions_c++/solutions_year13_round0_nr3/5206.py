#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int isPalin(int num){
	int orig=num;
	int rev=0;
	int copy=num;

	while(num>0){
		copy=num%10;
		rev=copy+(rev*10);
		num=num/10;
	}
	if(rev==orig){
		return 1;
	}
	return 0;	
}


int compute(int num){
	double val=sqrt(num);
	if(val!=(int)val){
		return 0;
	}	
	if(isPalin(num)==0){
	return 0;
	}
	if(isPalin((int)val)==0){
		return 0;
	}
	return 1;

}


int main(){
	int k=1,num;
	FILE*in=fopen("C-small-attempt0.in","r");
	FILE*out=fopen("output.txt","w");
	fscanf(in,"%d",&num);
	while(k<=num){
	int start,finish;
	fscanf(in,"%d %d",&start,&finish);
	int i,count=0;
	for(i=start;i<=finish;i++){
		if(i%10!=0){
		if(compute(i)==1){
			count++;
		}
	}
	}
	fprintf(out,"Case #%d: %d\n",k,count);
	k++;
	}

}




