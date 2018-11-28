#include <vector>
#include <string>
#include <iostream>
#include <queue>
#include <map>
using namespace std;

int DEBUG=0;

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

int doit(int R, int C, vector<string> g) {
  int mp[256];
  mp['<']=0;
  mp['>']=1;
  mp['^']=2;
  mp['v']=3;
  int u[101][101];
  memset(u,0,sizeof(u));
  int ret=0;
  if(DEBUG) cout<<"!"<<endl;
  for(int i=0;i<R;i++) for(int j=0;j<C;j++) {
    if(u[i][j]) continue;
    if(g[i][j]=='.') continue;
    u[i][j]=1;
    int dir=mp[g[i][j]];
    int y=i,x=j;
    bool found=false;
    y+=dy[dir]; x+=dx[dir];
    for(;;) {
      if(y<0||y>=R||x<0||x>=C) { if(found) ret++; break; }
      if(g[y][x]=='.') { y+=dy[dir]; x+=dx[dir]; continue; }
      if(u[y][x]) { found=true; break; }
      u[y][x]=1;
      dir=mp[g[y][x]];
      found=true;
      y+=dy[dir]; x+=dx[dir];
    }
if(DEBUG)    cout<<i<<" "<<j<<" "<<"found="<<found<<endl;
    if(found) continue;
    ret++;
    for(int idx=0;idx<4;idx++) {
      int y=i,x=j;
      bool found=false;
      dir=idx;
      y+=dy[dir]; x+=dx[dir];
if(DEBUG) cout<<i<<" "<<j<<" "<<y<<" "<<x<<" "<<endl;
      for(;;) {
//        if(DEBUG) cout<<y<<" "<<x<<endl;
        if(y<0||y>=R||x<0||x>=C) { if(found) ret++; break; }
        if(g[y][x]=='.') { y+=dy[dir]; x+=dx[dir]; continue; }
        if(u[y][x]) {found=true; break; }
        u[y][x]=1;
        dir=mp[g[y][x]];
        found=true;
        y+=dy[dir]; x+=dx[dir];
      }   
      if(found) break;
      if(idx==3) return -1;
    } 
//    cout <<"#"<<i<<" "<<j<<" "<<ret<<endl;
  }
  return ret;
}      

int main() {
  int tests;
  cin >> tests;
  for(int i = 0; i < tests; i++) {    
    int R, C;
    cin>>R>>C;
    vector<string> g;
    for(int j=0;j<R;j++) {
      string s;
      cin>>s;
      g.push_back(s);
    }
    DEBUG=0;
    int val=doit(R,C,g);
    if(val==-1)      cout << "Case #" << (i+1) << ": " << "IMPOSSIBLE" << endl;
    else cout << "Case #" << (i+1) << ": " << doit(R,C,g) << endl;
  }
  return 0;
}
