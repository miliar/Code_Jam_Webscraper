#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;

#define mod (1000002013)

long long get (int n, int d)
{
  return (n*1ll*d-(d*1ll*(d+1))/2)%mod;
}

long long res1, res2;
multiset <pair <int, int> > S;
pair <int, int> B[1100], C[1100];
pair <pair <int, int>, int> A[1100];

int main()
{
  int tst, cnt, n, m, s, l, r, i;
  pair <int, int> p;
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    printf("Case #%d: ", cnt);
    cerr<<cnt<<endl;
    res1=0, res2=0;
    scanf("%d%d", &n, &m);
    for (i=0; i<m; i++)
    {
      scanf("%d%d%d", &A[i].first.first, &A[i].first.second, &A[i].second), res1+=A[i].second*1ll*get(n,A[i].first.second-A[i].first.first), res1%=mod;
      B[i]=mp(A[i].first.first,A[i].second), C[i]=mp(A[i].first.second,A[i].second);
      assert(B[i].first<C[i].first);
      //assert(A[i].second<=100);
    }
    sort(B,B+m), sort(C,C+m), l=0, r=0;
    long long bal=0;
    while (l<m || r<m)
    {
      //cerr<<l<<" "<<r<<"    "<<S.size()<<"    "<<bal<<endl;
      assert(bal>=0);
      //if (S.size())
      //  cerr<<"!!   "<<S.begin()->first<<" "<<S.begin()->second<<endl;
      if (l!=m && (r==m || B[l].first<=C[r].first))
      {
        S.insert(mp(-B[l].first,B[l].second)), bal+=B[l].second, l++;
        continue;
      }
      //cerr<<bal<<endl;
      while (C[r].second>0)
      {
        //assert(C[r].second<=100);
        assert(bal>=0);
        assert(S.size());
      //  cerr<<"???"<<endl;
        p=(*S.begin()), S.erase(S.begin()), bal-=p.second;
        s=min(p.second,C[r].second), res2+=s*1ll*get(n,C[r].first+p.first), res2%=mod;
        assert(s);
        //cerr<<"TTT   "<<s<<endl;
      //  cerr<<"????????????3"<<endl;
        C[r].second-=s, p.second-=s;
        if (p.second>0)
          S.insert(p), bal+=p.second;
    //    cerr<<"??????2"<<endl;
      }
      //if (S.size())
      //  cerr<<"!!   "<<S.begin()->first<<" "<<S.begin()->second<<endl;
      r++;
    }
   // cerr<<"YTTTTTTTTTTTT"<<endl;
    assert(!S.size());
    cout<<(res1-res2+mod)%mod<<endl;
  }
  return 0;
}
