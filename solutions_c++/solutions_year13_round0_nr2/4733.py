#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

bool sol(vector< vector<int> > &table){
  int h = table.size();
  int w = table[0].size();
  for(int y=0; y<h; y++){
    for(int x=0; x<w; x++){
      int num = table[y][x];
      bool flg = false;

      for(int i=0; i<h; i++){
	if( table[i][x] > num ){ break; }
	if( i == h-1 )flg = true;
      }
      for(int i=0; i<w; i++){

	if( table[y][i] > num ){ break; }
	if( i == w-1 )flg = true;
      }
      if( !flg ) return false;
    }
  }
  return true;
}


int main(){
  int T;
  cin >> T;
  for( int t_case = 1; t_case <= T; t_case++ ){
    int n,m;
    cin >> n >> m;
    vector< vector<int> > table(n,vector<int>(m,0));
    for(int y=0; y<n; y++) for(int x=0; x<m; x++){ cin >> table[y][x]; }
    printf("Case #%d: ",t_case);
    if( sol(table) ){
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
  return 0;
}
