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
long long create_odd_pal(long long i) {
  long long s =0;
  long long a = 10;
  long long ii = i;
  while (i > 10) {
    s = s * 10 + i % 10;
    a = a * 10;
    i /= 10;
  }
  return s * a + ii;
}

long long create_even_pal(long long i) {
  long long s= 0;
  long long a= 1;
  long long ii = i;
  while( i > 0) {
    s = s * 10 + i % 10;
    a = a * 10;
    i /= 10;
  }
  return a * s + ii;
}
vector <long long> pal;
vector <long long> s_pal;
bool is_pal(long long i) {
  int a[30];
  int n = 0;
  while (i ) {
    a[n] = i % 10;
    i/= 10;
    ++n;
  }
  for (int k = 0; k< n/2; ++k) {
    if ( a[k] != a[n-1-k] ) return false;
  }
  return true;
}
void init() {
  pal.clear();
  pal.reserve(100000);
  s_pal.clear();
  
  
  for (int i = 1; i<= 9999; ++i) {
    if ( i % 10 == 0) {
      continue;
    }
    
    pal.push_back( create_odd_pal(i) );
    
    pal.push_back( create_even_pal(i));
    
  }
  sort(pal.begin(), pal.end());
  for (int i = 0; i< pal.size(); ++i) {
    if (is_pal( pal[i] * pal[i])) {
      s_pal.push_back(pal[i] * pal[i]);
    }
  }
  
}
long long find_idx(long long A) {
  long long l = 0;
  long long h = s_pal.size()-1;
  long long res = -1;
  while( l <= h) {
    long long mid = (l + h) >> 1;
    if ( s_pal[mid] <= A) {
      res = mid;
      l = mid + 1;
    } else {
      h = mid -1;
    }
  }
  return res;
}


void Work() {
  
  //output<<"Result Here"<<endl;
  long long A, B;
 
  input>>A>>B;
 
  if (A > B) {
    output<<0<<endl;
    return;
  }
 
  long long res1 = find_idx( A - 1);
  long long res2 = find_idx( B);
  output<<res2 - res1<<endl;
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
