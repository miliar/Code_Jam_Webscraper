#include <iostream>
#include <cstring>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iomanip>
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
  double c, f, x;
  input>>c>>f>>x;
  double cur_inc = 2;
  double best = x / 2;
  double cur_time = 0;
  while(true) {
    double next_time = c / cur_inc;
    double finish_time = x / cur_inc;
    if ((cur_time + finish_time) < best) {
      best = cur_time + finish_time; 
    }
    cur_time = cur_time + next_time;
    cur_inc = cur_inc + f;
    if (cur_time >= best) {
      break;
    }
  }
  output<<std::setprecision(9)<<std::setiosflags(std::ios_base::fixed)<<best<<endl;
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
