#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
  int tcs, r1, r2, result, count;
  int c1[5][5], c2[5][5];

  cin >> tcs;
  for(int cs = 1; cs <= tcs; ++cs){
    cin >> r1;
    for(int i = 1; i < 5; ++i)
      for(int j = 1; j < 5; ++j)
	cin >> c1[i][j];
    
    cin >> r2;
    for(int i = 1; i < 5; ++i)
      for(int j = 1; j < 5; ++j)
	cin >> c2[i][j];

    count = 0;
    for(int i = 1; i < 5; ++i){
      for(int j = 1; j < 5; ++j){
	if(c1[r1][i] == c2[r2][j]){
	  ++count;
	  result = c1[r1][i];
	}
      }
    }

    cout << "Case #" << cs << ": ";
    if(count == 1){
      cout << result;
    } else if(count == 0){
      cout << "Volunteer cheated!";
    } else {
      cout << "Bad magician!";
    }
    cout << endl;
  }

  return 0;
}
