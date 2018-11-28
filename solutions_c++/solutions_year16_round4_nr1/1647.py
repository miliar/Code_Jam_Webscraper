#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;
int n,r,p,s;

string abc(int pp, int rr, int ss,string cand) {
  string ret = "";
  for(int i=1; i<=n; i++) {
    if(rr == r && pp == p && ss == s) {
      if( ret == "" || cand < ret) ret = cand;
      break;
    }
    int tr = rr;
    int ts = ss;
    int tp = pp;
    rr =0; ss =0; pp =0;
    rr += tp;
    pp += tp;
    rr += tr;
    ss += tr;
    pp += ts;
    ss += ts;
    string tmp = cand;
    cand = "";
    for(int j=0; j< tmp.size(); j+=2) {
      string ccc = tmp.substr(j, 2);
      if(ccc == "PS") {
        cand = cand + "PRPS";
      }
      if(ccc == "PR") {
        cand = cand + "PRRS";
      }
      if(ccc == "RS") {
        cand = cand + "PSRS";
      }
    }
    string cand1 = cand.substr(0,cand.size()/2);
    string cand2 = cand.substr(cand.size()/2, cand.size()/2);
    string cand3 = cand2 +  cand1;
    cand = min(cand, cand3);
  }

  return ret;
}
int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    cin >> n >> r >> p >> s;
    string ret = "";
    string c1 = abc(1,1,0,"PR");
    string c2 = abc(0,1,1,"RS");
    string c3 = abc(1,0,1,"PS");

    if(c1 != "") ret = c1;
    if(c2 != "") ret = c2;
    if(c3 != "") ret = c3;

    printf("Case #%d: ",tc);
    if(ret!= "") {
      cout << ret << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}