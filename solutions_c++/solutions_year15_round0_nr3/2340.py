#include <cstdlib>
#include <stdint.h>
#include <iostream>

using namespace std;

int f(char c) {
  if(c == 'i') {
    return 2;
  } else if(c == 'j') {
    return 3;
  } else if(c == 'k') {
    return 4;
  } else {
    return 1;
  }
}

int q(int a, int b) {
  int s, p; // s - sign modifier, p - product of abs(a) and abs(b)
  
  if(a * b < 0) {
    s = -1;
  } else {
    s = 1;
  }
  
  a = abs(a);
  b = abs(b);
  
  if(a == 1) {
    p = b; // 1 is neutral
  } else if(b == 1) {
    p = a; // 1 is neutral
  } else if(a == b) {
    p = -1; // i*i=j*j=k*k=-1; 1*1=1 is already handled by the first if
  } else if(a == 2 and b == 3) {
    p = 4; // i*j=k
  } else if(a == 2 and b == 4) {
    p = -3; // i*k=-j
  } else if(a == 3 and b == 2) {
    p = -4; // j*i=-k
  } else if(a == 3 and b == 4) {
    p = 2; // j*k=i
  } else if(a == 4 and b == 2) {
    p = 3; // k*i=j
  } else if(a == 4 and b == 3) {
    p = -2; // k*j=-i
  }
  
  return p * s;
}

void test() {
  int L;
  int64_t X;
  char S[10001];
  cin >> L >> X;
  cin >> S;
  
  if(X > 12) {
    X = 12 + (X % 4);
  }
  
  int p = 1;
  for(int i = 0; i < L*X; i++) {
    p = q(p, f(S[i%L]));
  }
  
  if(p != -1) { // ijk = -1
    cout << "NO\n";
    return;
  }
  
  int a = 1;
  for(int i = 0; i < L*X; i++) {
    a = q(a, f(S[i%L]));
    if(a == 2) { // i
      int b = 1;
      for(int j = i+1; j < L*X; j++) {
        b = q(b, f(S[j%L]));
        if(b == 3) { // j
          cout << "YES\n";
          return;
        }
      }
    }
  }
  
  cout << "NO\n";
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; i++) {
    cout << "Case #" << i+1 << ": ";
    test();
  }
  return 0;
} 
