#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
// Let's Fight!

typedef long long ll;

const int MAXP = 10101;

int P;
int S;
ll e[MAXP], f[MAXP];
map<ll, int> inv;
vector<ll> nvec, ans;

bool can_make(vector<ll> vec, ll target)
{
  set<int> s;
  s.insert(0);
  for(auto v: vec)
  {
    set<int> t = s;
    for(auto u: s)
      t.insert(u+v);
    s = t;
  }
  return s.count(target);
}

void calc_vec()
{
  inv.clear();
  for(int i=0; i<P; i++)
    inv[e[i]] = i;
  nvec.clear();
  ll tot = 0;
  for(int i=0; i<P; i++)
    tot += f[i];
  S = __lg(tot);
  assert(tot == 1LL<<S);

  for(int i=0; i<S; i++)
  {
    ll x = 0;
    int sum = 0;
    for(int j=0; j<P; j++)
    {
      sum += f[j];
      if(sum >= 2)
      {
        x = e[j];
        break;
      }
    }
    x -= e[0];
    nvec.PB(x);

    if(x == 0)
    {
      for(int j=0; j<P; j++)
        f[j] /= 2;
      continue;
    }

    for(int j=0; j<P; j++)
    {
      if(f[j] == 0) continue;
      int pos = inv[e[j] + x];
      f[pos] -= f[j];
    }
  }

  sort(nvec.begin(), nvec.end());
  reverse(nvec.begin(), nvec.end());

  assert((int)nvec.size() == S);
  ans.clear();
  ll target = -e[0];
  for(int i=0; i<S; i++)
  {
    vector<ll> tmp;
    for(int j=i+1; j<S; j++)
      tmp.PB(nvec[j]);
    if(can_make(tmp, target-nvec[i]))
    {
      target -= nvec[i];
      ans.PB(-nvec[i]);
    }
    else
      ans.PB(nvec[i]);
  }

  ll test = 0;
  for(int i=0; i<S; i++)
    if(ans[i] < 0)
      test += ans[i];
  assert(test == e[0]);

  sort(ans.begin(), ans.end());
}

int main()
{
  IOS;
  int T;
  cin>>T;
  for(int tt=1; tt<=T; tt++)
  {
    cin>>P;
    for(int i=0; i<P; i++)
      cin>>e[i];
    for(int i=0; i<P; i++)
      cin>>f[i];
    calc_vec();
    cout<<"Case #"<<tt<<":";
    for(auto v: ans)
      cout<<" "<<v;
    cout<<endl;
  }
  return 0;
}
