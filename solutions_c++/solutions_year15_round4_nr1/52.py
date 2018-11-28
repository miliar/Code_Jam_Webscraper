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
vector<string> bd;
void docase(){
  in n,m;
  cin>>n>>m;
  bd.resize(n);
  forn(i,n)
    cin>>bd[i];
  in cg=0;
  forn(i,n){
    forn(j,m){
      if(bd[i][j]=='.')continue;
      bool hrd=0;
      forn(k,n)
	if(k!=i && bd[k][j]!='.')
	  hrd=1;
      forn(k,m)
	if(k!=j && bd[i][k]!='.')
	  hrd=1;
      if(!hrd){
	cout<<"IMPOSSIBLE"<<endl;
	return;
      }
      in dx=0;
      in dy=0;
      if(bd[i][j]=='^')
	dx=-1;
      if(bd[i][j]=='v')
	dx=1;
      if(bd[i][j]=='>')
	dy=1;
      if(bd[i][j]=='<')
	dy=-1;
      in cx=i;
      in cy=j;
      do{
	cx+=dx;
	cy+=dy;
      }while(cx>=0 && cx<n && cy>=0 && cy<m && bd[cx][cy]=='.');
      if(cx>=0 && cx<n && cy>=0 && cy<m)
	cg--;
      cg++;
    }
  }
  cout<<cg<<endl;
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
