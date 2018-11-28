#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>

#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define sz size()
#define pb push_back
#define mp make_pair
#define ALL(X) (X).begin(),(X).end()

using namespace std;

typedef long long ll;
typedef vector<int> vi;

void output(int c, long long n, long long m)
{ printf ("Case #%d: %lld %lld\n", c, n, m); }

int main(void)
{
  int t,n;
  long long p;
  cin >> t;
  FOR(cas,1,t+1){
    cin >> n >> p;
    long long a=p;
    int cnt=-1;
    while(a>0){
      cnt++;
      a/=2;
    }
    long long res1=0;
    REP(i,n){
      res1*=2; 
      if(i<cnt)res1++;
    }
    long long b=p;
    p--;
    cnt=0;
    REP(i,n){
      if(p%2==1)cnt++;else cnt=0;
      p/=2;
    }
    long long res2=1;
    REP(i,cnt+1)res2=res2*2;
    res2-=2;
    if(cnt==n)res2=b-1;
    output(cas,res2,res1);
  }
  return 0;
}
