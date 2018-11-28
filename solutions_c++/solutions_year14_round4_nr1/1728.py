#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
using namespace std;

#define mp make_pair
#define pb push_back
#define all(c) c.begin(),c.end()

typedef pair<int,int> pii;
typedef long long ll;

int N,X,S[10005];

int solve()
{
  cin>>N>>X;
  vector<int> s;
  for(int i=1;i<=N;i++)
    {
      scanf("%d",S+i);
      s.pb(S[i]);
    }
  sort(all(s));
  int ret=0;
  while(!s.empty())
    {
      int val = s.back();
      s.pop_back();
      auto it = upper_bound(all(s),X-val);
      if(it!=s.begin())
	  s.erase(--it);
      ret++;
    }
  return ret;
}

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    cout<<"Case #"<<t<<": "<<solve()<<endl;
  
  return 0;
}
