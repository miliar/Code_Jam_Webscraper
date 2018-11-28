#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>

using namespace std;

int main() {
  int cases;
  int number=1;
  cin >> cases;
while(cases--){ 
  int matrix_size_x, matrix_size_y;
  cin >> matrix_size_x >> matrix_size_y;
  int manip[matrix_size_x][matrix_size_y];
  for (int i=0;i<matrix_size_x;i++){
    for (int k=0;k<matrix_size_y;k++){
      cin >> manip[i][k];
    }
  }
//   for (int i=0;i<matrix_size_x;i++){
//     for (int k=0;k<matrix_size_y;k++){
//       cout << manip[i][k] << " ";
//     }
//     cout<< endl;
//   }

  bool no_clear_vision=false;
  
  for (int i=0;i<matrix_size_x;i++){
    
    for (int k=0;k<matrix_size_y;k++){
      
      bool rowclearvision=true;
      
      for (int j=0;j<matrix_size_y;j++){
	if (!(manip[i][k]>=manip[i][j])) rowclearvision=false;
      }
      
      bool colclearvision=true;
      
      for (int j=0;j<matrix_size_x;j++){
	if (!(manip[i][k]>=manip[j][k])) colclearvision=false;
      }
      
      if (rowclearvision==false && colclearvision==false){
	no_clear_vision=true;
	break;
      }
      
    }
    
    if (no_clear_vision) break;
    
  }
  
  string count;
  if (no_clear_vision){
    count="NO";
  } else {
    count="YES";
  }
  cout<< "Case #" << number <<": "<< count << endl;
  number++; 
}
  return 0;
}
