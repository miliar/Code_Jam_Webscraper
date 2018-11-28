#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "stdlib.h"
using namespace::std;

typedef pair<int,int> ii;
typedef pair<float,int> fi;
typedef vector<ii> vii;
typedef vector<int> vi;

vi divi;

bool primo(long long int nb){
  //std::cout << "entou primo" << std::endl;
  long long int i;
  int fg =1;
  for (i = 2 ; i < 10000; i++){
        if (nb % i == 0){
          fg=0;
          break;
        }
  }
  if (fg){
          return true;
        }
  else{
          divi.push_back(i);
          return false;
}
}
int main(){


int x;
int somador;
bool flag;
int n,j;
vi v;
cin >> x;
cin >> n >> j;
somador = n-1;
std::cout << "Case #1:" << std::endl;
v.push_back(1);
for (int i = 1; i < n-1; i++) {
  v.push_back(0);
}
v.push_back(1);
/*
for (int i = 0; i < n; i++) {
  cout << v[i];
}
std::cout << "" << std::endl;
*/
while(j>0){
divi.clear();
long long int ver[11] = {0,0,0,0,0,0,0,0,0,0,0};
/////CONVERSOR////
flag =true;
for (int k = 2; k < 11; k++) {
for (int i = 0; i < n; i++) {
  if(v[n-1-i]!=0){
  long long int h = pow(double(k),double(i));
  ver[k] += h;
}
  //std::cout << h << std::endl;
  //std::cout << ver[k] <<" "<< v[n-1-i] <<"*" << h << std::endl;
}
//std::cout << ver[k] << std::endl;
if(primo(ver[k])){
  //std::cout<< "primo" << ver[k] << " " << k << endl;
  flag = false;
  break;
}
//std::cout << ver[j] << std::endl;
}

/////RESPOSTAS/////

if(flag){
  for (int i = 0; i < n; i++) {
    cout << v[i];
  }
  std::cout << " ";
  for (int i = 0; i < divi.size(); i++) {
    std::cout << divi[i] << " ";
  }
std::cout << std::endl;
j--;
}
//////SOMADOR//////
v[n-2] += 1;
for (int i = n-2; i > 2; i--) {
  if(v[i] >= 2){
    v[i] =0;
    v[i-1] += 1;
  }
}
/*
std::cout << std::endl;
for (int i = 0; i < n; i++) {
  cout << v[i];
}
std::cout << std::endl;
*/

}

}
