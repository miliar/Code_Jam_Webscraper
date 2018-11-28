#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;


vector<int> vec;

bool palindrome(int i){
  int tmp1 = i, tmp2 = 0,cre = 1;
  while(tmp1){
    tmp2 *= 10;
    tmp2 += tmp1%10;
    tmp1 /= 10;
  }
  if(tmp2 == i) return true;
  return false;
}

int numero(int A,int num = 0){
  int cont = 0;
  for (int i = 0; vec[i] <= (A - num) and i < vec.size(); ++i){
    cont++;
  }
  return cont;
}

int main(){
  for (int i = 1, j = i*i; j < 10001; i++, j = i*i){
    if(palindrome(i) and palindrome(j)) vec.push_back(j);
  }
  int A,B,test,caso = 0,ca,cb;
  scanf("%i",&test);
  while(test--){
    scanf("%i %i", &A,&B);
    printf("Case #%i: %i\n",++caso ,(numero(B) - numero(A,1)));
  }
  return 0;
}