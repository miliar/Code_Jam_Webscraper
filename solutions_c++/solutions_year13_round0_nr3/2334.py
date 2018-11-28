#include <cstdlib>
#include <utility>
#include <cmath>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

typedef unsigned long long int ULL;

bool mirror(string ns){
  int k = ns.size() / 2;
  for (int j = 0; j<k; ++j){
    if( ns[ns.size()-1-j] != ns[j] ){
      return false;
    }
  }
  return true;
}

ULL solve(ULL a){
  stringstream ss;
  ULL cnt=0;
  ULL t = sqrt(sqrt(a));
  if( a >= 1 )
    cnt++;
  if( a>= 4 )
    cnt++;
  if( a>= 9 )
    cnt++;
  for (ULL i=1; i<=t; ++i){
    ss.clear();
    string is;
    ss<<i; ss>>is;

    for (int j = 0; j<11; ++j){
      ss.clear();
      string ri(is.rbegin(),is.rend());
      if(j==0){
	ss<< is << ri;
      }else
	ss<< is << j-1 << ri;

      ULL n;
      ss>>n;

      n=n*n;
      string ns;

      ss.clear();
      ss << n; ss >> ns;
      if(n<=a && mirror(ns) ){
	cnt++;
      }

    }
  }
  return cnt;
}

int main(){
  int t;
  cin>>t;
  for (int i = 1; i <= t; ++i){
    ULL a,b;
    cin>>a>>b;
    cout << "Case #" << i << ": "<< (solve(b) - solve(a-1) ) << endl;
  }
  return 0;
}
