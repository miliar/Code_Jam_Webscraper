#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define ri(X) scanf("%d", &(X))
#define pi(X) printf("%d", (X))
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define lint long long
#define pii pair<int,int>
#define inf 1e9
#define linf 1e18
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define uni(X) X.erase(unique(X.begin(), X.end()), X.end());



int f(vector<int> ve){
  int i = 0;
  int k = ve.size()-1;
  
  int result = 0;
  while(k >= 0){
    if(ve[k] == 1){
      k--;
      continue;
    }
    if(ve[0] == 1){
      ve[0] = 0;
      result++;
    }
    reverse(ve.begin(), ve.begin()+k+1);
    for(int i = 0; i <= k; i++){
      ve[i] = !ve[i];
    }
    result++;
  }
  return result;
}


vector<int> stov(string s){
  vector<int> res;
  for(int i = 0; i < s.size();i++){
    res.pb(s[i]=='+'?1:0);
  }
  return res;
}

vector<int> compress(vector<int>ve){
  vector<int> res;  
  for(int i = 0; i < ve.size(); i++){
    if(res.size() > 0 &&  res.back() == ve[i]) continue;
    res.pb(ve[i]);
  }
  return res;
}


// BEGIN TEST
vector<int> itov(int p, int siz){
  
  vector<int> ve;
  for(int k = 0; k < siz; k++){
    ve.pb(p%2);
    p/=2;
  }
  return ve;
}

int vtoi(vector<int> ve){
  int result = 0;
  for(int i = 0; i < ve.size(); i++){
    if(ve[i] == 0) continue;
    result = result | (1<<i);
  }
  return result;
}


void pv(vector<int> ve){
  for(int i = 0; i < ve.size(); i++){
    printf("%d", ve[i]);
  }cout << endl;
}
bool end(vector<int> vu){
  for(int i = 0; i < vu.size(); i++){
    if(vu[i] == 0) return 0;
  }
  return 1;
}

int ftest(vector<int> ve){
  set<int> visit;
  map<int,int> d;
  queue<int> Q;
  int si = vtoi(ve);
  visit.insert(si);
  d[si] = 0;
  Q.push(si);
  
  int su, sv;
  vector<int> vu, vv;
  while(!Q.empty()){
    su = Q.front();
    Q.pop();
    vu = itov(su, ve.size());
    
    if(end(vu)) return d[su];
    
    for(int k = 1; k <= ve.size(); k++){
      vv = vu;
      
      reverse(vv.begin(), vv.begin()+k);
      for(int i = 0; i < k; i++){
        vv[i] = !vv[i];
      }
      
      sv = vtoi(vv);
      if(visit.count(sv) > 0) continue;
      visit.insert(sv);
      d[sv] = d[su] + 1;
      Q.push(sv);
    }
    
    
   
    
  }
  
  
  
}

int test(){
  int n = 0;
  for(int siz = 12; siz <= 12; siz++){
    int ss = 1<< siz;
    for(int s = 0; s < ss; s++){
      vector<int> vi = itov(s, siz);
      
      
      int r1 = ftest(vi);
      int r2 = f(compress(vi));
      if(r1 != r2){
        pv(vi);
        pv(compress(vi));
        printf("%d %d\n", r1, r2);
        exit(0);
      }
    } 
  }
}
// END TEST;




int main(){
  
  int T;
  string s;
  cin >> T;
  for(int t = 0; t < T; t++){
    cin >> s;
    vector<int> ve = compress(stov(s));
    //cout << s << " ";
    //pv(ve);
    printf("Case #%d: %d\n", t+1, f(ve));
  }
  return 0;
}

