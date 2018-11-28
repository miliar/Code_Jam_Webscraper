#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define KAN 10

using namespace std;

int* tobcd (unsigned int num);
 
unsigned int func(int t, int*b1,int*b2,unsigned limit);

//int *arr;


unsigned int todec (int*bin);

FILE *f1,*f2;
	





int main(){

	int t=0;
	   unsigned int a=0, b=0, k=0;
	   unsigned int x=0, y=0, ans=0;
	   int *bin1, *bin2;

//	   arr=(int*)malloc(sizeof(int)*KAN);
 
	f1=fopen("B-small-attempt2.in","r");
	f2=fopen("B-small-attempt2out.out","w");

//	f1=fopen("Bin.txt","r");
//	f2=fopen("Bout.txt","w");



	fscanf(f1,"%d",&t);

//
//	  cin>>t;

	for(int aa=0; aa<t; aa++){
		ans=0;
		fscanf(f1,"%u%u%u",&a,&b,&k);
//		bin3=tobcd(k);
		
		for(x=0; x<a; x++){
			
			bin1=tobcd(x);
		
			for(y=0; y<b; y++){
		
			bin2=tobcd(y);
			
			ans+=func(aa+1,bin1,bin2,k);
			
			}
			
		}
		free(bin1); free(bin2);
		fprintf(f2,"Case #%d: %u\n",aa+1, ans);
		
	
    }
	return 0;

}

unsigned int func(int t,int*b1,int*b2,unsigned limit){
	
	int x=0;
	int and;
//	int *and=(int*)malloc(sizeof(int)*KAN);
	unsigned int ans, andand=0;


	for(x=0; x<KAN; x++){
		//and[x]=b1[x]*b2[x];
		if(b1[x]==1 && b2[x]==1) 
	{and=1;
		andand+=and*pow(2.0,x);
		}
	}

//	andand = todec(and);
	
//	andand+=


//	printf("andand=%u, limit=%u\n",andand,limit);
//	free(and);
	if(andand<limit) return 1;

	else return 0;

	return 0;

}


int* tobcd (unsigned int num){

	int x=0, y=0;
	
	int* arr=(int*)malloc(sizeof(int)*KAN);
//	printf("num->%u\n",num);
	for(x=0; x<KAN; x++)
		arr[x]=0;

	x=0;
	while(num>0){
		arr[x++]=num%2;
		num/=2;
	}
	for(y=x-1; y>=0; y--){
//		printf("%d",arr[y]);
	}
//	puts("");

	return arr;
}

unsigned int todec (int*bin){

	int x=0;
	unsigned int ans=0;
	for(x=KAN-1; x>0; x--)
		if(bin[x]==0) ans+=0;
		else	ans+=(bin[x]*pow(2.0,x));

	return ans;

}