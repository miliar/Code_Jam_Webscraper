#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
#define PB push_back
#define MP make_pair
#define sz(v) ((v).size())
#define forn(i,n) for(int i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
typedef long long in;
typedef unsigned long long int llu;

void runtc();

int main(){
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);

  int ntc;
  cin>>ntc;
  for(int i=0;i<ntc;++i) {
    cout<<"Case #"<<(i+1)<<": ";
    runtc();
    cout<<endl;
  }
  
  return 0;
}

const char BLANK = '.';
int R, C;
vector<string> g;

bool march(int r, int c, pair<int,int> dir) {
  int rpp = dir.first;
  int cpp = dir.second;
  int rr = r;
  int cc = c;
  while(1){
    rr+=rpp;
    cc+=cpp;
    if(rr<0 || rr>=R || cc<0 || cc>=C) {
      return false;
    }
    if(g[rr][cc]!=BLANK){
      return true;
    }
  }
}
//=============================================================================
void runtc() {
  cin>>R>>C;
  g.clear();
  forn(i,R) {
    string s;
    cin>>s;
    g.push_back(s);
  }
  map<char,pair<int,int>> dir;
  dir['^'] = pair<int,int>(-1,0);
  dir['v'] = pair<int,int>( 1,0);
  dir['<'] = pair<int,int>( 0,-1);
  dir['>'] = pair<int,int>( 0, 1);

  in res = 0;
  forn(r,R){
    forn(c,C){
      if(g[r][c]!=BLANK) {
        if(!march(r,c,dir[g[r][c]])) {
          res++;
        }
        bool ok=march(r,c,dir['^']) || march(r,c,dir['v']) || march(r,c,dir['<']) || march(r,c,dir['>']);
        if(!ok) {
          cout<<"IMPOSSIBLE";
          return;
        }
      }
    }
  }

  cout<<res;
}
