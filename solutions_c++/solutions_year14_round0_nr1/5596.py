#include <iostream>
#include <cstring>

using namespace std;

void solve(int test){
  cout << "Case #" << test << ": ";
  
  int row;
  int a[16][16];
  int used[17];
  memset(used, 0, sizeof(used));
  
  for(int q = 0; q < 2; ++q){
    cin >> row;
    
    for(int i = 0; i < 4; ++i)
      for(int j = 0; j < 4; ++j){
	cin >> a[i][j];
	if(i == row - 1	)
	  ++used[a[i][j]];
      }
  }
  
  int brr = 0, rem = 0;
  
  for(int i = 1; i <= 16; ++i)
    if(used[i] == 2){
      brr++;
      rem = i;
    }
    
  if(!brr){
    cout << "Volunteer cheated!\n";
    return;
  }
  if(brr > 1){
    cout << "Bad magician!\n";
    return;
  }
  
  cout << rem << endl;
  
}
int main(){
  int tests;
  cin >> tests;
  
  for(int i = 1; i <= tests; ++i){
    solve(i);
  }
}