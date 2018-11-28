using namespace std;
#include <cmath>
#include <cstdio>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef long long ll; 
typedef pair<int,int> pii; 
#define FOR(i,n) for (int i = 0; i < n; i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define MP make_pair
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d\n",x)
#define split(str) {vs.clear();istringstream ss(str);while(ss>>(str))vs.push_back(str);}
#define PI 3.141592653589793
#define MOD 1000002013
int main()
{
  int t;
  sf(t);
  int temp = 1;
  while(t--)
  {
    ll actual = 0;
    ll cheat = 0;
    int n, m;
    sf(n); sf(m);
    vector<pii > entry;
    vector<pii > exit;
    while(m--)
    {
      int o,e,p;
      sf(o); sf(e); sf(p);
      ll i = e-o;
      i = n*i*2 + i - i*i;
      i /= 2;
      if(i >= MOD) i %= MOD;
      actual = (actual + (i*p)%MOD)%MOD;
      entry.PB(MP(o,p));
      exit.PB(MP(e,p));
    }
    sort(all(entry));
    sort(all(exit));
    pii tickets[1005];
    int i = 0;
    int j = 0;
    int ticki = 0;
    while(i < exit.size())
    {
      while(j < entry.size() && entry[j].first <= exit[i].first)
      {
	tickets[ticki++] = entry[j];	
	j++;
      }
      int p = exit[i].second;
      while(p>0)
      {
	int pass = min(p,tickets[ticki - 1].second);
	ll k = exit[i].first-tickets[ticki - 1].first;
	k = n*k*2 + k - k*k;
	k /= 2;
	if(k >= MOD) k %= MOD;
	cheat = (cheat + (k*pass)%MOD)%MOD;
	p -= pass;
	tickets[ticki - 1].second -= pass;
	if(tickets[ticki - 1].second == 0)
	  ticki --;
      }
      i++;	
    }
    printf("Case #%d: %lld\n",temp,(actual - cheat + MOD)%MOD);
    temp++;
  }
}