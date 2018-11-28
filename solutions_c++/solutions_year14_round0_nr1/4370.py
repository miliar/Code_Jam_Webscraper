#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <cstring>
#include <string>
#include <math.h>
#include <limits.h>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b

using namespace std;

int T,N,M;
int a[5][5],b[5][5];
ifstream fin("a.in");
ofstream fout("b.out");

int _search(int x,int y){
  int num=0,ans;
  int i,j;
  for(i=1;i<5;i++){
    for(j=1;j<5;j++){
      if(a[x][i]==b[y][j]){
        num++;
        ans=i;
        break;
      }
    }
  }
  if(num==1)
    return (-1)*ans;
  else
    return num;
}

int main(){
  int i,j,k,t;
  int x,y;
  fin>>T;
  
  
  for(t=1;t<=T;t++){
    fin>>x;
    for(i=1;i<5;i++){
      for(j=1;j<5;j++)
        fin>>a[i][j];
    }
    
    fin>>y;
    for(i=1;i<5;i++){
      for(j=1;j<5;j++)
        fin>>b[i][j];
    }
    
    fout<<"Case #"<<t<<": ";
    k=_search(x,y);
    if(k<0)
      fout<<a[x][-k];
    else if(k==0)
      fout<<"Volunteer cheated!";
    else
      fout<<"Bad magician!";
    fout<<endl;
  }
}