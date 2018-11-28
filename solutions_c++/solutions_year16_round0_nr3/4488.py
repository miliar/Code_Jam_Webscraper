#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

long long int convert(string str, int base){
  long long int resp = 1;

  int i = str.size()-2;
  long long int j = 1;

  while(i >= 0){
    j *= base;
    if(str[i] == '1'){
      resp += j;
    }
    i--;
  }

  return resp;
}


bool isPrime(long long int n){
  if(n<5 || n%2==0 || n%3==0){
    return (n==2||n==3);
  }

  int maxP = sqrt(n)+2;

  for(int p=5; p<maxP; p+=6)
    if(n%p==0||n%(p+2)==0)
      return false;

  return true;
}

bool testBase(string str){
  for(int i = 2; i <= 10; i++){
    long long int x = convert(str,i);
    if(isPrime(x)){
      return false;
    }
  }
  return true;
}

string toBinary(int n, int digits){
  string str = "";

  while(n > 0){
    int x = n%2;
    n /= 2;

    if(x == 0){
      str = '0' + str;
    }else{
      str = '1' + str;
    }
  }

  while(str.size() < digits){
    str = '0' + str;
  }

  return str;
}

void printDivisors(string str){
  for(int i = 2; i <= 10; i++){
    long long int x = convert(str, i);
    int k = 3;
    while(x%k != 0){
      k++;
    }
    cout << " " << k;
  }
  cout << endl;
}

int main(){
  int T, N, J;

  cin >> T;

  for(int k = 1; k <= T; k++){
      printf("Case #%i:\n", k);
      cin >> N >> J;
      string str = "1" + toBinary(0, N-2) + "1";
      int i = 0, j = 0;
      while(str.size() == N && j < J){
          i++;
          if(testBase(str)){
            cout << str;
            printDivisors(str);
            j++;
          }

          str = "1" + toBinary(i,N-2) + "1";
      }
  }
  return 0;
}
