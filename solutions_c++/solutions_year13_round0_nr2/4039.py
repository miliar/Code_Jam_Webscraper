#include<iostream>
#include<fstream>
#include <algorithm>
using namespace std;
ifstream fin("in");
ofstream fout("out");
int lawn[100][100];
int row[100];
int column[100];

int main(){
  int cases;
  fin >> cases;
  for (int i=1; i<=cases; i++){
    int N, M;
    fin >> N>> M;
    for (int j=0;j<N;j++){
      row[j]=0;
    }
    for (int j=0;j<M;j++){
      column[j]=0;
    }
    for (int j=0; j<N;j++){
      for (int k=0; k<M; k++){
	fin >>lawn[j][k];
	if (lawn[j][k]>column[k]){
	  column[k]=lawn[j][k];
	}
	if (lawn[j][k]>row[j]){
	  row[j]=lawn[j][k];
	}
      }
    }
    bool b=true;
    for (int j=0; j<N; j++){
      for (int k=0; k<M; k++){
	if (lawn[j][k]<row[j] && lawn[j][k]<column[k]){
	  b=false;
	  break;
	}
      }
      if (b==false) break;
    }
    if (b==false){
      fout<<"Case #"<<i<<": NO"<<endl;
    } else {
      fout<<"Case #"<<i<<": YES"<<endl;
    }
  }
  return 0;
}
    
