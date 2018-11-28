#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");

int main()
{
  int n,nt,t,tmp;
  int partiti[26];
  in>>t;
  string s;
  for (int nt=1;nt<=t;nt++){
    out<<"Case #"<<nt<<":";
    for (int i=0;i<26;i++) partiti[i]=0;
    int np,ns=0;
    in>>np;
    for (int i=0;i<np;i++){
      in>>partiti[i];
      ns+=partiti[i];
    }
    int max1,max2,pmax1,pmax2;
    char a,b;
    while (ns>0){
      if (partiti[0]>partiti[1]){
        max1=partiti[0]; pmax1=0;
        max2=partiti[1]; pmax2=1;
      } else {
        max1=partiti[1]; pmax1=1;
        max2=partiti[0]; pmax2=0;
      }
      for (int i=2;i<np;i++){
        if (partiti[i]>max1){
          max2=max1; pmax2=pmax1;
          max1=partiti[i]; pmax1=i;
        } else if (partiti[i]>max2){
          max2=partiti[i]; pmax2=i;
        }
      }
      if (max1-max2>1){
        //rimuovo i due senatori dello stesso partito
        partiti[pmax1]-=2;
        a='A'+pmax1;
        out<<" "<<a<<a;
        cout<<" "<<a<<a;
        ns-=2;
      } else {
        // ne rimuovo uno di un partito e uno dell'altro
        if (ns==3){
          //ne rimuovo solo 1
          partiti[pmax1]--;
          a=('A'+pmax1);
          out<<" "<<a;
          ns--;
        } else {
          partiti[pmax1]--;
          partiti[pmax2]--;
          a=('A'+pmax1);
          b=('A'+pmax2);
          out<<" "<<a<<b;
          ns-=2;
        }
      }
    }
    out<<endl;
    cout<<endl;
  }
  return 0;
}
