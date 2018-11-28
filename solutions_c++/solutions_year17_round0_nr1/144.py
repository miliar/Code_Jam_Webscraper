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
void dot(){
  string s;
  in k;
  cin>>s>>k;
  in sm=0;
  for(in i=0;i+k<=sz(s);++i){
    if(s[i]=='-'){
      ++sm;
      for(in j=i;j-i<k;++j){
	if(s[j]=='+')
	  s[j]='-';
	else
	  s[j]='+';
      }
    }
  }
  forv(i,s){
    if(s[i]=='-'){
      cout<<"IMPOSSIBLE"<<endl;
      return;
    }
  }
  cout<<sm<<endl;
}
int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  in t;
  cin>>t;
  forn(z,t){
    cout<<"Case #"<<(z+1)<<": ";
    dot();
  }
  return 0;
}
