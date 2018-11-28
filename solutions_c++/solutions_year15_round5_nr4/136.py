#include <iostream>
#include <vector>
#include <utility>
#include <map>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> mono;
typedef vector<mono> poly;
bool is_divisible(const poly& p, ll N){
  map<ll, ll> S;
  for (int i=0;i<p.size();++i){
    ll q = p[i].first/N;
    ll r = p[i].first-q*N;
    if (r<0){
      --q;
      r+=N;
    }
    if (q%2==0)
      S[r] += p[i].second;
    else
      S[r] -= p[i].second;
  }
  for (map<ll, ll>::iterator it=S.begin();it!=S.end();++it)
    if (it->second!=0)
      return false;
  return true;
}
poly div(const poly& p, ll N){
  map<ll, ll> res;
  for (int i=0;i<p.size();++i){
    ll x=p[i].first;
    ll c=p[i].second;
    while (x<0 || x>=N){
      if (x>=N){
        res[x-N] += c;
        c = -c;
        x -= N;
      }
      else{
        res[x] += c;
        c = -c;
        x += N;
      }
    }
  }
  poly ret;
  for (map<ll, ll>::iterator it=res.begin(); it!=res.end();++it){
    if (it->second!=0)
      ret.push_back(*it);
  }
  return ret;
}
istream& operator>>(istream& inp, poly& p){
  p.clear();
  int n;inp>>n;
  vector<ll> v(n);
  for (int i=0;i<n;++i)
    inp>>v[i];
  for (int i=0;i<n;++i){
    ll f;inp>>f;
    p.push_back(make_pair(v[i], f));
  }
  return inp;
}
ostream& operator<<(ostream& out, const poly& p){
  for (int i=0;i<p.size();++i)
    out<<'('<<p[i].first<<','<<p[i].second<<')'<<' ';
  return out;
}
poly p;
vector<ll> cands;
vector<ll> ans;
map<ll, bool> dyn[100];
int main(){
  int tnum, tcou=0;cin>>tnum;
  while (tnum--){
    ans.clear();
    cands.clear();
    for (int i=0;i<100;++i)
      dyn[i].clear();
    cin>>p;
    for (int i=0;i<p.size();++i)
      if (p[i].first!=0)
        cands.push_back(abs(p[i].first));
    sort(cands.begin(), cands.end());
    cands.resize(unique(cands.begin(), cands.end())-cands.begin());
    for (int i=(int)cands.size()-1;i>=0;--i)
      while (is_divisible(p, cands[i])){
        p=div(p, cands[i]);
        ans.push_back(cands[i]);
      }
    ll sum = abs(p[0].first);
    if (ans.size()>0){
      dyn[ans.size()].clear();
      dyn[ans.size()][0] = true;
      for (int i=ans.size()-1;i>=0;--i){
        for (map<ll, bool>::iterator it=dyn[i+1].begin();it!=dyn[i+1].end();++it)
          dyn[i][it->first] = false;
        for (map<ll, bool>::iterator it=dyn[i+1].begin();it!=dyn[i+1].end();++it)
          dyn[i][it->first+ans[i]] = true;
      }
      for (int i=0;i<ans.size();++i){
        if (dyn[i][sum]){
          ans[i] = -ans[i];
          sum -= ans[i];
        }
      }
    }
    ll c = p[0].second;
    while (c>1){
      ans.push_back(0);
      c/=2;
    }
    sort(ans.begin(), ans.end());
    cout<<"Case #"<<++tcou<<":";
    for (int i=0;i<ans.size();++i)
      cout<<' '<<ans[i];
    cout<<endl;
  }
  return 0;
}
