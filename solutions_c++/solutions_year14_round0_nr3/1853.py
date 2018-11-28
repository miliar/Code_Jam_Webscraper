#include <bits/stdc++.h>
using namespace std;

const int dx[] = {1, 0, -1, 0, 1, 1, -1, -1};
const int dy[] = {0, 1, 0, -1, 1, -1, 1, -1};

struct State{
  int x, y;
  State(int x, int y) : x(x), y(y){}  
};

int Cx, Cy;
int H, W, M;
char field[55][55];
char tmp[55][55];

bool is_in(int x, int y){
  return 0 <= x && x < W && 0 <= y && y < H;
}

void init(){
  for(int i = 0 ; i < 55 ; i++)
    for(int j = 0 ; j < 55 ; j++) field[i][j] = tmp[i][j] = '.';
}

void make(){
  int x = 0, y = 0;
  field[y][x] = '*';
  M--;
  while(M > 0){
    for(int i = 0 ; i < 4 ; i++){
      while(true){
	int nx = x + dx[i], ny = y + dy[i];
	  if(!is_in(nx, ny) || field[ny][nx] == '*' || M <= 0) break;
	  field[ny][nx] = '*';
	  y = ny, x = nx;
	  M--;
      }
    }
  }
}

bool isValid(){
  int asta = 0;

  for(int i = 0 ; i < H ; i++){
    for(int j = 0 ; j < W ; j++){
      if(field[i][j] == '.' || field[i][j] == 'c'){
	int cnt = 0;
	for(int d = 0 ; d < 8 ; d++){
	  int nx = j + dx[d], ny = i + dy[d];
	  if(nx < 0 || ny < 0 || nx >= W || ny >= H) continue;
	  if(field[ny][nx] == '*') cnt++;
	}
	tmp[i][j] = cnt+'0';	
      }
      else tmp[i][j] = '*', asta++;
    }
  }
  
  
  bool used[55][55];

  for(int Y = 0 ; Y < H ; Y++){
    for(int X = 0 ; X < W ; X++){
      if(tmp[Y][X] != '0') continue;
      queue<State> que;
      que.push(State(X, Y));
      memset(used, false, sizeof(used));      
      int C = 0;
      while(!que.empty()){
	State q = que.front(); que.pop();
	if(used[q.y][q.x]) continue;
	used[q.y][q.x] = true;
	C++;
	if(tmp[q.y][q.x] != '0') continue;
	
	for(int k = 0 ; k < 8 ; k++){
	  int nx = q.x + dx[k], ny = q.y + dy[k];
	  if(!is_in(nx, ny) || tmp[ny][nx] == '*') continue;
	  que.push(State(nx, ny));
	}
      }
      if(asta + C == H*W){
	Cx = X, Cy = Y;
	return true;
      }
    }
  }
  return false;
}
  /*
  for(int i = 0 ; i < H ; i++){
    for(int j = 0 ; j < W ; j++){
      if(tmp[i][j] == '*'){
	used[i][j] = true;
	continue;
      }
      
      if(tmp[i][j] == '0'){
	used[i][j] = true;
	for(int k = 0 ; k < 8 ; k++){
	  int nx = j + dx[k], ny = i + dy[k];
	  if(is_in(nx, ny)) used[ny][nx] = true;	
	}
      }
    }
  }
  
  for(int i = 0 ; i < H ; i++){
    for(int j = 0 ; j < W ; j++){
      if(!used[i][j]) return false;
    }
  }
  return true;  
}
  */

void Output(){
  for(int i = 0 ; i < H ; i++){
    for(int j = 0 ; j < W ; j++){
      if(i == Cy && j == Cx){
	cout << 'c';
	continue;
      }
      cout << field[i][j];
    }
    cout << endl;
  }
}

void print(){
  for(int i = 0 ; i < H ; i++){
    for(int j = 0 ; j < W ; j++){
      cout << field[i][j];
    }
    cout << endl;
  }      
  cout << endl;
}

void solve(){
  for(int bit = 0 ; bit < (1<<(H*W)) ; bit++){
    if(__builtin_popcount(bit) != M) continue;
    
    init();
    
    int cnt = 0;
    for(int i = 0 ; i < H ; i++){
      for(int j = 0 ; j < W ; j++){
	if( bit & 1 << cnt ) field[i][j] = '*';
	cnt++;
      }
    }    

    //print();
    
    if(isValid()){
      Output();
      return;
    }
  }
  cout << "Impossible" << endl;
}

int main(){
  int T;
  cin >> T;
  for(int tc = 1 ; tc <= T ; tc++){
    cin >> H >> W >> M;
    
    cout << "Case #" << tc << ":" << endl;
    
    if(M == H*W-1){
      for(int i = 0 ; i < H ; i++){
	for(int j = 0 ; j < W ; j++){
	  if(i == H-1 && j == W-1) break;
	  cout << '*';
	}
	if(i == H-1) cout << 'c';
	cout << endl;
      }
      continue;
    }    
    
    solve();
  }  
  return 0;
}
