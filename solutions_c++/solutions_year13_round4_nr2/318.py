#include <iostream>
#include <cmath>
#include <algorithm>

#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long

using namespace std;

int cs,n;
ll p,team,l,r,r1,r2;

bool f(ll mid){
  ll pcnt = p;
  ll tcnt = team;
  ll rem = mid;

  while(rem>0){
    rem--;rem/=2;
    tcnt /= 2;
    pcnt -= tcnt;
    if(pcnt<=0)return false;
  }
  if(pcnt>0)return true;
  else return false;
  
}


int main(){

  cin>>cs;
  rep(ii,cs){
    cin>>n>>p;team = 1; while(n--)team*=2;
    l = 0; r=team;
    while(r-l>1){
      ll mid = (l+r)/2;
      if(f(mid))l=mid;
      else r = mid;
    }
    r1 = l;
    p = team-p;

    l = -1; r = team;

    while(r-l>1){
      ll mid = (l+r)/2;
      if(f(mid))l=mid;
      else r = mid;
    }
    r2 = team-1-r;
    cout<<"Case #"<<ii+1<<": "<<r1<<" "<<r2<<endl;

  }




}
