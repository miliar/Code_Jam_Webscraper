#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("B-small.in");
ofstream out("out.out");
vector <int> panPiatto;
int nPers;
int nMinRimanenti(void){
  int m=panPiatto.at(0);
  for (int i=1;i<nPers;i++){
    if (panPiatto.at(i)>m) m=panPiatto.at(i);
  }
  return m;
}

int piattoMax(void){
  int m=panPiatto.at(0);
  int p=0;
  for (int i=1;i<nPers;i++){
    if (panPiatto.at(i)>m) {m=panPiatto.at(i);p=i;}
  }
  return p;
}

int nPiatti(int q){
  int n=0;
  for (int i=0;i<nPers;i++){
    if (panPiatto.at(i)==q) n++;
  }
  return n;
}

bool inline max3(void){
  for(int i=0;i<nPers;i++)if (panPiatto.at(i)>3 && panPiatto.at(i)%3!=0) return false; return true;
}

int main()
{
  int caso,ncasi;
  in>>ncasi;
  for (caso=1;caso<=ncasi;caso++){
    panPiatto.clear();
    in>>nPers;
    int nMin=0;
    {
      int tmp;
      for (int i=0;i<nPers;i++) {in>>tmp; panPiatto.push_back(tmp);}
    }
      bool convieneDividere=false;
    int minm=nMinRimanenti();
    while (true){
              //il tempo che guadagno per quel piatto>tempo che guadagnerei per dimezzare tutti i piatti
      if (nMinRimanenti()>3 && nMinRimanenti()/2>nPiatti(nMinRimanenti())) {
        if (nMinRimanenti()==9 && nPiatti(9)==1 && max3()){
          panPiatto.push_back(6);
          panPiatto.at(piattoMax())=3;
        }else{
          panPiatto.push_back(panPiatto.at(piattoMax())/2);
          panPiatto.at(piattoMax())-=panPiatto.at(piattoMax())/2;
        }
        nPers++;
        nMin++;
        if (nMin+nMinRimanenti()<minm)minm=nMin+nMinRimanenti();//così non rischio di perdere tempi migliori
      } else break;
    }
    nMin+=nMinRimanenti();
    if (nMin<minm)minm=nMin;//così non rischio di perdere tempi migliori
    if (minm!=nMin)cout<<"Case #"<<caso<<": "<<minm<<endl;
    out<<"Case #"<<caso<<": "<<minm<<endl;
  }
}
