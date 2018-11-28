#include <iostream>
#include <string.h>
using namespace std;

int f[4][4];
int s[4][4];

int main(){
  int N, i, j, k, m, n;
  cin >> N;
  for ( i = 0; i < N; i++) {
    memset(f, 0, sizeof(f));
    memset(s, 0, sizeof(s));
    int first, second;

    cin >> first;
    for (j = 0; j < 4; j++) {
      for (k = 0; k < 4; k++) {
        cin >> f[j][k];
      }
    }
    cin >> second;
    for (j = 0; j < 4; j++) {
      for (k = 0; k < 4; k++) {
        cin >> s[j][k];
      }
    }
    

    int same = 0;
    int result = -1;
   
    for (j = 0; j < 4; j++) {
      for (k = 0; k < 4; k++) {
        if (f[first-1][j] == s[second-1][k]) {
          same++;
          result = f[first-1][j];
          break;
        }
      }
    } 

    if (same == 0) {
      cout << "Case #" << (i+1) << ": " << "Volunteer cheated!\n";
    } else if (same == 1) {
      cout << "Case #" << (i+1) << ": " << result << "\n";
    } else {
      cout << "Case #" << (i+1) << ": " << "Bad magician!\n";
    } 
    
  }
  return 0;
}
