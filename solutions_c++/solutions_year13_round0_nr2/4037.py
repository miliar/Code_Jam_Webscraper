#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
int a[101][101];

bool check(int x,int y,int N,int M){
	int i;int flag=0;
	for(i=0;i<M;i++){
		if(a[x][i]>a[x][y]){
			flag++;break;
		}
	}

	for(i=0;i<N;i++){
		if(a[i][y]>a[x][y]){
			flag++;break;
		}
	}
	if(flag==2) return false;
	else return true;
}

int main(){
	int T,N,M,i,j;
	fin>>T;
	int t;
	for(i=0;i<101;i++)
		for(j=0;j<101;j++)
			a[i][j]=0;
	for(t=0;t<T;t++){
		fout<<"Case #"<<t+1<<": ";
		fin>>N>>M;
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				fin>>a[i][j];
		int flag=1;
		for(i=0;i<N&&flag;i++)
			for(j=0;j<M;j++){
				if(check(i,j,N,M)) continue;
				else{
					flag=0;break;
				}
			}
		if(flag==1) fout<<"YES"<<endl;
		else if(flag==0) fout<<"NO"<<endl;
	}
	return 0;
}