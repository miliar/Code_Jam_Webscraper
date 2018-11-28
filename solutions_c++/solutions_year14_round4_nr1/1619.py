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

int f[11000];
bool v[11000];
void Work() {
  int n, cap;
  input>>n;
  input>>cap;
  int i,j; 
  for (i = 0; i < n; ++i) {
    input>>f[i];
  }
  sort(f,f+n);
  int res = n;
  int use = 0;
  i = n-1;
  memset(v, 0,sizeof(v));
  while (res > 0 && i >=0) {
    if (v[i] == true) {
      --i;
      continue;
    }
    v[i] = true;
    j = i - 1;
    bool p = false;
    for (j = i - 1; j >=0; --j) {
      if (v[j] == false && f[j] + f[i] <= cap) {
        v[j] = true;
        p = true;
        break;
      }
    }
    if (p) {
      res -= 2;
    } else {
      res -= 1;
    }
    use = use + 1;
    //cout<<use<<" "<<res<<" "<<n<<" "<<i<<endl;
  }
  output<<use<<endl;
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
