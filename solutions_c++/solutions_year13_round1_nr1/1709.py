#include <iostream>
#include <algorithm>
#include <cmath>

#define ll long long 
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int cs;
ll r,t,n;
double rd,td;

int main(){

  cin>>cs;
  rep(ii,cs){
    cin>>r>>t;
    rd = (double)r;
    td = (double)t;

    ll ln = 0,rn = t;

    while(rn-ln>1){
      ll m = (ln+rn)/2;
      double md = (double)m;

      if(((rd*2.0+md*2.0-1.0)*md)<=td){
	if(((2*r+2*m-1)*m)<=t){
	    ln = m;
	  }
      }
      else rn = m;
    }
    cout<<"Case #"<<ii+1<<": "<<ln<<endl;
  }
}
