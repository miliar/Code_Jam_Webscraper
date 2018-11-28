#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;


int a[64][64];
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int d8x[] = {1, 1, 1, -1, -1,-1, 0, 0};
int d8y[] = {0, 1, -1, 1, -1, 0, 1,-1};

int N, M, cnt;

int valid(int x, int y){
  if(x < 0 || y < 0)
    return 0;
  if(x >= N || y >= M)
    return 0;
  return 1;
}

int neighbours(int i, int j){
  int res = 0;
  
  for(int dir = 0; dir < 8; ++dir){
    int nx = i + d8x[dir], ny = j + d8y[dir];
    if(!valid(nx, ny))
      continue;
    res += a[nx][ny];
  }
  return res;
}

int zeroNeighbour(int x, int y){
  for(int dir = 0; dir < 8; ++dir){
    int nx = x + d8x[dir], ny = y + d8y[dir];
    if(!valid(nx, ny))
      continue;
    if(a[nx][ny])
      continue;
    if(!neighbours(nx, ny))
      return 1;
  }
  
  return 0;
}

void print(){ 
  int cntt  = 0;
  for(int i = 0; i < N; ++i){
    for(int j = 0; j < M; ++j)
      if(a[i][j] == 0){
	if((cntt == 0 && neighbours(i,j) == 0)||N*M == cnt + 1){
	  cout << 'c';
	  cntt = 1;
	}
	else cout << '.';
      }
      else{
      cout << '*';
      }
    cout << endl;
  }
}

int ok(){
  int used[64][64];
  memset(used, 0, sizeof(used));
 
  int x = -1, y = -1;
  
  for(int i = 0; i < N; ++i)
    for(int j = 0; j < M; ++j)
      if(neighbours(i, j) == 0 && a[i][j] == 0){
	 x = i;
	 y = j;
      }
 // cout << x << " " << y << endl;
  queue < pair<int, int> > q;
  if(x == -1)
    return 0;
  
  q.push( make_pair(x, y) );
  used[x][y] = 1;
  while(!q.empty()){
    x = q.front().first;
    y = q.front().second;
    q.pop();
    
    for(int i = 0; i < 8; ++i){
      int nx = d8x[i] + x, ny = d8y[i] + y;
      if(valid(nx,ny) == 0)
	continue;
      if(a[nx][ny])
	continue;
      if(used[nx][ny])
	continue;
      used[nx][ny] = 1;
      
      if(!neighbours(nx, ny)){
	q.push(make_pair(nx, ny));
      }
    }
  }
  for(int i = 0; i < N; ++i)
    for(int j = 0; j < M; ++j)
      if(!used[i][j] && !a[i][j]){
	//cout << i << " " << j << endl;
	return 0;
      }
  return 1;
}
void solve(int test){
  cout << "Case #" << test << ":\n";
  memset(a, 0, sizeof(a));
  cin >> N >> M >> cnt;
  
  for(int d = 0; d < (1 << (N*M)); ++d){
    if( __builtin_popcount(d) != cnt )
      continue;
    for(int i = 0; i < N * M; ++i)
      a[i / M][i % M] = (bool)( (1 << i) & d);
    
    if(ok() || cnt == N * M - 1 ){
      print();
      return;
    }
  }
  
  cout << "Impossible\n";
}
int main(){
  int tests;
  cin >> tests;
  
  for(int i = 1; i <= tests; ++i){
    solve(i);
  }
}