#include <stdio.h>

#include <stdlib.h>

#include <math.h>

#include <iostream>

using namespace std;

int min(int a, int b){
	return (a<b)? a : b;
}


int main(){
	
	int T;
	int M,N;
	int **grid;
	int *max1;
	int *max2;
	int check;
	
	FILE *fi;
    if(!(fi=fopen("./inputB", "r"))){
        printf("File \'inputB\' could not be opened!\n");
        exit(-1);
    }
    fscanf(fi, "%d", &T);
	//fscanf(fi, "%lg", z+i);
	
	FILE *fo;
    if(!(fo=fopen("./outputB", "w"))){
        printf("File \'outputB\' could not be opened!\n");
        exit(-1);
    }
    
    for(int i=1; i<=T; i++){
    	fscanf(fi, "%d", &M);
    	fscanf(fi, "%d", &N);
    	grid = (int**)malloc(M*sizeof(int*));
    	for(int j=0; j<=M-1; j++){
    		grid[j]= (int*)malloc(N*sizeof(int));
    		for(int k=0; k<=N-1; k++) fscanf(fi, "%d", grid[j]+k);
    	}
    	max1=(int*)malloc(M*sizeof(int));
    	max2=(int*)malloc(N*sizeof(int));
    	for(int j=0; j<=M-1; j++){
    		max1[j]=0;
    		for(int k=0; k<=N-1; k++) max1[j]=(grid[j][k]>max1[j])? grid[j][k] : max1[j];
    	}
    	for(int k=0; k<=N-1; k++){
    		max2[k]=0;
    		for(int j=0; j<=M-1; j++) max2[k]=(grid[j][k]>max2[k])? grid[j][k] : max2[k];
    	}
    	
    	check=0;
    	for(int j=0; j<=M-1; j++) for(int k=0; k<=N-1; k++) if(grid[j][k]<min(max1[j],max2[k])) check++;
    	
    	fprintf(fo, "Case #%d: ", i);
    	if(check>0) fprintf(fo, "NO");
    	else fprintf(fo, "YES");
    	fprintf(fo, "\n");
    	    	
    	for(int j=0; j<=M-1; j++) free(grid[j]);
    	free(grid);
    	free(max1);
    	free(max2);
    }
		
	fclose(fi);
	fclose(fo);
	
	return 0;
}
