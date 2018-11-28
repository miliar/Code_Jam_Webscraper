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
in n,p,q,r,s;
vector<in> nt;
int main(){
  in T;
  cin>>T;
  forn(zz,T){
    cout<<"Case #"<<zz+1<<": ";
    cin>>n>>p>>q>>r>>s;
    nt.resize(n);
    in tot=0;
    forn(i,n){
      nt[i]=(i*p+q)%r+s;
      tot+=nt[i];
    }
    in left=tot;
    in right=0;
    in mid=0;
    in a=n;
    in b=n-1;
    in best=tot;
    while(right<=left || right<=mid){
      if(left>=mid){
	a--;
	left-=nt[a];
	mid+=nt[a];
      }
      else{
	right+=nt[b];
	mid-=nt[b];
	b--;
      }
      if(right<best && mid<best && left<best){
	if(right<mid){
	  if(mid<left)
	    best=left;
	  else
	    best=mid;
	}
	else{
	  if(left<right)
	    best=right;
	  else
	    best=left;
	}
      }
    }
    cout<<setprecision(15)<<(tot-best)/double(tot)<<endl;
  }
  return 0;
}

