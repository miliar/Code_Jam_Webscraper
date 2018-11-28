#include <iostream>
#include <map>
#include <vector>
#include <complex>
#include <stack>
#include <stdio.h>
using namespace std;
typedef vector <vector<char> > MineMap;
typedef pair<int,int> P;
int dx[8] = {-1, 0, 1,-1, 1,-1, 0, 1};
int dy[8] = {-1,-1,-1, 0, 0, 1, 1, 1};


void printmatrix(MineMap &matrix){
  for(int i = 0 ; i < matrix.size() ;i++){
    for(int j = 0; j < matrix[i].size() ; j++){
      cout << matrix[i][j];
    }
    cout << endl;
  }
}
bool isValidMap(MineMap &matrix,const int R ,const int C){
  vector<vector<int> > SurroundMine(R,vector<int>(C,0)),SurroundBlank(R,vector<int>(C,0));
  vector<vector<char> > visited(R,vector<char>(C,0));
  int mineCount = 0;
  P star ;
  for(int i = 0; i < R ; i++){
    for(int j = 0; j < C ; j++){
      if(matrix[i][j] == '*'){
	SurroundMine[i][j] = -1;
	mineCount++;
	continue;
      }
      for(int k = 0; k < 8 ; k++){
	int X = i + dx[k];
	int Y = j + dy[k];
	if( X>= 0 && X <R && Y >= 0 && Y < C ) {
	  if(matrix[X][Y] == '*') SurroundMine[i][j]++;
	}
      }
      if(SurroundMine[i][j] == 0)star = make_pair(i,j);
    }
  }
  stack<P> st;
  st.push(star);
  int count = 0;
  while(!st.empty()){

    P now = st.top();
    st.pop();
    if(visited[now.first][now.second])continue;
    visited[now.first][now.second] =1;
    count ++;
    if(SurroundMine[now.first][now.second] != 0)continue;
    for(int i = 0; i < 8 ; i++){
      int X = now.first + dx[i];
      int Y = now.second+ dy[i];
      if(X >= 0 && X < R && Y >= 0  && Y < C){
	if(visited[X][Y])continue;
	if(SurroundMine[X][Y] >= 0){
	  st.push(P(X,Y));
	}
      }
    }
  }
  if(count + mineCount  < R * C)return false;
  for(int i = 0  ; i< R*C ; i++){
    int X = i / C;
    int Y = i % C;
    if(matrix[X][Y] !='*' && SurroundMine[X][Y] == 0){
      matrix[X][Y] = 'c';
      break;
    }
  }
  return true;
}
bool search(const int R ,const int C ,const int now_index,const int max_index,const int restMine ,MineMap &matrix){
  /*  printf("R = %d , C = %d , now_index = %d , max_index = %d , restMine = %d\n"
	 ,R,C,now_index,max_index,restMine);
  printmatrix(matrix);
  */
  if(restMine==0){
      return isValidMap(matrix,R,C);
  }
  for(int i = now_index ; i < max_index;i++){
    int r = i /C,c = i % C;
    matrix[r][c] = '*';
    bool flag = search(R ,C,i+1,max_index,restMine-1,matrix);
    if(flag)return true;
    matrix[r][c] = '.';
  } 
  return false;
}
void solve(int n){
  cout << "Case #" << n << ":" << endl;
  int R,C,M;
  cin>> R >> C >> M; 
  MineMap matrix(R,vector<char>(C,'.'));
  if(R*C - 1 == M){
    for(int i = 0 ; i <R ; i++){
      for(int j = 0 ; j < C; j++){
	cout << ((i+j) ==0 ? 'c':'*') ;
      }
      cout << endl;
    }
    return ;
  }
  if(search(R,C,0,R*C,M,matrix)){
    for(int i = 0 ; i < R ;i++){
      for(int j = 0; j < C ; j++){
	cout << matrix[i][j];
      }
      cout << endl;
    }
  }
  else {
    cout <<"Impossible"<<endl;
  }
  return ;
}
int main(){
  int T ;
  cin >> T;
  for(int i = 0 ; i < T ; i++){
    solve(i+1);
  }
}
