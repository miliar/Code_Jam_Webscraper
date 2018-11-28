#include <bits/stdc++.h>
using namespace std;

int main() {
  int test,in,acum,out;
  string st;
  cin>>test;
  for(int ca = 1; ca <= test; ca++){
    out = 0;
    cin>>in>>st;
    int lim;
    acum = 0;
    for(lim = st.size()-1; lim >= 0; lim--)
      if(st[lim] != '0') break;
    for(int i = 1; i <= lim; i++){
      acum += st[i-1] - '0';
      if(acum < i) {
        out++;
        acum++;
      }
    }
    cout<<"Case #"<<ca<<": "<<out<<endl;
  }
  return 0;
}
