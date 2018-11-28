#include <bits/stdc++.h>

#define REP(i,n)    for(int i=0;i<(n);++i)

using namespace std;

char winner(char l, char r) {
  switch (l) {
    case 'R':
      return r == 'P' ? 'P' : 'R';
    case 'P':
      return r == 'R' ? 'P' : 'S';
    case 'S':
      return r == 'R' ? 'R' : 'S';
    default:
      return '\0';
  }
}

bool ok(const string &str) {
  if (str.size() == 1) return true;
  string rec;
  REP(i,str.size()/2) {
    if (str[i*2] == str[i*2+1]) return false;
    rec += winner(str[i*2], str[i*2+1]);
  }
  return ok(rec);
}

/*
map<tuple<n,r,p,s>, string> memo;

string solve(int n, int r, int p, int s) {
  if (n == 1) {
    if (r) return "r";
    if (p) return "p";
    return "s";
  }
  auto itr = memo.find(make_tuple(n,r,p,s));
  if (itr != end(memo)) return *itr;
  string candi;
  int h = 1 << (n-1);
  REP(i,r)REP(j,p) {
    if (i+j > h) break;
    int k = h - (i+j);
    string rec = solve(n-1, i, j, k);
    if (rec != "") {

      if (candi == "" || rec < candi) {
        candi = rec;
      }
    }
  }
}*/
int main() {
  int T;
  cin>>T;
  REP(cnt,T){
    int n,r,p,s;
    cin>>n>>r>>p>>s;
    cout << "Case #" << (cnt+1) << ": ";
    string hoge = string(p,'P') + string(r,'R') + string(s,'S');
    string candi;
    do {
      if (ok(hoge)) {
        if (candi == "" || hoge < candi) {
          candi = hoge;
        }
        break;
      }
    } while(next_permutation(begin(hoge),end(hoge)));
    if (candi == "")
      cout << "IMPOSSIBLE" << endl;
    else
      cout << candi << endl;
  }
  return 0;
}
