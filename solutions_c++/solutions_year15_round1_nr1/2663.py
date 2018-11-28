#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(){
    int T,it;
    int N;
    int M[10100];
	int min1,min2;
	int j;
	int max;
    
    FILE *in,*out;
    in=fopen("A-large.in","r");
    out=fopen("A-large.out","w");
    //in=fopen("input.txt","r");
    //out=fopen("output.txt","w");
    
    fscanf(in,"%d",&T);
    for(it=1;it<=T;it++){
        fscanf(in,"%d",&N);
        min1=0;
		min2=0;
		max=0;
        for(j=0;j<N;j++){
			fscanf(in,"%d",&M[j]);
			if(j>0){
				if((M[j-1])>M[j]){
					min1=min1+M[j-1]-M[j];
				}
			}
			
			
			if(j>0){
				if(M[j-1]-M[j]>max){
					max=M[j-1]-M[j];
				}
			}
		}
		for(j=0;j<N-1;j++){
			if(M[j]<max){
				min2=min2+M[j];
			}
			else{
				min2=min2+max;
			}
		}
		
        fprintf(out,"Case #%d: %d %d\n",it,min1,min2);
    }
    fclose(in);
    fclose(out);
    
    //system("pause");
    return 1;
}
