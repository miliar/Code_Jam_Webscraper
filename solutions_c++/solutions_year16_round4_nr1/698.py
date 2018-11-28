#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 100030;    // Change as necessary
const ll  MODD = 1000000009; //

map<pair<int,char>,string> M;

string f(int depth,char root){
  if(depth == 0) return string(1,root);
  if(M.count(make_pair(depth,root))) return M[make_pair(depth,root)];
  
  string t;
  switch(root){
    case 'R': t += "RS"; break;
    case 'S': t += "PS"; break;
    case 'P': t += "PR"; break;
    default: assert(false);
  }
  
  string t1 = f(depth-1,t[0]);
  string t2 = f(depth-1,t[1]);
  
  return M[make_pair(depth,root)] = min(t1,t2) + max(t1,t2);
}

map<string,string> ans;

void do_case(){
  int n,a,b,c;
  cin >> n >> a >> b >> c;
  
  string t = string(b,'P')+string(a,'R')+string(c,'S');
  if(ans.count(t) == 0){
    cout << "IMPOSSIBLE" << endl;
  } else
    cout << ans[t] << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  string t = "RPS";
  for(int i=0;i<3;i++)
    for(int j=0;j<14;j++){
      string x = f(j,t[i]);
      string y = x;
      sort(y.begin(),y.end());
      ans[y] = x;
    }
  
  int T,C=1; cin >> T;
  
  while(T--){
    cout << "Case #" << C++ << ": ";
    do_case();
  }
  
  return 0;
}
