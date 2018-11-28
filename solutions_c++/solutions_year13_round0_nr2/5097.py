#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

ifstream fin;
ofstream fout;

int t,k;
int n,m;
int a[101][101];
int b[101][101];

int max(int no, int len, int type){
	int res=0;
	if(type==1){
		//row
		for(int i=0;i<len;i++){
			res=((res>=a[no][i])?res:a[no][i]);
		}
	}else{
		//col
		for(int i=0;i<len;i++){
			res=((res>=a[i][no])?res:a[i][no]);
		}
	}
	return res;
};

bool equal(int n,int m){
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++){
		if(a[i][j]!=b[i][j]) return false;
	}
	return true;
};

int main(){
	fin.open("B-large.in");
	fout.open("B-large.out");

	fin>>t;
	for(k=0;k<t;k++){
		fin>>n>>m;
		for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			fin>>a[i][j];
			b[i][j]=100;
		}
		int tmp;
		//row
		for(int i=0;i<n;i++){
			tmp=max(i,m,1);
			for(int j=0;j<m;j++){
				b[i][j]=((tmp<b[i][j])?tmp:b[i][j]);
			}
		}
		//col
		for(int j=0;j<m;j++){
			tmp=max(j,n,0);
			for(int i=0;i<n;i++){
				b[i][j]=((tmp<b[i][j])?tmp:b[i][j]);
			}
		}
		//compare
		fout<<"Case #"<<k+1<<": "<<(equal(n,m)?"YES":"NO")<<endl;
		

	}	
	fin.close();
	fout.close();
	return 0;
}