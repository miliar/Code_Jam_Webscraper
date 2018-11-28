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

int T;
double C,F,X;
ifstream fin("a.in");
ofstream fout("b.out");



int main(){
  int i,j,k,t;
  int x,y;
  double v,m,times;
  fin>>T;

  for(t=1;t<=T;t++){
    fin>>C>>F>>X;
    v=2.0;
    times=0;
    for(m=0;m<X;v+=F){
      if(X/v<(C/v+X/(v+F))){
        times+=X/v;
        m=X;
      }
      else
        times+=C/v;
    }
    fout<<"Case #"<<t<<": "<<fixed;
    fout.precision(7);
    fout<<times<<endl;
  }
}