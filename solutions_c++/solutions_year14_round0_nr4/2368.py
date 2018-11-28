#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
using namespace std;
typedef long long in;
in wns(vector<double> u, vector<double> v){
  sort(u.begin(),u.end());
  sort(v.begin(),v.end());
  reverse(u.begin(),u.end());
  reverse(v.begin(),v.end());
  in r=0;
  in j=0;
  forv(i,u){
    while(j<sz(v) && v[j]>u[i])
      j++;
    if(j<sz(v)){
      r++;
      j++;
    }
  }
  return r;
}
vector<double> flp(vector<double> u){
  forv(i,u)
    u[i]=2.0-u[i];
  return u;
}
int main(){
  in T;
  cin>>T;
  forn(z,T){
    cout<<"Case #"<<z+1<<": ";
    in n;
    cin>>n;
    vector<double> u,v;
    u.resize(n);
    v.resize(n);
    forn(i,n)
      cin>>u[i];
    forn(i,n)
      cin>>v[i];
    cout<<wns(flp(v),flp(u))<<" "<<n-wns(v,u)<<endl;
  }
  return 0;
}

