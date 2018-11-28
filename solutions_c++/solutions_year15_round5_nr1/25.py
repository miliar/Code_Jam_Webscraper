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

typedef pair<int, int> pii;

const int MAXN = 1010101;

int N, D;
int S0, AS, CS, RS, M0, AM, CM, RM;
int s[MAXN], m[MAXN];
int lb[MAXN], rb[MAXN];
vector<int> ch[MAXN];
pii seg[MAXN];

void init()
{
  s[0] = S0;
  m[0] = M0;
  for(int i=1; i<N; i++)
  {
    s[i] = (s[i-1] * AS + CS) % RS;
    m[i] = (m[i-1] * AM + CM) % RM;
  }
  for(int i=1; i<N; i++)
    m[i] %= i;
  m[0] = -1;
}

void dfs(int v)
{
  if(m[v] != -1)
  {
    lb[v] = min(lb[v], lb[m[v]]);
    rb[v] = max(rb[v], rb[m[v]]);
  }
  for(auto c: ch[v])
    dfs(c);
}

void make_tree()
{
  for(int i=0; i<N; i++)
    ch[i].clear();
  for(int i=1; i<N; i++)
    ch[m[i]].PB(i);
  for(int i=0; i<N; i++)
    lb[i] = rb[i] = s[i];
  dfs(0);
}

int calc()
{
  for(int i=0; i<N; i++)
  {
    seg[i] = MP(rb[i], lb[i]);
  }

  sort(seg, seg+N);

  int maxans = 0;

  int pos = 0;
  multiset<int> vcur;
  for(int i=0; i<=RS; i++)
  {
    while(pos<N && seg[pos].F <= i)
    {
      vcur.insert(seg[pos].S);
      pos++;
    }
    while(!vcur.empty())
    {
      auto it = vcur.begin();
      if(*it < i-D)
        vcur.erase(it);
      else
        break;
    }
    maxans = max(maxans, (int)vcur.size());
  }

  return maxans;
}

int main()
{
  IOS;
  int T;
  cin>>T;
  
  for(int tt=1; tt<=T; tt++)
  {
    cin>>N>>D;
    cin>>S0>>AS>>CS>>RS>>M0>>AM>>CM>>RM;
    init();
    make_tree();
    int ans = calc();
    cout<<"Case #"<<tt<<": "<<ans<<endl;
  }

  return 0;
}
