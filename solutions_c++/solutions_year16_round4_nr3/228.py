#include <iostream>
#include <vector>
using namespace std;

int R,C;
int dfs(const vector<vector<int> >& grid, int r, int c, int w) {
  if(r==-1) return 1+c;
  if(c==C) return 1+C+r;
  if(r==R) return 1+C+R+(C-1-c);
  if(c==-1) return 1+C+R+C+(R-1-r);
  int g = grid[r][c];
  if(g) {
    if(w==0) return dfs(grid, r, c+1, 3);
    if(w==1) return dfs(grid, r-1, c, 2);
    if(w==2) return dfs(grid, r, c-1, 1);
    if(w==3) return dfs(grid, r+1, c, 0);
  } else {
    if(w==2) return dfs(grid, r, c+1, 3);
    if(w==3) return dfs(grid, r-1, c, 2);
    if(w==0) return dfs(grid, r, c-1, 1);
    if(w==1) return dfs(grid, r+1, c, 0);
  }
}
int rr[100], cc[100];

int doit(const vector<vector<int> >& grid, int x) {
  int r=rr[x], c=cc[x];
  if(r==-1) return dfs(grid, r+1, c, 0);
  if(c==C) return dfs(grid, r, c-1, 1);
  if(r==R) return dfs(grid, r-1, c, 2);
  if(c==-1) return dfs(grid, r, c+1, 3);
}

int main(void) {
  int T; cin >> T;
  for(int ts=1; ts<=T; ts++) {
    cout << "Case #" << ts << ":" << endl;
    cin >> R >> C;
    vector<int> v(R+R+C+C);
    for(int i=0; i<R+R+C+C; i++) cin >> v[i];
    vector<vector<int> > grid(R, vector<int>(C));
    /*for(int r=-1; r<=R; r++) {
      for(int c=-1; c<=C; c++) {
        cout << dfs(r,c,0) << " ";
      }
      cout << endl;
    }*/
    int r,c;
    r=-1; for(int c=0; c<C; c++) { int x = dfs(grid, r, c, 0); rr[x]=r; cc[x]=c; }
    r=R;  for(int c=0; c<C; c++) { int x = dfs(grid, r, c, 0); rr[x]=r; cc[x]=c; }
    c=-1; for(int r=0; r<R; r++) { int x = dfs(grid, r, c, 0); rr[x]=r; cc[x]=c; }
    c=C;  for(int r=0; r<R; r++) { int x = dfs(grid, r, c, 0); rr[x]=r; cc[x]=c; }
    //for(int x=1; x<=R+R+C+C; x++) cout << x << ": " << rr[x] << " " << cc[x] << endl;
    bool done=false;
    for(int msk=0; msk<(1<<R*C); msk++) {
      for(int r=0; r<R; r++) for(int c=0; c<C; c++) {
        int i=r*C+c;
        grid[r][c]=(msk&(1<<i))?1:0;
      }
      bool good=true;
      for(int i=0; i<v.size(); i+=2) if(doit(grid,v[i]) != v[i+1]) good=false;
      if(good) {
        done=true;
        for(int r=0; r<R; r++) {
          for(int c=0; c<C; c++) {
            cout << (grid[r][c]? '\\' : '/');
          }
          cout << endl;
        }
        break;
      }
    }
    if(!done) {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
