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

#define FOR(i,k,n)  for (int i=(k); i<(int)(n); ++i)
#define REP(i,n)    FOR(i,0,n)
#define FORIT(i,c)	for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define sz          size()
#define pb          push_back
#define mp          make_pair
#define ALL(X)      (X).begin(),(X).end()

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int a[128][128];

void output(int cas,string str){
  cout<<"Case #"<<cas<<": "<<str<<endl;
  return;
}

int main(void)
{
  int t;
  cin>>t;
  FOR(cas,1,t+1){
    int n,m;
    cin>>n>>m;
    REP(i,n)REP(j,m)cin>>a[i][j];
    bool flag=true;
    REP(i,n)REP(j,m){
      bool fl=true;
      REP(k,m)if(a[i][j]<a[i][k])fl=false;
      if(fl)continue;
      fl=true;
      REP(k,n)if(a[i][j]<a[k][j])fl=false;
      if(!fl)flag=false;
    }
    if(flag)output(cas,"YES");
    else output(cas,"NO");
  }
  return 0;
}
