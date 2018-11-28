#include <iostream>

using namespace std;


int main(void){
  int n, n0, row, col;
  int niwa[100][100] = {{0}};
  bool table[100][100] = {{false}};

  cin >> n;
  n0 = n;
  
  while(n--){
    int min = 100;
    bool flg = true;
    cin >> row >> col;
    for(int i = 0; i < row; ++i){
      for(int j = 0; j < col; ++j){
	cin >> niwa[i][j];
      if(niwa[i][j] < min)
	min = niwa[i][j];
      }
    }
    for(int i = 0; i < row; ++i){
      for(int j = 0; j < col; ++j)
	table[i][j] = (niwa[i][j] == min);
    }
    
    for(int i = 0; i < row; ++i){
      for(int j = 0; j < col; ++j){
	
	if(table[i][j]){
	  bool fr = true, fc = true;
	  for(int k = 0; k < row; ++k)
	    fr = table[k][j] && fr;
	  for(int l = 0; l < col; ++l)
	    fc = table[i][l] && fc;
	  flg = (fr || fc) && flg;
	}

      }
    }
    cout << "Case #" << n0 - n << ": ";
    if(!flg)
      cout << "NO";
    else
      cout << "YES";
    cout << endl;
  }
}
