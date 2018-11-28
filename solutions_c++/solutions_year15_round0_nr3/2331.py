#include <iostream>
#include <string>
#include <vector>
using namespace std;
long long M[4][4] = {
  {0,1,2,3},
  {1,4,3,6},
  {2,7,4,1},
  {3,2,5,4}
};

void process(const string& str,long long X, vector<long long>&V){
  X = min(X,12+X%4);
  V.resize(str.length()*X);
  for(long long i=0;i<X;++i){
    for(long long j=0;j<str.length();++j){
      V[i*str.length()+j] = str[j]-'h';
    }
  }
}

long long muilt(long long a, long long b){
  bool neg = false;
  if(a>=4){
    a %= 4;
    neg = !neg;
  }
  if(b>=4){
    b %= 4;
    neg = !neg;
  }
  long long ans = M[a][b];
  if(ans >= 4){
    ans %= 4;
    neg = !neg;
  }
  return ans + (neg?4:0);
}
int main(){
  int T;cin >> T;
  long long idx = 0;
  while(T--){
    ++idx;
    long long L,X;cin >> L >> X;
    string str;cin >>str;
    vector<long long>V;
    process(str, X, V);
    long long cur = 0;
    long long exp[]={1,2,3}; long long expid = 0;
    for(long long i=0;i<V.size();++i){
      cur = muilt(cur,V[i]);
      if(expid<2){
        if(cur == exp[expid]){
          ++expid;
	  cur = 0;
        }
      }
    }
    if(expid==2 && cur==3)
      cout << "Case #"<<idx<<": "<<"YES"<<endl;
    else
      cout << "Case #"<<idx<<": "<<"NO"<<endl;
  }
  return 0;
}
