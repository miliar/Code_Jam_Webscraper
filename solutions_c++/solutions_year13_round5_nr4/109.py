#include <functional>/*{{{*/
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;typedef long long ll;typedef long double real;void run();int main(){ios::sync_with_stdio(0);run();}/*}}}*/

bool did[21][1<<20];
real dp[21][1<<20];

int rot(int x,int n){
  return (x|((x&1)<<n))>>1;
}

real solve(int n,int mask){
  if (mask+1==(1<<n)) return 0;

  for (int a=mask,b=n; a=rot(a,n),b--;){
    mask=min(mask,a);
  }

  if (not did[n][mask]){
    did[n][mask]=true;

    int wait[20];
    for (int i=0; i<n; i++)
      if (not (mask&(1<<i)))
        wait[i]=i;
      else
        wait[i]=-1;

    int woot=-1;
    for (int u=2; u--;){
      for (int i=0; i<n; i++){
        if (wait[i]!=i and woot!=-1){
          wait[i]=woot;
        }
        if (wait[i]!=-1){
          woot=wait[i];
        }
      }
    }

    for (int i=0; i<n; i++){
      dp[n][mask] += solve(n,mask|(1<<wait[i])) + (n-((i-wait[i]+n)%n));
    }
    dp[n][mask]/=n;

    if (false){
      for (int i=0; i<n; i++)
        cout<<" "<<wait[i]<<(mask&(1<<i)?'X':'.');
        cout<<endl;
      cout<<"   => "<<dp[n][mask]<<endl;
    }

  }
  return dp[n][mask];
}

void run(){
  int tsts; cin>>tsts;
  cout.precision(13);

  for (int tst=1; tst<=tsts; ++tst){

    string s; cin>>s; int n=s.size();

    int orig=0;
    for (char i:s) orig=orig*2+(i=='X');

    printf("Case #%d: %.13Lf\n",tst,solve(n,orig));
  }
}

