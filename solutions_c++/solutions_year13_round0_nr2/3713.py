/*
ID: nongeek1
PROG: my
LANG: C++
*/
#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("my.in");
ofstream fout("my.out");

int n,m;
int a[100][100];
int rowMax[100];
int colMax[100];

void solve(){
  fin >> n >> m;
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      fin >> a[i][j];
  
  for(int i=0; i<100; i++)
    rowMax[i] = colMax[i] = 0;
  
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++){
      rowMax[i] = max(rowMax[i], a[i][j]);
      colMax[j] = max(colMax[j], a[i][j]);
    }
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(a[i][j]<rowMax[i] && a[i][j]<colMax[j]){
	fout << "NO" << endl;
	return;
      }
  fout << "YES" << endl;
}
int main(){
  int caseN;
  fin >> caseN;
  for(int index=1; index<=caseN; index++){
    fout << "Case #" << index <<": ";    
    solve();
  }
  return 0;
}
