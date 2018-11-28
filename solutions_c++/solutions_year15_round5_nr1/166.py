#include <iostream>
#include <utility>
#include <vector>
using namespace std;
typedef long long ll;
struct seq{
  ll x, a, c, r;
  ll next(){
    ll ret = x;
    x = (x*a+c)%r;
    return ret;
  }
};
istream& operator>>(istream& inp, seq& s){
  return inp>>s.x>>s.a>>s.c>>s.r;
}
int n, D;
seq S, P;
int s[1000000];
int p[1000000];
pair<int, int> I[1000000];
vector<pair<int, bool> > e;
int main(){
  int tnum, tcou=0;cin>>tnum;
  while (tnum--){
    cin>>n>>D>>S>>P;
    for (int i=0;i<n;++i){
      s[i] = S.next();
      p[i] = P.next();
      if (i==0)
        p[i] = -1;
      else
        p[i] = p[i]%i;
    }
    I[0] = make_pair(s[0], s[0]);
    for (int i=1;i<n;++i){
      I[i] = I[p[i]];
      I[i].first = min(I[i].first, s[i]);
      I[i].second = max(I[i].second, s[i]);
    }
    e.clear();
    for (int i=0;i<n;++i){
      if (I[i].second - I[i].first>D)
        continue;
      e.push_back(make_pair(I[i].second-D, true));
      e.push_back(make_pair(I[i].first+1, false));
    }
    sort(e.begin(), e.end());
    int num=0, ii=0;
    int ans=0;
    while (ii<e.size()){
      int j;
      for (j=ii;j<e.size()&&e[j].first==e[ii].first;++j){
        if (e[j].second)
          ++num;
        else
          --num;
      }
      ans = max(ans, num);
      ii = j;
    }
    cout<<"Case #"<<++tcou<<": "<<ans<<endl;
  }
  return 0;
}
