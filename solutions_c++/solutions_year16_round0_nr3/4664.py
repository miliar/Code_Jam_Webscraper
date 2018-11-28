#include <string.h>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
#define MOD 1000000007
typedef long long ll;

ll biton(string s, int n)
 {
  ll rit = 0;
  for(int i = 0; i < s.size(); i++) { if(s[i] == '1') rit += floor(pow(n,s.size()-i-1)); }
  return rit;
 }

ll divisione(ll n,int b)
 {
  for(ll i = b+1; i * i <= n; i++) { if(n % i == 0) return i;}
  return 1;
 }
string alg(ll n, ll m)
 {
  string s;

  for(ll z = m; z > 0; z >>= 1) s = s + ( ((n & z) == z) ? "1" : "0" );
  return s.substr(1);
 }

int main()
 {
  int t;
  int n;
  int j;
  cin >> t >> n >> j;
  ll M,ans;
  ll out[9];
  int w,c = 0;
  string s;
  
  cout << "Case #" << 1 << ": " << endl;
  M = pow(2.0,n);
  for(ll ii = M/2 + 1; ii < M-1; ii+=2)
   {
	s = alg(ii,M);
  w = 0;
    for(int i = 2; i <= 10; i++)
     {
	  ans = divisione(biton(s,i),i + c); if(ans == 1) break;
	  out[i-2] = ans;
	  if(i == 10) { w = 1; c++; }
	 }
	if(w == 1) { cout << s; for(int i = 0; i < 9; i++) cout << " " << out[i]; cout << endl; } // Output
	if(c == j) break;
   }
  return 0;
 }
