#include <iostream>
#include <cmath>

using namespace std;

long long base(long long a, long long b){
  long long ct = 0;
  long long count = 0;
  while(a != 0){
    long long lastdig = a%10; a/=10;
    ct += lastdig*pow(b,count);
    count ++;
  }
  return ct;
}

long long ctb(long long x){
  long long ct = 0;
  long long out = 0;
  while(x != 0){
    out += (x%2)*pow(10,ct);
    x/=2; ct++;
  }
  return out;
}

long long pcheck(long long x){
  for(long long i = 2; i < (int)sqrt(x); i++){
    if(x%i == 0){return i;}
  }
  return -1;
}

int main(){
  int tct = 0;
  cout << "Case #1: \n";
  for(long long i = 32769; i < (1 << 16); i += 2){
    if(tct == 50){return 0;}
    bool works = true;
    for(long long j = 2; j <= 10; j++){
      if(pcheck(base(ctb(i),j)) == -1){works = false; j = 11;}
    }
    if(works){
      tct ++;
      cout << ctb(i);
      for(long long j = 2; j <= 10; j++){
	cout << " " << pcheck(base(ctb(i),j));
      }
      cout << endl;
    }
  }
  return 0;
}
