#include <iostream>
#include <cstring>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
template<class T> void atov(int n,T A[],vector<T> &vi){
  vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);
}//NOTES:atov(
template<class T> void stov(string s,vector<T> &vi){
  vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));
}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template <typename T> inline T Gcd( T a, T b) {
  // a, b should be unnegative
  if ( b == 0) return a;
  return Gcd( b, a % b);
}


ifstream input;
ofstream output;

void init() {

}


void Work() {
  //output<<"Result Here"<<endl;
  int a[4][4];
  int v[18];
  int r;
  for (int i = 1; i <= 16; ++i) v[i] = 0;
  input>>r;
  for (int i= 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      input>>a[i][j];
    }
  }

  for (int i = 0; i < 4; ++i) {
    ++v[ a[r - 1][i] ]; 
  }
  input>>r;
  for (int i = 0; i< 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      input>>a[i][j];
    }
  }
  int match = 0;
  int p = 0;
  for (int i = 0; i < 4; ++i) {
    if (v[ a[r - 1][i] ] > 0) {
      match = match + 1;
      p = a[r - 1][i];
    }
  }
  if (match == 0) {
    output<<"Volunteer cheated!"<<endl;
  } else if (match == 1) {
    output<<p<<endl;
  } else  {
    output<<"Bad magician!"<<endl;
  }  
}
int main() {
  
int t = 0;
  string inputfile("input.in");
  string outputfile("output.out");
  input.open(inputfile.c_str());
  output.open(outputfile.c_str());
  input>>t;
  int tcase = 0;
  init();
  while( t--) {
    ++tcase;
    output<<"Case #"<<tcase<<": "; 
    Work();
  }
}
