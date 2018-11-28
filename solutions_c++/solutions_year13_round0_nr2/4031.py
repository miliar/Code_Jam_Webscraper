#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int ismax(){
}

int main(){

  ifstream input("input.in",ios::in);
  ofstream output("output.out", ios::out);
  
  int t;

  int N;//lines
  int M;//cols
  
  int tab[100][100];
  int linemax[100];
  int colmax[100];
  
  int allright[100][100];
  
  input>>t;
  for(unsigned T=0; T<t; ++T){
    
    input>>N;
    input>>M;
    
    for(int i=0;i<N;++i){
      for(int j=0;j<M;++j){
	allright[i][j]=0;
      }
    }
    
    for(int i=0;i<N;++i){
      for(int j=0;j<M;++j){
	input>>tab[i][j];
      }
    }
    
   
    for(int i=0;i<N;++i){
      int max=0;
      for(int j=0;j<M;++j){
	if(tab[i][j]>max)max=tab[i][j];
      }
      linemax[i]=max;
    }  
    
    for(int i=0;i<M;++i){
      int max=0;
      for(int j=0;j<N;++j){
	if(tab[j][i]>max)max=tab[j][i];
      }
      colmax[i]=max;
    }  
    
    for(int i=0;i<N;++i){
      for(int j=0;j<M;++j){
	if(tab[i][j]==linemax[i])allright[i][j]=1;
      }
    }
    
    
    for(int i=0;i<N;++i){
      for(int j=0;j<M;++j){
	if(tab[i][j]==colmax[j])allright[i][j]=1;
      }
    }
    
    int resp=1;
    for(int i=0;i<N;++i){
      for(int j=0;j<M;++j){
	if(allright[i][j]==0)resp=0;
      }
    }
    
    
    if(resp){output<<"Case #"<<T+1<<": YES\n";}
    else{output<<"Case #"<<T+1<<": NO\n";}
  } 
  
  return 1;

}