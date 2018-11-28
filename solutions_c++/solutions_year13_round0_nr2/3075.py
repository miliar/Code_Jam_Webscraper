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

int a[102][102];
int b_row[102];
int b_col[102];
int n,m;
bool is_possible() {
  for (int i = 0; i< n; ++i) {
    b_row[i] = 1;
  }
  for (int j = 0; j< m; ++j) {
    b_col[j] = 1;
  }

  for (int i = 0; i< n; ++i) {
    for (int j = 0; j< m; ++j) {
      b_row[i] = max(a[i][j], b_row[i]);
      b_col[j] = max(a[i][j], b_col[j]);
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j< m; ++j) {
      if (min(b_row[i], b_col[j]) != a[i][j]) {
        return false;
      }
    }
  }
  return true; 
}
void Work() {
  
  //output<<"Result Here"<<endl;
  input>>n>>m;
  for (int i = 0; i< n; ++i) {
    for (int j = 0; j< m ; ++j) {
      input>>a[i][j];
    }
  }
  if (is_possible() ) {
    output<<"YES"<<endl;
  } else {
    output<<"NO"<<endl;
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
