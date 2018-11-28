#include <iostream>
#include <cstdio>
using namespace std;




int A[1001][1001];
int B[1001][1001];

int solve (int N, int M)
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
			B[i][j]=0;
	}

	int max=0;

	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
			if(max<A[i][j])max=A[i][j];
	}

	


	//First row check
	for(int t=max;t>0;t--){
	for(int k=0;k<M;k++) 
	{
		int same=0;
			for(int l=0;l<N;l++){
				if(A[l][k]<=t)
					same++;
				else
					break;
			}

			if(same==N)
			{for(int l=0;l<N;l++) B[l][k]=t;	}		


	}

	/*Last row check

	for(int k=0;k<M;k++) 
	{
		int same=0;
			for(int l=N-2;l>=0;l--){
				if(A[l][k]==A[N-1][k])
					same++;
				else
					break;
			}

			for(int l=N-1;l>=N-1-same;l--) B[l][k]=1;			

		
	}*/

	//First Column Check

	for(int k=0;k<N;k++) 
	{
		int same=0;
			for(int l=0;l<M;l++){
				if(A[k][l]<=t)
					same++;
				else
					break;
			}

			if(same==M){
				for(int l=0;l<M;l++) B[k][l]=t;			}
    }

	//Last column check

	/*for(int k=0;k<N;k++) 
	{
		int same=0;
			for(int l=M-2;l>=0;l--){
				if(A[k][l]==A[k][M-1])
					same++;
				else
					break;
			}

			for(int l=M-1;l>=M-1-same;l--) B[k][l]=1;			
    }*/

	}

	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
			if(B[i][j]!=A[i][j]) return 0;

		
	}

	return 1;

}


int main()
{
	FILE * fin;
    FILE * fout;

	int N, M;

	

	fin=fopen("BB-large.in","r");
	fout=fopen("BB-large.out", "w");

	

	int iter=0;

	char * res = " ";
	
	fscanf(fin,"%d\n", &iter);

		

	for(int j=0;j<iter;j++) {
      
    fscanf(fin, "%d %d\n", &N, &M);

	for(int i=0;i<N;i++) {
		for(int k=0;k<M;k++)
		{
		fscanf(fin, "%d", &A[i][k]);
		}		
	} 

	for(int i=0;i<N;i++) {
		for(int k=0;k<M;k++)
		{
	    	//printf("%d ",A[i][k]);
		}

		//printf("\n");
	}
	//printf("\n");
    
	if(solve(N,M))
		res="YES";
	else
		res="NO";

	fprintf(fout,"Case #%d: %s\n", j+1, res);
	}
    

	fclose(fin);
	fclose(fout);

	return 0;
}

