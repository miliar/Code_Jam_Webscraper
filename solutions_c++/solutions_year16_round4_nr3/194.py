#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>

using namespace std;

int r, c, a, b;
int ppair[200];
char ans[100][100];

bool ok(int r, int c){
  for(int i = 1;i <= 2*(r+c);i++){
    int nowr, nowc, dir;
    if(i <= c){
      nowr = 0;
      nowc = i-1;
      dir = 2;
    }
    else if(i <= c + r){
      nowr = i-c-1;
      nowc = c-1;
      dir = 3;
    }
    else if(i <= c + r + c){
      nowc = c - (i-c-r);
      nowr = r-1;
      dir = 0;
    }
    else{
      nowc = 0;
      nowr = r-(i - c - r - c);
      dir = 1;
    }
    while(0 <= nowc && nowc < c && 0 <= nowr && nowr < r){
      if(ans[nowr][nowc] == '\\'){
	if(dir == 0){
	  dir = 3;
	  nowc--;
	}
	else if(dir == 1){
	  dir = 2;
	  nowr++;
	}
	else if(dir == 2){
	  dir = 1;
	  nowc++;
	}
	else if(dir == 3){
	  dir = 0;
	  nowr--;
	}
      }
      
      else if(ans[nowr][nowc] == '/'){
	if(dir == 2){
	  dir = 3;
	  nowc--;
	}
	else if(dir == 3){
	  dir = 2;
	  nowr++;
	}
	else if(dir == 0){
	  dir = 1;
	  nowc++;
	}
	else if(dir == 1){
	  dir = 0;
	  nowr--;
	}
      }
    }
    int fuga;
    if(nowr == -1)fuga = nowc+1;
    if(nowr == r)fuga = c + r + c - nowc;
    if(nowc == -1)fuga = c + r + c + r - nowr;
    if(nowc == c)fuga = c + 1 + nowr;
    if(fuga != ppair[i])return false;
  }return true;
}

void solve(){
  cout << endl;
  cin >> r >> c;
  for(int i = 0;i < (r+c);i++){
    cin >> a >> b;
    ppair[a] = b;
    ppair[b] = a;
  }
  for(int i = 0;i < (1 << (r*c));i++){
    for(int j = 0;j < r;j++){
      for(int k = 0;k < c;k++){
	int hoge = (i >> (j * c + k)) % 2;
	if(hoge)ans[j][k] = '\\';
	else ans[j][k] = '/';
      }
    }
    if(ok(r, c)){
      for(int i = 0;i < r;i++){
	for(int j = 0;j < c;j++){
	  cout << ans[i][j];
	}cout << endl;
      }
      return;
    }
  }
  cout << "IMPOSSIBLE" << endl;
  return;
}

int main(){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
