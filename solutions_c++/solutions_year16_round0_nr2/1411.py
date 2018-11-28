

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

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

char cflip(char c) {
  return (c=='+')?'-':'+';
}

void flip(string& s, int size) {
  int i=0, j=size-1;
  while (i < j) {
    s[i] = cflip(s[i]);
    s[j] = cflip(s[j]);
    swap(s[i], s[j]);
    i++; j--;
  }
  if (i==j) s[i] = cflip(s[i]);
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  cin.tie(NULL);
  string pancakes;
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    cin >> pancakes;
    int nops = 0;
    int j=pancakes.size()-1;
    while (true) {
      while (j>=0 && pancakes[j]=='+') j--;
      if (j<0) break;
      int i=0;
      while (pancakes[i]=='+') i++;
      if (i>0) {
        flip(pancakes, i);
        //cout << pancakes << endl;
        nops++;
      }
      flip(pancakes, j+1);
      //cout << pancakes << endl;
      nops++;
    }
    cout << "Case #" << tc << ": ";
    cout << nops << endl;
  }
}
