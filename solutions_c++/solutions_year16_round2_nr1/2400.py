#include <bits/stdc++.h>
typedef long long ll;

using namespace std;


int main() {
  ios_base::sync_with_stdio(false);
  ll t;
  cin >> t;
  string s;
  map<char, int> l;
  vector<int>d;
  int j=1;
  while (t--) {
    cin >>s;
    d=vector<int>(10,0);
    for (int i=0; i<(int)s.size(); i++) {
      l[s[i]]++;
    }
    d[0]=l['Z'];
    d[2]=l['W'];
    d[8]=l['G'];
    d[3]=l['H']-d[8];
    d[4]=l['R']-d[3]-d[0];
    d[5]=l['F']-d[4];
    d[6]=l['X'];
    d[7]=l['V']-d[5];
    d[9]=l['I']-d[5]-d[6]-d[8];
    d[1]=l['N']-2*d[9]-d[7];
    cout << "Case #"<<j<<": ";
    j++;
    for (int i=0; i<10; i++) {
      while (d[i]--) cout << i;
    }
    cout <<'\n';
    s.clear();
    l.clear();
  }
  return 0;
}
