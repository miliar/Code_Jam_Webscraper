#include <cstdlib>
#include <utility>
#include <cmath>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

typedef unsigned long long int ULL;
int map[100+2][100+2]; 
#define MAX 500

bool checkH(int x,int y){
  int k = map[y][x];

  for( int i=x-1; map[y][i]!=MAX; i-- ){
    if( map[y][i]>k )
      return false;
  }

  for( int i=x+1; map[y][i]!=MAX; i++ ){
    if( map[y][i]>k )
      return false;
  }

  return true;
}

bool checkV(int x,int y){
  int k = map[y][x];
  for( int i=y-1; map[i][x]!=MAX; i-- ){
    if( map[i][x]>k )
      return false;
  }

  for( int i=y+1; map[i][x]!=MAX; i++ ){
    if( map[i][x]>k )
      return false;
  }
  return true;
}

int main(){
  int t;
  cin>>t;
  for (int i = 1; i <= t; ++i){
    int a,b;
    cin>>a>>b;
    for (int j = 0; j < 100+2; ++j){
      for (int k = 0; k < 100+2; ++k){
	map[j][k] = MAX;
      }
    }

    for (int j = 1; j <= a; ++j){
      for (int k = 1; k <= b; ++k){
	cin>>map[j][k];
      }
    }

    bool ans=true;
    for (int j = 1; j <= a; ++j){
      for (int k = 1; k <= b; ++k){
	if( map[j][k]<100 && !checkV(k,j) && !checkH(k,j) ){
	  ans=false;
	  goto ANS;
	}
      }
    }    
  ANS:
    cout << "Case #" << i << ": "<< (ans?"YES":"NO") << endl;
  }
  return 0;
}
