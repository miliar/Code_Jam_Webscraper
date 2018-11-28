#include <iostream>
#include <fstream>

using namespace std;

int main (){
  ifstream leer ("A-large.in",ios::in);
  ofstream copiar ("a.out",ios::out);
  int t,i=1,aux1=int('0');
  string st;
  leer >> t;
  while (i<=t){
    int m,p=0,ans=0,aux;
    leer >> m;
    leer >> st;
    for (int j=0;j<=m;j++){
      aux=int(st[j])-aux1;
      if (aux!=0){
        if (j>=p){
          ans+=j-p;
          p=j;
        }
      }
      p+=aux;
    }
    copiar << "Case #" << i << ": " << ans << endl;
    i++;
  }
  return 0;
}
