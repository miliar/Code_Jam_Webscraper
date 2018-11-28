/*

*.  x
..

*.  ok

.
.
.
*   ok

..**
..**
...*
****

*/

#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int T,M,R,C;
const int MAX = 5;
bool res[MAX][MAX];
int flag[MAX][MAX];

int rec(int x,int y){
  if(flag[y][x] == 2 || res[y][x] == 1)return 0;
  int cnt = 1;
  if(flag[y][x] == 1){
    flag[y][x] = 2;
    return cnt;
  }
  flag[y][x] = 2;
  for(int i = -1 ; i < 2 ; i++){
    for(int j = -1 ; j < 2 ; j++){
      int nx,ny;
      nx = x + j;
      ny = y + i;
      if(0 <= ny && ny < R && 0 <= nx && nx < C){
	cnt += rec(nx,ny);
      }
    }
  }
  return cnt;
}

void display(){
  for(int i = 0 ; i < R ; i++){
    for(int j = 0 ; j < C ; j++){
      cout << res[i][j];
    }
    cout << endl;
  }
  cout<< endl;
}

bool check(){

  //display();

  for(int i = 0 ; i < R ; i++)
    for(int j = 0 ; j < C ; j++)
      flag[i][j] = 0;

  for(int i = 0 ; i < R ; i++){
    for(int j = 0 ; j < C ; j++){

      if(res[i][j]){
	for(int x = -1 ; x < 2 ; x++){
	  for(int y = -1 ; y < 2 ; y++){
	    if(!(0 <= i+y && i+y < R && 0 <= j+x && j+x < C))continue;
	      flag[i+y][j+x] = 1;
	  }
	}
      }
    }
  }
  int a = rec(0,0);
  return a == (R*C)-M;
}


void func(){
  cin >> R >> C >> M;
  for(int i = 0 ; i < (1 << R*C) ; i++){
    if(__builtin_popcount(i) != M)continue;

    int cnt = 0;
    for(int j = 0 ; j < R ; j++){
      for(int k = 0 ; k < C ; k++){
	res[j][k] = ((i >> cnt)&1);
	cnt++;
      }
    }

    if(check()){
      for(int j = 0 ; j < R ; j++){
	for(int k = 0 ; k < C ; k++){
	  if(j == 0 && k == 0)cout << 'c';
	  else cout << (res[j][k]?'*':'.');
	}
	cout << endl;
      }
      return;
    }
  }
  cout << "Impossible" << endl;
}

int main(){
  cin >> T;
  for(int i = 0 ; i < T ; i++){
    cout << "Case #" << i+1 << ":" << endl;
    func();
  }
  return 0;
}
