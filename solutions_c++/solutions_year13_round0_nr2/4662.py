#include<iostream>
#include<vector>
using namespace std;

const int LIM = 101;
int in[LIM][LIM];

int rowUpdate(int r,int c,int height){
  for(int i=0;i<r;i++){
    int all = 0;
    for(int j=0;j<c;j++){
      if (in[i][j] == -1)all++;
      if (in[i][j] == -1 || in[i][j] == height);
      else goto end;
    }
    if (all == c)continue;// already cut...
    for(int j=0;j<c;j++){
      in[i][j] = -1;
    }
    return i;// i-th row become *
  end:;
  }
  return -1;
}

int colUpdate(int r,int c,int height){
  for(int j=0;j<c;j++){
    int all = 0;
    for(int i=0;i<r;i++){
      if (in[i][j] == -1)all++;
      if (in[i][j] == -1 || in[i][j] == height);
      else goto end;
    }
    if (all == r)continue;//already cut...
    for(int i=0;i<r;i++){
      in[i][j] = -1;
    }
    return j;
  end:;
  }
  return -1;
}

bool solve(int r,int c){
  for(int h=1;h <= 100;h++){
    while(true){
      if (rowUpdate(r,c,h) != -1)continue;
      else if (colUpdate(r,c,h) != -1)continue;
      else break;
    }
  }
  for(int i=0;i < r;i++){
    for(int j=0;j < c;j++){
      if (in[i][j] != -1)return false;
    }
  }
  return true;
}

int main(){
  int te,tc = 1;
  cin>>te;
  while(te--){
    int n,m;    
    cin>>n>>m;
    for(int i=0;i < n;i++){
      for(int j=0;j < m;j++){
	cin>>in[i][j];
      }
    }
    cout << "Case #" << tc++ << ": ";
    if (solve(n,m)) cout << "YES" << endl;
    else cout <<"NO"<<endl;
  }
  return 0;
}
