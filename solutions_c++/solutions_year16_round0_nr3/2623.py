#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
ifstream in("C-small.in");
ofstream out("out.out");

vector<int> next(vector<int> a){
  int i=1,base=2;
  while(true){
    if (a.at(a.size()-i)<base-1){
      a.at(a.size()-i)++;
      return a;
    } else {
      a.at(a.size()-i)=0;
      i++;
      if (i>a.size()){
        a.insert(a.begin(),0);
        return a;
      }
    }
  }
  return a;
};

long long pow2(int b, int e){
  long long n=1;
  for (int i=0;i<e;i++)n*=b;
  return n;
}

long long decodificaNum(vector<int> v,int b){
  long long n=0;
  for (int i=0;i<v.size();i++)
    n+=v.at(i)*pow2(b,v.size()-i-1);
  return n;
}

int main(){
  int t,nT,n,j;
  in>>nT;
  nT++;
  vector<int> jamCoin;
  for (t=1;t<nT;t++){
    out<<"Case #"<<t<<": "<<endl;
    in>>n>>j;
    for (int i=0;i<n;i++) jamCoin.push_back(0);
    jamCoin.at(0)=jamCoin.at(n-1)=1;
    vector <int> divisori;
    while (j>0){
      divisori.clear();
      for (int b=2;b<=10;b++){//provare con l'ordine delle basi invertito(da 10 a 2)
        long long num=decodificaNum(jamCoin,b);
        if (num%2==0){
          divisori.push_back(2);
          continue;
        }
        long long limit=sqrt(num);
        bool isPrimo=true;
        int z;
        for (z=3;z<=limit+1;z+=2)
          if (num%z==0) {isPrimo=false;break;}
        if (isPrimo) break;
        divisori.push_back(z);
      }
      if (divisori.size()==9){
        //il jamCoin è valido
        j--;
        for (int a=0;a<jamCoin.size();a++)
          out<<jamCoin.at(a);
        for (int a=0;a<divisori.size();a++)
          out<<" "<<divisori.at(a);
        out<<endl;
//        for (int a=0;a<jamCoin.size();a++)
//          cout<<jamCoin.at(a);
//        for (int a=0;a<divisori.size();a++)
//          cout<<" "<<divisori.at(a);
//        cout<<endl;
      }
      jamCoin=next(jamCoin);
      jamCoin=next(jamCoin);//vado avanti due volte così l'ultima cifra è sempre 1
    }
  }
  return 0;
}
