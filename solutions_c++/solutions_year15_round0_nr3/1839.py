#include <iostream>
#include <string>
#include <cstdio>
#include <climits>
using namespace std;

pair<bool,char> parse_pair(char const& x,char const& y){
  pair<bool,char> res;
  if (x=='1'){
    res.first=false;
    res.second=y;
  }
  else if (y=='1'){
    res.first=false;
    res.second=x;
  }
  else if (x==y){
    res.first=true;
    res.second='1';
  }
  else{
    if ( (x-'i'+1)%3==(y-'i')%3 ){
      res.first=false;
    }
    else{
      res.first=true;
    }
    res.second='i'+'j'+'k'-x-y;

  }
  return res;
}

int main(){
  freopen("/Users/corey.xpx/Desktop/C-small-attempt0.in","r",stdin);
  freopen("/Users/corey.xpx/Desktop/out.txt","w",stdout);
  int T, cas = 0;
  int L, X;
  string s;
  string t;
  cin >> T;
  while (T--) {
    cin >> L >> X;
    cin >> s;
    for (int i = 0; i < X; i++){
      t.append(s);
    }
    bool flag = false;
    char ch = '1';
    int p = -1, q = -1;
    for (int i = 0; i < t.size(); i++){
      pair<bool,char> res = parse_pair(ch, t[i]);
      flag ^= res.first;
      ch = res.second;
      if (!flag && ch == 'i' && p < 0){
        p = i;
      }
      if (!flag && ch == 'k'){
        q = i;
      }
    }
    bool ans = 0 <= p && 
               p < q && 
               flag && 
               ch=='1';
    cout << "Case #" << ++cas << ": " << (ans ? "YES" : "NO") << endl;
  }

}
