#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
using namespace std;
ifstream in("B-small.in");
ofstream out("out.out");
string pancakes;
int main()
{
  int t,nT,n;
  in>>nT;
  nT++;
  for (t=1;t<nT;t++){
    out<<"Case #"<<t<<": ";
    in>>pancakes;
    int nMoves=0;
    bool fine;
    while (true){
      fine=true;
      int i;
        /*la logica di base dell'algoritmo è:
        -scambiare i primi n + in -
        -girare tutto lo stack (tranne i + che sono in fondo)
        */
      for (i=0;i<pancakes.size();i++)
        if (pancakes.at(i)!='+'){fine=false; break;}
      if (fine){
        out<<nMoves<<endl;
        break;
      }
      if (i>0){//scambio i primi i + in -
        nMoves++;
        for(int j=0;j<i;j++){
          pancakes.at(j)='-';
        }
      }
      //rimuovo i + che stanno alla fine della pila
      for (i=pancakes.size()-1;i>=0;i--)
        if (pancakes.at(i)=='+') pancakes.erase(pancakes.size()-1,1);
        else break;
      //ora faccio lo swap dell'intera pila;
      nMoves++;
      string newPan;
      for (int j=pancakes.size()-1;j>=0;j--)
        if (pancakes.at(j)=='+') newPan.push_back('-');
        else newPan.push_back('+');
      for (int j=pancakes.size()-1;j>=0;j--)
        pancakes.at(j)=newPan.at(j);
    }
  }
  return 0;
}
