#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstring>
#include<math.h>
using namespace std;
int max(int *A, int size){
	int largest=A[0];
	for(int i=0;i<size;i++)
		largest=largest>A[i]?largest:A[i];
	return largest;
}
int min(int *A, int size){
	int least=A[0];
	for(int i=0;i<size;i++)
		least=least<A[i]?least:A[i];
	return least;
}
void refill(int*A, int N, int M, int s){
	int rowfill[N],colfill[M];
	for(int i=0;i<N;i++){
		int check=0;
		for(int j=0;j<M;j++)
			if(A[i*M+j]==s)
				check++;
		if(check==M)	rowfill[i]=1;
		else		rowfill[i]=0;
		}
	for(int j=0;j<M;j++){
		int check=0;
		for(int i=0;i<N;i++)
			if(A[i*M+j]==s)
				check++;
		if(check==N)	colfill[j]=1;
		else		colfill[j]=0;
		}
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++)
			if(rowfill[i] || colfill[j])
				A[i*M+j]++;
		}
}
int checklevel(int *A, int N, int M, int s){
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			if(A[i*M+j]==s)
				return 1;
	return 0;
}
const char* isitpossible(int *A, int N, int M){
	int mini,maxi;
	mini=min(A,N*M);
	maxi=max(A,N*M);
	//list total no's
	for(int s=mini;s<=maxi;s++){
		refill(A,N,M,s);
		if(checklevel(A,N,M,s))
			return "NO";
		}
	return "YES";
}
int main(){
	int T,N,M;
	int Tposi,Tposj;
	cin>>T;
	for(int t=0;t<T;t++){
		Tposi=-1; Tposj=-1;
		cin>>N>>M;
		int *A;
		A = (int*) malloc(sizeof(int)*N*M);
		for(int _i=0;_i<N;_i++)
			for(int _j=0;_j<M;_j++)
				cin>>A[_i*M+_j];	
		cout<<"Case #"<<t+1<<": "<<isitpossible(A,N,M)<<endl;
		free(A);
	}
}
