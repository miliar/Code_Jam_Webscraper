#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>
#include<map>
#include<set>
using namespace std;
void solve(int level, int r, int p, int s, string& res) {
  int sum = r + p + s;
  if (sum == 1) {
    if (r) res="R";
    if (p) res="P";
    if (s) res="S";
    return;
  }
  if (sum %2 != 0 || sum/2 < r || sum/2 < p || sum/2 < s) {
    res = "IMPOSSIBLE";
    return;
  }
  int tr = sum/2-p, tp =sum/2-s, ts=sum/2-r;
  solve(level + 1, tr, tp, ts, res);
  if (res != "IMPOSSIBLE"){
    string t = "";
    for (int i = 0;i <res.size();i++){
      char c=res[i];
      if(c=='R') {
        if (level == 0)
          t+="RS";
        else
          t+="SR";
      }
      if(c=='P') {
        t+="PR";
      }
      if(c=='S') {
        t+="PS";
      }
    }
    res = t;
  }
}
string minimize(const string& s) {
  if (s.size()==1)return s;
  string s1 = minimize(s.substr(0, s.size()/2));
  string s2 = minimize(s.substr(s.size()/2,s.size()/2));
  if(s1<s2)return s1+s2;
  return s2 + s1;
}
int main() {
  int T;
  scanf("%d",&T);
  for(int tn=1;tn<=T;tn++){
    int r,p,s,n;
    scanf("%d%d%d%d",&n,&r,&p,&s);
    string res;
    solve(0, r, p, s, res);
    if(res=="IMPOSSIBLE")
      printf("Case #%d: IMPOSSIBLE\n", tn);
    else
      printf("Case #%d: %s\n", tn, minimize(res).c_str());
  }
  return 0;
}
