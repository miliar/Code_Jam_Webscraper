#include <iostream>
#include <fstream>
using namespace std;
int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t;
	int n,m;
	fin>>t;
	int a[100][100];
	int x[100];
	int y[100];
	for(int k=0;k<t;k++){
		fin>>n>>m;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				fin>>a[i][j];
			}
		}
		for(int i=0;i<n;i++){
			x[i]=0;
			for(int j=0;j<m;j++){
				if(a[i][j]>x[i])x[i]=a[i][j];
			}
		}
		for(int j=0;j<m;j++){
			y[j]=0;
			for(int i=0;i<n;i++){
				if(a[i][j]>y[j])y[j]=a[i][j];
			}
		}
		bool flag=true;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(a[i][j]<x[i]&&a[i][j]<y[j]){
					flag=false;
					break;
				}
			}
		}
		if(flag)fout<<"Case #"<<k+1<<": YES"<<endl;
		else fout<<"Case #"<<k+1<<": NO"<<endl;
	}	
	return 0;
}
