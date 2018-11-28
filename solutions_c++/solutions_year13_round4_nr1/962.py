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

int m[120];
int f[120];
int solve(int A, int N) {
  sort(m, m + N);
  if ( A == 1) {
    return N;
  }
  int i = 0;
  memset(f, 0, sizeof(f));
  int curA = A;
  while (i < N) {
    if (curA <= m[i]) {
      curA += curA - 1;
      ++f[i];
    } else {
      curA += m[i];
      ++i;
      f[i] = f[i-1];
    }
  }
  int res = N;
  for (i = 0; i< N; ++i) {
    if (res > f[i] + N-i-1) {
      res = f[i] + N-i-1;
    }
  }
  return res;
}

void Work() {
  int i,A, N;
  input>>A>>N;
  for ( i = 0; i< N; ++i) {
    input>>m[i];
  }
  output<<solve(A,N)<<endl;
  
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

