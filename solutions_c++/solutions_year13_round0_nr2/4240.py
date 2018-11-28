#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
using namespace std;

int check(int table[], int n, int m) {
  int rN[n], rM[m];
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++) {
      if(table[i*m+j]>rN[i]) rN[i]=table[i*m+j];
      if(table[i*m+j]>rM[j]) rM[j]=table[i*m+j];
    }
  for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
      if(table[i*m+j]<rN[i] && table[i*m+j]<rM[j]) return 1;
  return 1;
}

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int C;
  cin >> C;
  int n, m;
  for(int i=0; i<C; i++) {
    cin >> n >> m;
    int table[n][m];
    for(int j=0; j<n; j++)
      for(int k=0; k<m; k++)
        cin >> table[j][k];
    cout << "Case #" << i+1 << ": ";
    
    int ret = 1;
    int rN[n], rM[m];
    for(int i=0; i<n; i++) rN[i]=0;
    for(int i=0; i<m; i++) rM[i]=0;
    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++) {
        if(table[i][j]>rN[i]) rN[i]=table[i][j];
        if(table[i][j]>rM[j]) rM[j]=table[i][j];
      }
    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++)
        if(table[i][j]<rN[i] && table[i][j]<rM[j]) ret = 0;
    
    if(ret) cout << "YES" << endl; else cout << "NO" << endl;
  }
  
  return 0;
}

