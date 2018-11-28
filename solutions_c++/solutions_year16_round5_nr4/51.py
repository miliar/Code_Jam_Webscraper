#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define F first
#define S second
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)(x).size())
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) {
  return s<<"("<<p.first<<","<<p.second<<")";
}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ ";
  for (auto it : c) s << it << " ";
  s<<"]";
  return s;
}
// Let's Fight!

const int MAXN = 202;

int N, L;
string good[MAXN], bad;

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>N>>L;
    for(int i=0; i<N; i++)
      cin>>good[i];
    cin>>bad;

    bool ok = true;
    for(int i=0; i<N; i++)
      if(good[i] == bad)
        ok = false;

    cout<<"Case #"<<t<<": ";
    if(!ok)
      cout<<"IMPOSSIBLE"<<endl;
    else if(L == 1)
    {
      cout<<"0 0?"<<endl;
    }
    else
    {
      for(int i=0; i<L-1; i++) cout<<"1";
      cout<<" ";
      for(int i=0; i<L; i++) cout<<"0?";
      cout<<endl;
    }
  }
  return 0;
}
