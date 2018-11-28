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
int calc_fair_war(const vector<double>&v1, const vector<double>& v2) {
  int p1 = 0;
  int lost = 0;
  for (int i = 0; i<v1.size(); ++i) {
    while (p1 < v2.size() && v2[p1] < v1[i]) ++p1;
    if (p1 == v2.size()) {
      break;
    }
    else {
      ++lost;
      ++p1;
    }
  }
  return v1.size() - lost;
}
void pv(vector<double>s) {
  output<<"========="<<endl;
  for (int i = 0; i< s.size(); ++i) {
    output<<s[i]<<" ";
  }
  output<<endl;;
}
int calc_deceitful_war(const vector<double>&v1, const vector<double>& v2) {
  int s1 = 0, e1 = v1.size() - 1, e2 = v2.size() - 1;
  int lost = 0;
  
  while( s1 <= e1 ) {
    if (v1[e1] > v2[e2]) {
      --e1;
      --e2;
    } else if (v1[s1] > v2[e2]) {
      // Game is over
      break;
    } else {
      // lost one point
      ++s1;
      --e2;
      ++lost;
    }
  }
  return v1.size() - lost;
}


void Work() {
  int n;
  input>>n;
  vector<double> Naomi(n,0);
  vector<double> Ken(n, 0);
  for (int i = 0; i< n; ++i) {
    input>>Naomi[i];
  }
  for (int i = 0 ; i < n; ++i) {
    input>>Ken[i];
  }
  sort(Naomi.begin(), Naomi.end());
  sort(Ken.begin(), Ken.end());
  //  pv(Naomi);pv(Ken);
      
  int y = calc_deceitful_war(Naomi, Ken);
  int z = calc_fair_war(Naomi,Ken);
  output<<y<<" "<<z<<endl;
  //output<<"Result Here"<<endl;
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
