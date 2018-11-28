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

int T,N;
double A[1100],B[1100];
bool a[1100],b[1100];
ifstream fin("a.in");
ofstream fout("b.out");

int cmp(const void*arg1,const void*arg2){
  return *(double *)arg1>*(double *)arg2?1:-1;
}

class table{
  public:
    table(){
      int i;
      rest=N;
      for(i=0;i<N;i++){
        buffA[i]=A[i];
        buffB[i]=B[i];
      }
    }
    
    int check(){
      int i,flag=1;
      for(i=0;i<rest;i++){
        if(buffA[i]<buffB[i])
          flag=0;
      }
      if(flag)
        return 1;
      else{
        Delete();
        return 0;
      }
    }
    
    void Delete(){
      int i;
      for(i=0;i<rest-1;i++)
        buffA[i]=buffA[i+1];
      rest--;
    }
  
    double buffA[1100];
    double buffB[1100];
    int rest;
};

int main(){
  int i,j,k,t;
  int x,y;
  int ans1,ans2;
  fin>>T;
  
  for(t=1;t<=T;t++){
    fin>>N;
    for(i=0;i<N;i++)
      fin>>A[i];
    for(i=0;i<N;i++)
      fin>>B[i];
    qsort(A,N,sizeof(A[0]),cmp);
    qsort(B,N,sizeof(B[0]),cmp);
    
    for(i=0;i<N;i++){
      a[i]=false;
      b[i]=false;
    }
    
    ans2=0;
    for(i=0;i<N;i++){
      for(j=0;j<N;j++){
        if(A[i]<B[j] && b[j]==false){
          b[j]=true;
          ans2++;
          break;
        }
      }
    }
    ans2=N-ans2;
    
    ans1=0;
    class table que;
    for(i=0;i<N;i++){
      if(que.check())
        break;
    }
    ans1=que.rest;
    fout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<endl;
  }
}