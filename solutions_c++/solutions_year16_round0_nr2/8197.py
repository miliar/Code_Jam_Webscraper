#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;++i)
#define rep(i,n) REP(i,0,n)

using namespace std;


struct Data {
  string state;
  int cost;
  bool operator < ( const Data & data ) const {
    if( cost != data.cost ) return cost > data.cost;
    return state < data.state;
  }
};

string convert(string s) {
  string ret = "";
  rep(i,(int)s.size()) {
    if( i == 0 || s[i] != s[i-1] ) {
      ret += s[i];
    }
  }
  return ret;
}

int main() {
  /*
  map<string,int> mini;
  priority_queue<Data> Q;
  REP(i,1,11) {
    Q.push((Data){string(i,'+'),0});
    mini[string(i,'+')] = 0;
  }

  while( !Q.empty() ) {
    Data data = Q.top(); Q.pop();
    string state = data.state;
    rep(i,(int)state.size()) {
      string nstate = state;
      for(int j=i;j>=0;--j) nstate[i-j] = ((state[j]=='+')?'-':'+');
      if( mini.count(nstate) ) {
        if( mini[nstate] > data.cost + 1 ) {
          mini[nstate] = data.cost + 1;
          Q.push((Data){nstate,data.cost+1});
        }
      } else {
        mini[nstate]= data.cost + 1;
        Q.push((Data){nstate,data.cost+1});
      }
    }
  }
  puts("--");
  */
/*
+   0
-   1
+-  2,4,6,8,10
+-+ 2,4,6,8
-+- 3,5,7,9
-+  1,3,5,7,9
 */
  int T,CNT=1;
  cin >> T;
  while( T-- ) {
    cout << "Case #" << CNT++ << ": ";
    string s;
    cin >> s;
    //cout << "ANS : " << mini[s] << endl;
    s = convert(s);
    bool check = true;
    rep(i,(int)s.size()) if( s[i] == '-' ) { check = false; break; }
    if( check ) { puts("0"); continue; }
    check = true;
    rep(i,(int)s.size()) if( s[i] == '+' ) { check = false; break; }
    if( check ) { puts("1"); continue; }
    if( s[0] == '+' && s[(int)s.size()-1] == '-' )  {
      printf("%d\n",2*(int)((int)s.size()/2));
    } else if( s[0] == '+' && s[(int)s.size()-1] == '+' )  {
      printf("%d\n",2*(int)(((int)s.size()-1)/2));
    } else if( s[0] == '-' && s[(int)s.size()-1] == '-' )  {
      printf("%d\n",1+2*(int)(((int)s.size()-1)/2));
    } else if( s[0] == '-' && s[(int)s.size()-1] == '+' )  {
      printf("%d\n",1+(2*(int)(((int)s.size()/2)-1)));
    }
    
  }
  return 0;
}
