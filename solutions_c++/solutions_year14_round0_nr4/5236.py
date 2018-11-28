#include <stdio.h> 
#include <stdlib.h>

#define SWAP(X,Y) {int T=X; X=Y; Y=T; } 
#define ARRAY_MAX 1000;
void init(int permutation[],int n,int r); 
int next(int permutation[],int n,int r); 

void main(void) 
{
	FILE *input,*output;
	int times;
	int permutation[10000]; 
	
	int count=1;
	
	int num=0;
	double *b;
	double *c;
	input = fopen("D-small-attempt1.in","r");
	output = fopen("output.out","w");
	fscanf(input,"%d",&times);
	
	while(times--){
		int max=0;
		int min=0;
		

	int  i,j; 

	for (i=0;i<10000;i++){
		permutation[i]=0;
	}
	num=0;
		fscanf(input,"%d",&num);
		b = (double*)malloc(sizeof(double)*num);
		c = (double*)malloc(sizeof(double)*num);
		init(permutation, num, num); 
		
		for(i=0;i<num;i++){
			fscanf(input,"%lf",&b[i]);
			
		}
		
		for(i=0;i<num;i++){
			fscanf(input,"%lf",&c[i]);
			
		}
	
		
		do 
		{
			int temp=0;
			int tmmp2=0;
			for(i=0;i<num;i++ ) 
			{
				
			
				if(b[i]>=c[permutation[i]-1]){
					temp++;
				}
				if(c[i]>=b[permutation[i]-1]){
					tmmp2++;
					
				}
				
			}
			if(temp>max){
				max=temp;
			}
			if(tmmp2>min){
				min=tmmp2;
			}
		} 
		while(next(permutation,num,num)); 
		
	
			fprintf(output,"Case #%d: %d %d\n",count,max,num-min);
	
		

		free(b);
		free(c);
		
		count++;

	}
	
} 
void init(int permutation[], int n, int r) 
{ 
	int i; 
	for( i = 0 ; i < r ; i++ ) 
	{ 
		permutation[i] = i+1; 
	} 
	for( i = r ; i < n ; i++ ) 
	{ 
		permutation[i] = n+r-i; 
	} 
} 
int next(int permutation[], int n, int r) 
{ 
   int i; 
   int j; 
   int num3=-1; 
   int num2;
   
   for(i=0;i<n;i++) 
   { 
	   if( permutation[i] < permutation[i+1] ) num3 = i; 
   } 
   if(num3==-1) {
	   return 0; 
   }
   num2 = num3+1; 
   for( i = num2+1 ; i < n ; i++ ) 
   { 
      if(permutation[num3] < permutation[i] ){
		  num2 = i; 
	  }
   } 
   SWAP(permutation[num3], permutation[num2]);   
   j = n-num3-1; 
   for(i=0;i<j/2;i++) 
   { 
	   SWAP(permutation[num3+1+i], permutation[num3+j-i]); 
   }  
   j = n-r; 
   for(i=0;i<j/2;i++) 
   { 
      SWAP(permutation[r+i], permutation[r+j-i-1]); 
   } 
   return 1; 
} 