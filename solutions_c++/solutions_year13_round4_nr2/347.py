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

void run(){
  int tsts; cin>>tsts;
  for (int tst=1; tst<=tsts; ++tst){

    ll n,p; cin>>n>>p; ll m=1ll<<n;

    ll must=0;
    ll might=0;

    for (ll i=-1,rad=m; rad; rad>>=1ll){
      ll x=i+rad; if (x>=m) continue;

      ll score=0;
      ll better=x;
      ll remaining=m;

      for (int j=0; j<n; j++, remaining/=2ll){
        better=min(better,remaining-1);
        score=score*2+(better!=remaining-1);
        better=(better+1)/2ll;
      }

      if (score>=m-p) might=i=x, rad<<=1ll;
    }

    for (ll i=-1,rad=m; rad; rad>>=1){
      ll x=i+rad; if (x>=m) continue;

      ll score=0;
      ll worse=m-x-1;
      ll remaining=m;

      for (int j=0; j<n; j++, remaining/=2ll){
        worse=min(worse,remaining-1);
        score=score*2+(worse==remaining-1);
        worse=(worse+1)/2;
      }

      if (score>=m-p) must=i=x, rad<<=1ll;
    }

    cout<<"Case #"<<tst<<": "<<must<<" "<<might<<endl;
  }
}

