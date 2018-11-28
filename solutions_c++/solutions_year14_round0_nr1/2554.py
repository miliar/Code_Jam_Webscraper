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
bool pos[16];
in ar;
in c;
int main(){
  in T;
  cin>>T;
  forn(z,T){
    cout<<"Case #"<<z+1<<": ";
    forn(i,16)
      pos[i]=1;
    cin>>c;
    c--;
    forn(i,4){
      forn(j,4){
	cin>>ar;
	ar--;
	if(i!=c)
	  pos[ar]=0;
      }
    }
    cin>>c;
    c--;
    forn(i,4){
      forn(j,4){
	cin>>ar;
	ar--;
	if(i!=c)
	  pos[ar]=0;
      }
    }
    in fp;
    in np=0;
    forn(i,16){
      if(pos[i]){
	fp=i+1;
	np++;
      }
    }
    if(np>1)
      cout<<"Bad magician!"<<endl;
    if(np==1)
      cout<<fp<<endl;
    if(np==0)
      cout<<"Volunteer cheated!"<<endl;
  }
  return 0;
}

