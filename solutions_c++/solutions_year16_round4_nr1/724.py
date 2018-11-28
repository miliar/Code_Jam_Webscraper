#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int t;
  cin >> t;
  vector<string> strp, strs, strr, poss;
  strp.push_back("P");
  strr.push_back("R");
  strs.push_back("S");
  for (int i=0; i<13; ++i) {
    string sp = strp[i], ss = strs[i], sr = strr[i];
    strp.push_back(sp<sr?sp+sr:sr+sp);
    strs.push_back(ss<sp?ss+sp:sp+ss);
    strr.push_back(sr<ss?sr+ss:ss+sr);
  }
  for(int i=0;i<strp.size();++i){
    poss.push_back(strp[i]);
    poss.push_back(strr[i]);
    poss.push_back(strs[i]);
  }
  vector<int> cr, cp, cs;
  for (int i=0; i<poss.size(); ++i) {
    cr.push_back(0);
    cp.push_back(0);
    cs.push_back(0);
    for (int j=0; j<poss[i].size(); ++j) {
      if (poss[i][j] == 'R')
        cr.back()++;
      else if (poss[i][j] == 'P')
        cp.back()++;
      else
        cs.back()++;
    }
    //cout <<poss[i] << ' ' << cr[i] << ' ' << cp[i] << ' ' <<cs[i] <<endl;
  }
  for (int ta=1; ta<=t; ++ta) {
    cout << "Case #" << ta << ": ";
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string ans="";
    for (int i=0; i<poss.size(); ++i) {
      if (cr[i]==r && cp[i] == p && cs[i]==s) {
        if (ans == "" || ans < poss[i])
          ans = poss[i];
      }
    }
    if(ans == "") {
      ans = "IMPOSSIBLE";
    }
    cout << ans << endl;
  }
}