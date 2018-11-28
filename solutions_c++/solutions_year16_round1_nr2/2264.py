#include<bits/stdc++.h>
using namespace std;
int N;
int T;
vector<int> V[111];

int fie[55][55];
bool check( int x,int y, int id ){
  if( x == -1 )
    for(int i=0;i<N;i++)
      if( fie[i][y] != -1 && fie[i][y] != V[id][i] ) return false;
  if( y == -1 )
    for(int i=0;i<N;i++)
      if( fie[x][i] != -1 && fie[x][i] != V[id][i] ) return false;
  return true;
}
void ume( int x,int y, int id ){
  if( x == -1 )
    for(int i=0;i<N;i++)
      fie[i][y] = V[id][i];
  if( y == -1 )
    for(int i=0;i<N;i++)
      fie[x][i] = V[id][i];
}
bool solve(int id, int x,int y,int skx,int sky){
  if( skx != -1 && x == skx ) x++;
  if( sky != -1 && y == sky ) y++;
  if( x == N && y== N ) return true;
  if( x > N || y > N ) return false;
  int tmp[55][55]={};
  for(int i=0;i<N;i++)
    for(int j=0;j<N;j++)
      tmp[i][j] = fie[i][j];
  if( check( x, -1 , id ) ){
    ume( x, -1, id );
    if( solve(id+1,x+1,y,skx,sky) ) return true;
    for(int i=0;i<N;i++)
      for(int j=0;j<N;j++)
        fie[i][j] = tmp[i][j];
  }
  if( check( -1, y, id ) ){
    ume( -1, y, id );
    return solve(id+1,x,y+1,skx,sky);
  }
  return false;
}

int main(){
  cin >> T;
  for(int ttt=1;ttt<=T;ttt++){
    cin >> N;
    
    for(int i=0;i<2*N-1;i++){
      V[i].clear();
      for(int j=0;j<N;j++){
        int v; cin >> v;
        V[i].push_back( v );
      }
    }
    sort( V,V+2*N-1 );

    vector<int> res;
    for(int i=0;i<N;i++){
      memset(fie,-1,sizeof(fie));
      if( solve( 0, 0, 0, i, -1 ) ){
        for(int j=0;j<N;j++)
          res.push_back( fie[i][j] );
        break;
      }

      
    }
    if( res.empty() ){
      for(int i=0;i<N;i++){
        memset(fie,-1,sizeof(fie));
        if( solve( 0, 0, 0, -1, i ) ){
          for(int j=0;j<N;j++)
            res.push_back( fie[j][i] );
          break;
        }          
      }
    }
    

    cout << "Case #" << ttt << ":";
    for(int i=0;i<res.size();i++) cout << " "<< res[i];
    cout << endl;    
  }
}
