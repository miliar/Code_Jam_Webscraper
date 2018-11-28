#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cstring>
#include <queue>
#include <map>
using namespace std;
typedef long long ll;
const int maxn = 100005;

int main() {
  //freopen("in.cpp","r",stdin);
  freopen("A-large.in","r",stdin);
  freopen("A.l.out","w",stdout);
  int T,ncase=0;
  cin>>T;
  while(T--) {
    string s;
    int m;
    cin>>s>>m;
    int ret=0;
    for(int i=0; i+m-1<s.size(); i++) {
      if(s[i]=='+')continue;
      ret++;
      for(int j=i; j<i+m; j++)s[j]=(s[j]=='+'?'-':'+');
    }
    bool sign=0;
    for(int i=0; i<s.size(); i++)if(s[i]=='-') {
        sign=1;
        break;
      }
    if(sign)cout<<"Case #"<<++ncase<<": "<<"IMPOSSIBLE"<<endl;
    else cout<<"Case #"<<++ncase<<": "<<ret<<endl;
  }
  return 0;
}
