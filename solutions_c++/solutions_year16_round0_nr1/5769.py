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


/*
void verifica(){
for (int i = 0; i < tam; i++) {
    resp[vetor[i]] = 'x';
    //std::cout << vetor[i] << " "<< resp[vetor[i]] <<std::endl;
}
}*/
/*
bool conclui(int tam) {
  for (int i = 0; i < 10; i++) {
    if(resp[i] != 'x'){
      return false;
    }
  }
  return true;
}*/

int main (){
  int n;
  char vetor[1000000];
  char resp[10] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
  int tam;
  int cont=1;
  int k;
  int m;
  int num;
  int flag;
  int pos;
  string s;
  cin >> n;


  while (cont < n) {
   cin >> k;
   if(k!=0){
   m=1;
   char resp[10] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
   //string s = string(itoa(k));
   while (true){

   num = m*k;
   //cout << num << endl;
   string s = to_string(num);
   tam = s.size();
   sprintf(vetor,"%d",num);
   /*
   for (int i = 0; i < tam; i++) {
             cout << vetor[i]<<" ";
           }
           std::cout << "" << std::endl;
*/
   for (int i = 0; i < tam; i++) {

       pos = (vetor[i]-48);
       //std::cout << "pos: "<<pos << std::endl;
       resp[pos] = 'x';
       //std::cout <<i <<" "<< vetor[i] << " "<< resp[vetor[i]] <<std::endl;
   }
   //resp [1] = 'x';
/*
  for (int i = 0; i < 10; i++) {
            cout << resp[i]<<" ";
          }
          std::cout << "" << std::endl;
*/
 for ( flag = 0; flag < 10; flag++) {
            if(resp[flag] != 'x'){
              break;
            }
  }
  if(flag ==10)
  break;

m++;
  }
  cont++;
  cout << "CASE #"<< cont <<": " <<num<<endl;
}
else
  cout << "CASE #"<< cont <<": " <<"INSOMNIA"<<endl;
}

}
