#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cassert>
#include<iomanip>
#define PB push_back
#define sz(v) (in((v).size()))
#define forn(i,n) for(in i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
using namespace std;
typedef long long in;
int main(){
  in T;
  cin>>T;
  forn(z,T){
    cout<<"Case #"<<z+1<<": ";
    double c,f,x;
    cin>>c>>f>>x;
    double p=2;
    double t=0;
    double best=x/p;
    while(t<best){
      if(x/p+t<best)
	best=x/p+t;
      t+=c/p;
      p+=f;
    }
    cout<<setprecision(15)<<best<<endl;
  }
  return 0;
}

