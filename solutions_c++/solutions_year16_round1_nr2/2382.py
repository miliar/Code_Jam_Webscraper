#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

vector<vi> lines;

int grid[55][55];
int N;


bool f(int i, int r, int c, bool used, int rused=-1, int cused=-1){
  if(!used && r<N && f(i,r+1,c,true, r, -1)){
    for(int c1=0;c1<N;c1++)
      cout<<grid[r][c1]<<' ';
    return true;
  }
  if(!used && c<N && f(i,r,c+1,true, -1, c)){
    for(int r1=0;r1<N;r1++)
      cout<<grid[r1][c]<<' ';
    return true;
  }
  if(i==lines.size()){
    return used;
  }
  if(r<N){// use it as rth row
    int c1 = 0;
    for(c1=0;c1<c && (grid[r][c1]==lines[i][c1] || c1==cused);c1++);
    if(c1==c){
      for(;c1<N;c1++){
	grid[r][c1]=lines[i][c1];
      }
      if(cused!=-1)
	grid[r][cused]=lines[i][cused];
      if(f(i+1,r+1,c,used, rused, cused))
	return true;
    }
  }
  if(c<N){
    int r1 = 0;
    for(r1=0;r1<r && (grid[r1][c]==lines[i][r1] || r1==rused);r1++);
    if(r1==r){
      for(;r1<N;r1++){
	grid[r1][c]=lines[i][r1];
      }
      if(rused!=-1)
	grid[rused][c]=lines[i][rused];

      if(f(i+1,r,c+1,used, rused, cused))
	return true;
    }
  }
  return false;
}

int main(){
  ios_base::sync_with_stdio(0);
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    lines.clear();
    cin>>N;
    for(int i=1;i<2*N;i++){
      vi v(N);
      for(int& e:v)
	cin>>e;
      lines.push_back(v);
    }
    sort(lines.begin(),lines.end());
    memset(grid,0,sizeof(grid));
    cout<<"Case #"<<t<<": ";
    f(0,0,0,0);
    cout<<endl;
  }
  return 0;
}
