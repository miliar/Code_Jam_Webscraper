#include<iostream>
#include<fstream>
#include <cmath>
using namespace std;
ifstream fin("in");
ofstream fout("out");
bool checkPal(int n){
  int nS[100]={0};
  int length=0;
  while (n>0){
    nS[length]=n%10;
    length++;
    n=n/10;
  }
  if (length<2) return true;
  for(int i=0; i<length; i++){
    if(nS[i]!=nS[length-i-1]){
      return false;
    }
  }
  return true;
}

int main(){
  int cases;
  fin >> cases;
  for (int i=1; i<=cases; i++){
    int A,B, count=0;
    fin>>A>>B;
    double rA,rB;
    rA=sqrt(A); if (floor(rA)<rA) {rA=floor(rA)+1;} 
    rB=sqrt(B); if (floor(rB)<rB) {rB=floor(rB);}
    for (int j=(int)rA; j<=rB; j++){
      if(checkPal(j) && checkPal(j*j)) //continue;
	  count++;
    }
    fout <<"Case #"<<i<<": "<<count<<endl;
  }
  return 0;
}
    
