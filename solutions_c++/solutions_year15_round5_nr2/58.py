#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define fors(i,s) for(auto i=(s).begin();i!=(s).end();++i)
#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long in;
typedef vector<in> VI;
typedef vector<VI> VVI;
VI s;
VI mn,mx;
void docase(){
  in n,k;
  cin>>n>>k;
  s.resize(n-k+1);
  forv(i,s)
    cin>>s[i];
  mn=VI(k,0);
  mx=VI(k,0);
  in maxd=0;
  forn(i,k){
    in cr=0;
    in cl=i;
    while(cl+k<n){
      cr+=(s[cl+1]-s[cl]);
      cl+=k;
      mn[i]=min(mn[i],cr);
      mx[i]=max(mx[i],cr);
    }
    maxd=max(maxd,mx[i]-mn[i]);
  }
  in goalss=s[0];
  in curss=0;
  forn(i,k){
    mx[i]-=mn[i];
    curss-=mn[i];
  }
  in nxt=0;
  while(nxt<k && (curss-goalss)%k!=0){
    if(mx[nxt]<maxd){
      mx[nxt]++;
      curss++;
    }
    else
      nxt++;
  }
  if((curss-goalss)%k==0)
    cout<<maxd<<endl;
  else
    cout<<maxd+1<<endl;
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in T;
  cin>>T;
  for(in zz=1;zz<=T;zz++){
    cout<<"Case #"<<zz<<": ";
    docase();
  }
  return 0;
}
