#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;

string torpil[1000];
int dizi[1000];

int main(){
  int i,j,n,m,sayac=0;
  ifstream oku ("input.txt");
  ofstream yaz ("output.txt");
  oku >> n;
  for(i=1;i<=n;i++){
    oku >> torpil[i];
  }
  for(i=1;i<=n;i++){
    for(j=0;j<=torpil[i].length()-1 ;j++){
      if(j==torpil[i].length()-1){
        if(torpil[i][j]=='-')
          dizi[i]++;
      }
      else if(torpil[i][j]!=torpil[i][j+1])
        dizi[i]++;
    }
  }
  for(i=1;i<=n;i++){
    yaz <<"Case #"<<i<<": "<<dizi[i]<<endl;
  }
}
