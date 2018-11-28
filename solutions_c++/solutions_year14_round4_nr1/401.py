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
vector<in> s;
int main(){
  in T;
  cin>>T;
  forn(zz,T){
    cout<<"Case #"<<zz+1<<": ";
    in n,x;
    cin>>n>>x;
    s.resize(n);
    forn(i,n)
      cin>>s[i];
    sort(s.begin(),s.end());
    in i=0;
    in j=n-1;
    in d=0;
    while(i<=j){
      d++;
      if(s[i]+s[j]<=x)
	i++;
      j--;
    }
    cout<<d<<endl;
  }
  return 0;
}

