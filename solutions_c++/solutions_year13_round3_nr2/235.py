#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())

int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};
string w="NESW";

map<pair<int, int>, int> gezien;
vi X, Y, S, R, P;

int main()
{
  int i,j,k,l; char buf[1000];
  X.pb(0); Y.pb(0); S.pb(0); R.pb(-1); P.pb(-1);
  set<pair<int,int> > klein;

  int y,x,s;
  for(i=0;i<sz(X);i++) {
    y=Y[i]; x=X[i]; s=S[i];
    if(s==500) break;
    for(int r=0;r<4;r++) {
      int ns=s+1;
      int nx=x+dx[r]*ns,ny=y+dy[r]*ns;
      if(nx<-200||ny<-200||nx>200||ny>200) continue;
      pair<int,int> p=make_pair(nx,ny);
      if(gezien.find(p)==gezien.end()) {
        if(nx>=0&&ny>=0&&nx<=100&&ny<=100) klein.insert(p);
        gezien[p]=sz(X);
        X.pb(nx); Y.pb(ny); S.pb(ns); R.pb(r); P.pb(i);
      }
    }

  }

  int keeses; scanf("%d",&keeses);
  for(int kees=1;kees<=keeses;kees++) {
    scanf("%d %d", &x, &y);
    i=gezien[make_pair(x,y)];
    string ans;
    while(i!=0) {
      ans+=w[R[i]];
      i=P[i];
    }
    reverse(ans.begin(),ans.end());
    printf("Case #%d: %s\n",kees,ans.c_str());
  }



  return 0;
}
