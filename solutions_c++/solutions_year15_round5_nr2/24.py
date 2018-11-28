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

const int MAXN = 1010;

int N, K;
int s[MAXN];

int calc()
{
  vector<int> diffs;
  int tot = 0;

  for(int i=0; i<K; i++)
  {
    vector<int> vec;
    vec.PB(0);
    for(int j=0; j*K+i+1<N-K+1; j++)
    {
      vec.PB(vec.back() + s[j*K+i+1] - s[j*K+i]);
    }
    sort(vec.begin(), vec.end());
    int lb = vec[0], rb = vec.back();
    diffs.PB(rb-lb);
    tot += lb;
    tot %= K;
  }

  tot = (((tot+s[0])%K)+K)%K;
  int cap = 0;
  sort(diffs.begin(), diffs.end());
  for(auto v: diffs)
    cap += diffs.back() - v;

  int ans = diffs.back();
  if(cap < tot)
    ans++;

  return ans;
}

int main()
{
  IOS;
  int T;
  cin>>T;
  for(int tt=1; tt<=T; tt++)
  {
    cin>>N>>K;
    for(int i=0; i<N-K+1; i++)
      cin>>s[i];
    int ans = calc();
    cout<<"Case #"<<tt<<": "<<ans<<endl;
  }

  return 0;
}
