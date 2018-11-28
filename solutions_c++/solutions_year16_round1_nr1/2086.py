#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include "math.h"
#include "stdio.h"
#include "stdlib.h"

using namespace::std;

typedef pair<int,int> ii;
typedef pair<float,int> fi;
typedef vector<ii> vii;
typedef vector<int> vi;

int main (){
int i,n,cont=1;
string s;
string aux;
cin >> n;
while (n--) {
s.clear();
cin >> s;
aux.clear();

aux.push_back(s[0]);
for (size_t i = 1; i < s.size(); i++) {
  //std::cout << int(s[i]) <<" "<< int(aux[i-1]) << i<< std::endl;
      if(s[i] >= aux[0]){
      //  std::cout << "entro" << std::endl;
        aux = s[i] + aux;
      }
      else{
        aux.push_back(s[i]);
      }
}
std::cout << "Case #"<< cont <<": ";
for (size_t i = 0; i < aux.size(); i++) {

  std::cout << aux[i];
}
std::cout << std::endl;
cont++;
}

return 0;
}
