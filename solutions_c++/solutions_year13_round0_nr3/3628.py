#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

#define debug(x) cerr<<#x<<" = "<<(x)<<endl;

using namespace std;
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define VAR(a,b) __typeof(b) a=(b)
#define REVERSE(c) reverse(ALL(c))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define MINN(X,Y) ((X) > (Y) ? (Y) : (X))
#define MAXX(X,Y) ((X) < (Y) ? (Y) : (X))
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long ULL;

int a[1000], b[1000];
set<ULL> all;

void solve()
{
  //  printf("\n");
  int a,b;
  cin>>a>>b;
  //  debug(a);
  //  debug(b);
  int cnt=0;
  for( set<ULL>::iterator it = all.begin();
       it!=all.end();
       it++)
    {
      if(*it >= a && *it<=b)
	cnt++;
    }
  cout<<cnt<<endl;
}


bool isGood( ULL i)
{
  stringstream ss;
  ss<<i;

  for(int i=0, j=ss.str().size()-1; i<j; i++,j--)
    {
      if(ss.str()[i] != ss.str()[j])
	return false;
    }
  return true;
}

void prep()
{
  for(ULL i=1; i<100000000; i++)
    {
      bool good= isGood(i);
      //debug(i);debug(good);
      if(good)
	{
	  ULL sq = i*i;
	  if(isGood(sq))
	    {
	      //cout<<i*i<<endl;
	    all.insert(i*i);
	    }
	}
    }
  //cout<<"done"<<endl;

}



int main()
{
  int T;
  prep();
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        solve();
    }
  return 0;
}
