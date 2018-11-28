#include<iostream>
#include<sstream>
#include<cstring>
#include<fstream>
#include<cmath>
using namespace std;
int checkH();
int checkV();
int clear();
int isVerified();
int lawn[100][100]={0};
int verify[100][100]={0};
int n,m,edge,mheight;
stringstream ss;
ifstream File("B-large.in");
ofstream oFile("output.io");
int main(){
	int i,j,k,t;
	File>>t;
	for(k=0;k<t;k++){
		clear();
		File>>n>>m;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				File>>lawn[i][j];
			}
		}
		checkH();
		checkV();
		/*
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				oFile<<verify[i][j]<<" ";
			}
			oFile<<endl;
		}*/
		oFile<<"Case #"<<k+1<<": ";
		if(isVerified())oFile<<"YES"<<endl;
		else oFile<<"NO"<<endl;
	}
    return 0;
}
int checkH(){
	for(int i=0;i<n;i++){
		mheight=0;
		for(int j=0;j<m;j++){
			if(lawn[i][j]>mheight)mheight=lawn[i][j];
		}
		for(int j=0;j<m;j++){
			if(lawn[i][j]>=mheight)verify[i][j]=1;
		}
	}
}
int checkV(){
	//oFile<<"V::";
	for(int i=0;i<m;i++){
		mheight=0;
		for(int j=0;j<n;j++){
			if(lawn[j][i]>mheight)mheight=lawn[j][i];
		}
	//	oFile<<mheight<<" ";
		for(int j=0;j<n;j++){
			if(lawn[j][i]>=mheight)verify[j][i]=1;
		}
	}
	//oFile<<endl;
}
int clear(){
	for(int i=0;i<100;i++){
		for(int j=0;j<100;j++){
			lawn[i][j]=0;
			verify[i][j]=0;
		}
	}
	n=0;
	m=0;
	edge=0;
}
int isVerified(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(!verify[i][j])return 0;
		}
	}
	return 1;
}
