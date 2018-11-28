
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
  a << "{";
  if (v.size()>0) a << v[0];
  for (int i=1; i<v.size(); i++) a << ", " << v[i];
  a << "}";
  return a;
}

string to_bin(LL x, int Nbits) {
  string ans;
  for (int i=Nbits-1; i>=0; i--)
    ans.push_back( (x & (1LL << i)) ? '1' : '0' );
  return ans;
}

void print_rest(int N) {
  for (int i=1; i<N; i++) {
    for (int j=0; j<N; j++) {
      char x = (j>i) ? '1' : '0'; 
      cout << x;
    }
    cout << endl;
  }
}

int main() {
  int TC;
  cin >> TC;
  for (int tc=0; tc<TC; tc++) {
    int N;
    LL M, max_m;
    cin >> N >> M;
    max_m = (1LL << (N-2));
    cout << "Case #" << tc+1 << ": ";
    if (M > max_m) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << "POSSIBLE" << endl;
      string first_row;
      if (M == max_m) {
        first_row = "0" + to_bin(M-1,N-2) + "1";
      } else {
        first_row = "0" + to_bin(M, N-2) + "0";
      }
      cout << first_row << endl;
      print_rest(N);
    }
  }
}
