#include<iostream>
#include<fstream>
using namespace std;

bool det(int M,int N,int**L){
	int i=0,j=0,*max_R=new int[M],*max_C=new int[N];
	if(M<=1||N<=1){delete max_R;delete max_C;return true;}

	for(i=0;i<M;i++){
		max_R[i]=L[i][0];
		for(j=1;j<N;j++){
			if(L[i][j]>max_R[i])max_R[i]=L[i][j];
		}
	}
	for(j=0;j<N;j++){
		max_C[j]=L[0][j];
		for(i=1;i<M;i++){
			if(L[i][j]>max_C[j])max_C[j]=L[i][j];
		}
	}
	for(i=0;i<M;i++){
		for(j=0;j<N;j++){
		    if(L[i][j]<max_R[i]&&L[i][j]<max_C[j]){
				delete max_R;delete max_C;return false;
			}
		}
	}
	return true;
}


void main(){
    fstream infile;
	ofstream outfile;
	infile.open("B-large.in");
	outfile.open("output.txt");
	int T,M,N,C;
	int **L;
	infile>>T;
	for(C=1;C<=T;C++){
		infile>>M>>N;
		L=new int*[M];
		for(int i=0;i<M;i++){
			L[i]=new int[N];
			for(int j=0;j<N;j++){
				infile>>L[i][j];
			}
		}

		if(det(M,N,L))outfile<<"Case #"<<C<<": YES"<<endl;
		else outfile<<"Case #"<<C<<": NO"<<endl;

		//delete L
		for(int i=0;i<M;i++){
			delete L[i];
		}
		delete L;
	}
	infile.close();
	outfile.close();
}

