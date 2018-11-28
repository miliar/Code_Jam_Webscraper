#include<iostream>
#include<fstream> 
#include<cstdio>
#include<stdlib.h>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("output.txt");

int i,j,k,n,p1,p2;
int a[4][4];
int b[4][4];

int result=0,pos=0;

int main(){
  fin>>n;
  for (k=1;k<=n;k++){
    fin>>p1;
    for (i=0;i<4;i++){
      for (j=0;j<4;j++){
        fin>>a[i][j];    
      }
    }
    fin>>p2;
    for (i=0;i<4;i++){
      for (j=0;j<4;j++){
        fin>>b[i][j];
      }
    }
    p1--;p2--;
    for (i=0;i<4;i++){
      for (j=0;j<4;j++){
        if (a[p1][i]==b[p2][j]){
          result++;
          pos=a[p1][i];
        }
      }
    }
    if (result==0) fout<<"Case #"<<k<<": Volunteer cheated!\n";
    else if (result==1) fout<<"Case #"<<k<<": "<<pos<<endl;
    else fout<<"Case #"<<k<<": Bad magician!\n";
    
    result=0;
    pos=0;
  }

  system("pause");
  return 0;
} 
