#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<stack>
using namespace std;
struct large_than{
bool operator() (const string& x, const string& y){
  return (x.compare(y) < 0);
}
};
struct small_than{
bool operator() (const string& x, const string& y){
  return (y.compare(x) < 0);
}
};
string halfsort(string s){
  if(s.length() == 1) return s;
  string l = s.substr(0, s.length()/2);
  string r = s.substr(s.length()/2, s.length()/2);
  l = halfsort(l);
  r = halfsort(r);
  string c = "";
  if(l.compare(r) < 0){
    c += l;
    c += r;
  }
  else{
    c += r;
    c += l;
  }
  return c;
}

bool calc(vector<int> &R, vector<int> &P, vector<int> &S, int d, int lim){
  if(d == lim) return true;
  if(R[d]+P[d] < S[d] || R[d]+S[d] < P[d] || S[d]+P[d]<R[d]){
    return false;
  }
  else{
    R[d+1] = (R[d] + S[d] - P[d]) / 2;
    S[d+1] = (S[d] + P[d] - R[d]) / 2;
    P[d+1] = (P[d] + R[d] - S[d]) / 2;
    return calc(R, P, S, d+1, lim);
  }
}
int main(){
  int t, n, r, p, s;
  scanf("%d", &t);
  for(int i=1; i<=t; i++){
    scanf("%d %d %d %d", &n, &r, &p, &s);
    vector<int> R, P, S;
    R = vector<int>(n+1, 0);
    S = vector<int>(n+1, 0);
    P = vector<int>(n+1, 0);
    R[0] = r;
    S[0] = s;
    P[0] = p;
    bool able = calc(R, P, S, 0, n);
    printf("Case #%d: ", i);
    if(!able){
      printf("IMPOSSIBLE\n");
    }
    else{
      string s = "";
      if(R[n] == 1)
        s = "R";
      else if(P[n] == 1)
        s = "P";
      else
        s = "S";
      for(int j = n-1; j >=0; j--){
        string re = "";
        for(char c : s){
          switch(c){
            case 'R':
              re += "RS";
              break;
            case 'P':
              re += "PR";
              break;
            case 'S':
              re += "PS";
              break;
            default:
              break;
          }
        }
        s = re;
        //vector<string> sorts = vector<string>();
        //sorts.push_back(s.substr(0, s.length()/2));
        //sorts.push_back(s.substr(s.length()/2, s.length()/2));
        s = halfsort(s);
        //sort(sorts.begin(), sorts.end(),large_than());
      }
      /*vector<string> sorts = vector<string>();
      for(int i=0; i<pow(2, n-1); i++){
        sorts.push_back(s.substr(2 * i, 2));
      }
      string res = "";
      for(string ss : sorts)
        res += ss; */
      cout << s << '\n';
    }

  }
  return 0;
}
