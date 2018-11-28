#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include "stdlib.h"
using namespace::std;

typedef pair<int,int> ii;
typedef pair<float,int> fi;
typedef vector<ii> vii;
typedef vector<int> vi;


int main (){
  int n,cont=0;
  int resp;
  int tam;
  string v;
  cin >> n;
  while (cont < n) {
    resp=0;
    v.clear();
    cin >> v;

    tam =v.size();
    //std::cout << v.size() << std::endl;

  for (int i = 0; i < tam-1; i++) {
      if(v[i] != v[i+1]){
        resp++;
      }
  }
  //std::cout << v[tam-1] << std::endl;
  if(v[tam-1] == '-')
      resp++;

  std::cout << "Case #"<<cont+1 <<": "<<resp << std::endl;
  cont++;
}
}
