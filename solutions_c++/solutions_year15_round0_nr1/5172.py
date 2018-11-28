#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");
int caso,ncasi;
int main()
{
  in>>ncasi;
  for (caso=1;caso<=ncasi;caso++){
    int livMax,nPersAlzate,nAmici=0;
    char livelli[1000];
    in>>livMax;
    short nPersLiv[livMax+1];
    in>>livelli;
    for (int i=0;i<=livMax;i++) nPersLiv[i]=livelli[i]-'0';
    //fine input, inizio algoritmo
    nPersAlzate=nPersLiv[0];
    for (int i=1;i<=livMax;i++){
      if (nPersAlzate>=i) nPersAlzate+=nPersLiv[i];
      else {
        nAmici+=i-nPersAlzate;
        nPersAlzate+=nPersLiv[i]+(i-nPersAlzate);
      }
    }
    cout<<"Case #"<<caso<<": "<<nAmici<<endl;
    out<<"Case #"<<caso<<": "<<nAmici<<endl;
  }
}
