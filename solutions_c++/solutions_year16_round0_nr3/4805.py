#include <iostream>

#include <math.h> 

using namespace std;

long primes[10000];

// thanks https://www.topcoder.com/community/data-science/data-science-tutorials/primality-testing-non-deterministic-algorithms/
long modulo(long a,long b,long c){
  long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
  while(b > 0){
    if(b%2 == 1){
      x=(x*y)%c;
    }
    y = (y*y)%c; // squaring the base
    b /= 2;
  }
  return x%c;
}

long long mulmod(long long a,long long b,long long c){
  long long x = 0,y=a%c;
  while(b > 0){
    if(b%2 == 1){
      x = (x+y)%c;
    }
    y = (y*2)%c;
    b /= 2;
  }
  return x%c;
}

bool Miller(long long p,int iteration){
  if(p<2){
    return false;
  }
  if(p!=2 && p%2==0){
    return false;
  }
  long long s=p-1;
  while(s%2==0){
    s/=2;
  }
  for(int i=0;i<iteration;i++){
    long long a=rand()%(p-1)+1,temp=s;
    long long mod=modulo(a,temp,p);
    while(temp!=p-1 && mod!=1 && mod!=p-1){
      mod=mulmod(mod,mod,p);
      temp *= 2;
    }
    if(mod!=p-1 && temp%2==0){
      return false;
    }
  }
  return true;
}

long checkIsNotPrime(long n) {
  for (long i = 2 ; i < 10000; i++) {
    if (n%primes[i]== 0) {
      return primes[i];
    }
  }
  return 0;
}

long tryNumber(long n) {

  long divs[9];
  for (long i = 2; i <= 10; i++) {
    long res = 0;
    long temp = n;
    long toAdd = 1;
    while (temp > 0) {
      if (temp & 1) {
        res += toAdd;
      }
      toAdd *= i;
      temp >>= 1;
    }

    if (Miller(res, 20)) {
      return 0;
    }

    long divisor = checkIsNotPrime(res);
    if (divisor) {
      divs[i-2] = divisor;
    } else {
      return 0;
    }
  }

  string out = "";
  while (n > 0) {
    if (n & 1) {
      out += "1";
    } else {
      out += "0"; 
    }
    
    n >>= 1;
  }


  for (long i = out.length(); --i >= 0;) {
    cout << out[i];
  }

  for (long i = 0; i < 9; i++) {
    cout << " ";
    cout << divs[i];
  }
  cout << endl;
  return 1; 
}

int main() {
  long t;


  // input is a list of the first 10000 primes found on the internet
  for (int i = 0; i < 10000; i++) {
    long temp;
    cin >> temp;
    primes[i] = temp;
  }

  t = 1;

  for (long i = 0; i < t; i++) {
    long n, j;
    n = 16;
    j = 50;

    cout << "Case #" << (i+1) << ":" << endl;

    long max = (long)pow(2, n-2);
    long hb = 1 << (n-1);

    long count = 0;

    for (long k = 0; k < max; k++) {
      long toTry = (k << 1) | hb | 1;

      count += tryNumber(toTry);
      if (count == j) {
        return 0;
      }
    }

  }
  return 0;
}
