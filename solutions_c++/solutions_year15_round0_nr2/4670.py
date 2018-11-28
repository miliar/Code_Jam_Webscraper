#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;


int main (){
  int B[1001];
  ifstream leer("B-small-attempt3.in",ios::in);
  ofstream copiar("b.out",ios::out);
  int c=1,t,ans,n,aux,menor;
  leer  >> t;
  vector<int> A;
  while (c<=t){
    menor=1000000;
    A.clear();
    for (int i=0;i<1001;i++){
      B[i]=0;
    }
    leer >> n;
    for (int i=0;i<n;i++){
      leer >> aux;
      B[aux]+=1;
    }
    for (int i=9;i>=1;i--){
      ans=0;
      for (int j=1000;j>0;j--){
        if (B[j]>0){
          if (j%i==0){
            ans+=B[j]*(j/i-1);
          } else {
            ans+=B[j]*(j/i);
          }
        }
      }
      ans+=i;
      if (ans<menor) menor=ans;
    }
    copiar << "Case #" << c << ": " <<  menor << endl;
    c++;
  }
  return 0;
}
