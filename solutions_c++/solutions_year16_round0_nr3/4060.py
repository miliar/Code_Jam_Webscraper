#include <string.h>
#include <stdio.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

string bin(long long n, long long M)
 {
  string b;

  for(long long z = M; z > 0; z >>= 1) b = b + ( ((n & z) == z) ? "1" : "0" );
  return b.substr(1);
 }

long long bin2n(string b, int n)
 {
  long long v = 0;
  for(int i = 0; i < b.size(); i++) { if(b[i] == '1') v += floor(pow(n,b.size()-i-1)); }
  return v;
 }

long long div1(long long n,int b)
 {
  // Return a divider of n
  for(long long i = b+1; i <= sqrt(n); i++) { if(n % i == 0) return i; /*if(i > 1000000) return 1;*/ }
  return 1;
 }

int main()
 {
  int t,n,j;
  cin >> t >> n >> j;
  long long M,tt;
  long long out[9];
  int f,c = 0;
  string s;
  
  cout << "Case #" << 1 << ": " << endl;
  M = pow(2.0,n);
  for(long long b = M/2 + 1; b < M-1; b+=2)
   {
	s = bin(b,M); f = 0;
    for(int i = 2; i <= 10; i++)
     {
	  tt = div1(bin2n(s,i),i + c); if(tt == 1) break;
	  out[i-2] = tt;
	  if(i == 10) { f = 1; c++; }
	 }
	if(f == 1) { cout << s; for(int i = 0; i < 9; i++) cout << " " << out[i]; cout << endl; } // Output
	if(c == j) break;
   }
  return 0;
 }
