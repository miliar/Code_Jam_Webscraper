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

ll v[40];
ll s[40];

void run(){
  ll tsts; cin>>tsts;
  cout.precision(10);

  for (ll tst=1; tst<=tsts; ++tst){

    ll b,n; cin>>b>>n;
    memset(v,0,sizeof v);
    for (ll i=0; i<n; i++) cin>>v[i];
    sort(v,v+37);
    v[37]=1ll<<60ll;
    for (ll i=0; i<=37; i++) s[i+1]=s[i]+v[i];

    real best=0;
/*
    ll same=0;
    for (ll least=v[0]; least<=v[0]+b; ++least){
      ll cost=0;

      while (v[same]<=least) ++same;
      cost=least*same-s[same];

      // number of bets on winning places
      ll winners=cost;

      for (ll inc=0; inc<=min(same-1,b-cost); ++inc){
        ll adds=cost+inc; // number of bets placed in total, including pushes
        ll good=same-inc; // number of places which might win

        winners=cost-least*inc+(s[same]-s[same-inc]);

        best=max(best,
          36.L*(cost-least*inc+(s[same]-s[same-inc]))/(same-inc)
          -(cost+inc)
        );
      }
    }
*/

    for (ll x=1; x<=37; x++){
      for (ll y=x; y<=37; y++){

        ll basis = v[y-1]*y-s[y] + (y-x); // equate + inc(x..y)
        ll basix = v[y-1]*x-s[x];

        ll lef=0;
        ll rad=4;
        while (basis+rad*y<=b) rad<<=1ll;
        rad<<=2ll;

        if (v[y-1]<v[y] and basis<=b){
          best=max(best,36.L*basix/x-basis);
        }
        else continue;

        while (rad){
          rad/=2ll;
          ll add=lef+rad;

          if (v[y-1]+add<v[y] and basis+add*y<=b){
            best=max(best,36.L*(basix+add*x)/x-(basis+add*y));
            lef=add;
          }
        }

      }
    }

    cout<<"Case #"<<tst<<": "<<fixed<<best<<endl;
  }
}

