#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
using namespace std;
ifstream in("B-small.in");
ofstream out("out.out");
string word,inS;
struct lista{
  vector<short> l;
};
vector<lista> biglietti;

int conta1(vector<int> a){
  int b=0;
//  for (int i=0;i<a.size();i++) cout<<a.at(i);
//  cout<<endl;
  for (int i=0;i<a.size();i++)
    if (a.at(i)==1) b++;
  return b;
  }

vector<int> next(vector<int> a,int n){
  int i=1,base=2;
  while(true){
    if (a.at(a.size()-i)<base-1){
      a.at(a.size()-i)++;
      if (conta1(a)==n) break;
      else {i=1;continue;}
    } else {
      a.at(a.size()-i)=0;
      i++;
      if (i>a.size()){
        a.insert(a.begin(),0);
        if (conta1(a)==n) break;
        else {i=1;continue;}
      }
    }
  }
  return a;
};

int main()
{
  int t,nT,n,tmp,altezze[2501];
  lista tmpL;
  in>>nT;
  nT++;
  for (t=1;t<nT;t++){
    out<<"Case #"<<t<<":";
    in>>n;
    for (int i=1;i<=2500;i++)altezze[i]=0;
    for (int i=0;i<(2*n-1)*n;i++){
      in>>tmp;
      altezze[tmp]++;
    }
    int j=0;
    for (int i=1;i<=2500&&j<n;i++){
      if (altezze[i]%2==1) {out<<" "<<i;j++;}
    }
    out<<endl;
  //ogni numero deve comparire un numero pari di volte
//    biglietti.clear();
//    for (int i=0;i<2*n-1;i++){
//      tmpL.l.clear();
//      for (int j=0;j<n;j++){
//        in>>tmp;
//        tmpL.l.push_back(tmp);
//      }
//      biglietti.push_back(tmpL);
//    }
//    //END OF INPUT
//    //ordino la lista
//    for (int i=0;i<biglietti.size();i++){
//      for (int j=0;j<biglietti.size()-i-1;j++){
//        if (biglietti.at(j).l.at(0)>biglietti.at(j+1).l.at(0)){
//          tmpL=biglietti.at(j);
//          biglietti.at(j)=biglietti.at(j+1);
//          biglietti.at(j+1)=tmpL;
//        }
//      }
//    }
//
//    vector <lista> schieramento;
//    vector <int>usati;
//    for (int i=0;i<biglietti.size();i++)usati.push_back(0);
//    bool trovata=false;
//    //creo la tabella per righe, dopodichè controllo che manchi una sola colonna
//    while (!trovata){
//      usati=next(usati,n);
//      int j=0;
//      schieramento.clear();
//      for (int i=0;i<n;j++){
//        if (usati.at(j)==1){
//          i++;
//          schieramento.push_back(biglietti.at(j));
//        }
//      }
////      for (int i=0;i<n;i++){
////        for (int j=0;j<n;j++){
////          cout<<schieramento.at(i).l.at(j)<<" ";
////        }
////        cout<<endl;
////      }
//      //controllo che la tabella creata sia corretta
//      bool corretta=true;
//      for (int i=0;i<n-1;i++){
//        for (int j=0;j<n;j++){
//          if (schieramento.at(i).l.at(j)>=schieramento.at(i+1).l.at(j)){
//            corretta=false;
//            break;
//          }
//        }
//        if (!corretta) break;
//      }
//      if (!corretta) continue;
//      //ora sono sicuro che sia corretta. Controllo che manchi una sola colonna
//      lista colonna;
//      int mancanti=0;
//      for (int i=0;i<n;i++){
//        colonna.l.clear();
//        for (int j=0;j<n;j++){
//          colonna.l.push_back(schieramento.at(j).l.at(i));
//        }
////        for (int f=0;f<n;f++) cout<<colonna.l.at(f)<<" ";
////        cout<<endl;
//        bool uguale;
//        for (int z=0;z<biglietti.size();z++){
//          if (usati.at(z)==1)continue;
//          uguale=true;
//          for (int a=0;a<n;a++){
//            if (biglietti.at(z).l.at(a)!=colonna.l.at(a)) {uguale=false; break;}
//          }
//          if (uguale){
//            break;
//          }
//        }
//        if (!uguale) mancanti++;
//        if (mancanti==2) break;
//      }
//      if (mancanti==1){
//        for (int a=0;a<n;a++) out<<" "<<colonna.l.at(a);
//        out<<endl;
//        trovata=true;
//      }
//    }
  }
  return 0;
}
