#include <iostream>
using namespace std;

int N = 4;
int ar1[4][4];
int ar2[4][4];

int main() {
  int t;
  cin >> t;
  for(int zi = 1; zi <= t; zi++) {
    int r1, r2;
    cin >> r1;
    r1--;

    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
	cin >> ar1[i][j];
      }
    }
    cin >> r2;
    r2--;
    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
	cin >> ar2[i][j];
   
    int count = 0;
    int card = -1;
    for(int c = 0; c < N; c++) {
      bool intersects = false;
      for(int c2 = 0; c2 < N; c2++) {
	if(ar1[r1][c] == ar2[r2][c2]) {
	  intersects = true;
	  card = ar1[r1][c];
	  break;
	}
      }
      if(intersects) count++;
    }

    cout << "Case #" << zi << ": ";
    if(count == 0)
      cout << "Volunteer cheated!";
    else if (count == 1)
      cout << card;
    else
      cout << "Bad magician!";
    cout << endl;
  }
  return 0;
}
