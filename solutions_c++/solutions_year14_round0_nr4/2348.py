#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
#include<algorithm>
#include <iomanip>
using namespace std;
int send(long double *n,long double*k,int N){
	int j=0;
	int p=0;
	sort(n,n+N);
	sort(k,k+N);
	for(int i=0;i<N&&j<N;i++){
		while(n[i]>k[j]&&j<N)
			j++;
		if(j<N){
			p++;
			j++;
		}
	}
	return p;
}
int main(){
	std::ios_base::sync_with_stdio(false);
	ifstream fin("D-large.in");
	ofstream fout("sum.txt");
	int T;
	fin>>T;
	int w[50],dw[50];
	long double n[1000],k[1000];
	for(int l=0;l<T;l++){
		int N;fin>>N;
		for(int e=0;e<N;e++){
			fin>>n[e];
		}
		for(int e=0;e<N;e++){
			fin>>k[e];
		}
		w[l]=N-send(n,k,N);
		dw[l]=send(k,n,N);
	}
	for(int l=0;l<T;l++){
		fout<<"Case #"<<l+1<<": "<<dw[l]<<" "<<w[l]<<endl;
	}
}