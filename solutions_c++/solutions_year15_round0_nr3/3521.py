#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#define i 2
#define j 3
#define k 4
using namespace std;
ifstream in("C-small.in");
ofstream out("out.out");
vector<char> sequenza;
vector<char> sottoSequenza;
//1=1 2=i 3=j 4=k
char prodotto(char a, char b){
  char risultato;
  char segno=(a>0 && b>0)||(a<0 && b<0)?1:-1;
  if (a<0)a*=-1;
  if (b<0)b*=-1;
  switch (a){
    case 1: risultato=b; break;
    case i: switch (b) {
              case 1: risultato= i;break;
              case i: risultato=-1;break;
              case j: risultato= k;break;
              case k: risultato=-j;break;
            }break;
    case j: switch (b) {
              case 1: risultato= j;break;
              case i: risultato=-k;break;
              case j: risultato=-1;break;
              case k: risultato= i;break;
            }break;
    case k: switch (b) {
              case 1: risultato= k;break;
              case i: risultato= j;break;
              case j: risultato=-i;break;
              case k: risultato=-1;break;
            }break;
    break;
  }
  return risultato*segno;
}
int main()
{
  int caso,ncasi;
  in>>ncasi;
  for (caso=1;caso<=ncasi;caso++){
    bool finito=false;
    int lSub,nRip;
    in>>lSub>>nRip;
    char stringa[lSub*nRip];
    in>>stringa;
    for (int z=0;z<lSub;z++){
      stringa[z]=stringa[z]=='1'?1:(stringa[z]=='i'?i:(stringa[z]=='j'?j:k));
    }
    for (int z=1;z<nRip*lSub;z++){
      stringa[z]=stringa[z%lSub];
    }
    long p=1;
    char risultato=stringa[0];
    while (risultato!=i && p<nRip*lSub){
      risultato=prodotto(risultato,stringa[p]);
      p++;
    }
    risultato=1;
    while (risultato!=j && p<nRip*lSub){
      risultato=prodotto(risultato,stringa[p]);
      p++;
    }
    risultato=1;
    while (risultato!=k && p<nRip*lSub){
      risultato=prodotto(risultato,stringa[p]);
      p++;
    }
    if (risultato==k) finito=true;
    risultato=1;
    while (p<nRip*lSub){
      risultato=prodotto(risultato,stringa[p]);
      p++;
    }
    if (finito && risultato==1){
      cout<<"Case #"<<caso<<": YES"<<endl;
      out<<"Case #"<<caso<<": YES"<<endl;
    } else{
      cout<<"Case #"<<caso<<": NO"<<endl;
      out<<"Case #"<<caso<<": NO"<<endl;
    }

  }
}
