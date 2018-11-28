#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define forn(n) for(int i=0;i<n;i++)
typedef long long LL;
int jamcoin[33];
LL dividor [9];
using namespace std;
void reset_dividor(){
  int i ;
  for (i=0;i<9;i++)
    dividor[i] = 1;
  return ;
}

void init(int lengthN){
  int i;
  for (i=1;i<lengthN;i++)
    jamcoin[i] = 0;
  jamcoin[0] = 1;
  jamcoin[lengthN-1] = 1;
  reset_dividor();
  return;
}

void print_dividor(){
  int i;
  for (i=0;i<8;i++)
    cout << dividor[i] << " ";
  cout << dividor[8] << endl;
  return;
}

void print_jamcoin(int lengthN){
  int i;
  for (i=lengthN-1;i>=0;i--)
    cout  << jamcoin[i];
  cout << " ";
  return;
}

bool check_sigle_prime(LL number, int base){
  if(number < 2) return false;
  if(number == 2) return true;
  if(number % 2 == 0) {
    dividor[base-2] = 2;
    return false;
  }
  for(LL i=3; (i*i)<=number; i+=2){
    if(number % i == 0 ) {
      dividor[base-2] = i;
      return false;
    }
  }
  return true;
}

bool check_all_prime(int size){
  int base, index;
  LL sum=0;
  LL power;
  bool isPrime = false;
  for (base=2;base<=10 && !isPrime;base++){
    power = 1;
    sum = 0;
    for(index=0; index<size; index++){
      sum += jamcoin[index] * power;
      power *= base;
    }
    isPrime = check_sigle_prime(sum, base);
  }
  return !isPrime;
}

void jamcoin_increase(int lengthN){
  jamcoin[1] += 1;
  int i ;
  for(i=1;i<lengthN;i++){
    if (jamcoin[i] > 1 ){
      jamcoin[i+1] += 1;
      jamcoin[i]   = 0;
    }
  }
  return;
}
void find_valid_jamcoin(int lengthN, int exampleJ){
  bool success = false;
  while (exampleJ >0){
    jamcoin_increase(lengthN);
    reset_dividor();
    success = check_all_prime(lengthN);
    if (success) {
      print_jamcoin(lengthN);
      print_dividor();
      exampleJ--;
    }
  }
  return; 
}
int solve(int case_num){
  int lengthN, exampleJ;
  scanf("%d", &lengthN);
  scanf("%d", &exampleJ);
  printf("Case #%d:\n", case_num);
  int i ;
  init(lengthN);
  find_valid_jamcoin(lengthN, exampleJ);
  return 0;
}

int main(){
  int T, i;
  scanf("%d", &T);
  for (i = 1; i<=T; ++i )
    solve(i);
  return 0;
}
// int main(){
//   int size = 6;
//   init(size);
//   jamcoin_increase(size);
//   print_jamcoin(size);
//   jamcoin_increase(size);
//   print_jamcoin(size);
//   jamcoin_increase(size);
//   print_jamcoin(size);
//   return 0;
// }
