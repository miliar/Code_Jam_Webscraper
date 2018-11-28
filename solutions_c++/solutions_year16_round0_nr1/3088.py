#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");
vector<bool> digits;

void checkDigits(int a){
  int b;
  while (a>0){
    b=a%10;
    digits.at(b)=true;
    a/=10;
  }
}

int main(){
  int t,nT,n;
  in>>nT;
  nT++;
  for (int i=0;i<10;i++) digits.push_back(false);
  for (t=1;t<nT;t++){
    int ni=0;//n*i
    for (int i=0;i<10;i++) digits.at(i)=false;
    out<<"Case #"<<t<<": ";
    in>>n;
    if (n==0){
      out<<"INSOMNIA"<<endl;
      continue;
    }
    while(true){
      ni+=n;
      checkDigits(ni);
      bool fine=true;
      for (int i=0;i<10;i++)
        if (!digits.at(i)){fine=false; break;}
      if (fine) {out<<ni<<endl;break;}
    }
  }
  return 0;
}
