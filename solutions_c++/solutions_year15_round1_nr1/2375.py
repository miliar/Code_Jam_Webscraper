#include <iostream>
#include <fstream>

using namespace std;

int main(){
  ifstream leer ("A-large.in",ios::in);
  ofstream copiar ("a.out",ios::out);
  int i=1,T,aux,menor,n,m;
  long long y,z;
  leer >> T;
  while (i<=T){
    menor=0,y=0,z=0;
    leer >> n;
    int A[n];
    leer >> A[0];
    for (int i=1;i<n;i++){
      leer >> A[i];
      aux=A[i-1]-A[i];
      if (aux>0) y+=aux;
      if(aux>menor) menor=aux;
    }
    for (int i=0;i<n-1;i++){
      if(A[i]<menor) z+=A[i];
      else z+=menor;
    }
    copiar << "CASE #" << i << ": " << y << " " << z << endl;
    i++;
  }
  return 0;
}
