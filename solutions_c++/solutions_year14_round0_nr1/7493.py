#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <cstdlib>

using namespace std;

int arr1[4][4];
int arr2[4][4];

void readBoard(int n) 
{
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (n==1) cin >> arr1[i][j];
      else if (n==2) cin >> arr2[i][j];
    }
  }
}


vector<int> ini;
int check(int l1, int l2)
{
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (arr1[l1][i] == arr2[l2][j]) {
	ini.push_back(arr1[l1][i]);
      }
    }
  }

  if (ini.size() == 0) return 1;
  else if (ini.size() == 1) return 2;
  else if (ini.size() >= 2) return 3;
}

int main() {

  int num; int c = 1;
  cin >> num;
  while (num--) {
    int line1, line2;
    cin >> line1;
    readBoard(1);
    cin >> line2;
    readBoard(2);
    
    int cuantos = check(line1-1, line2-1);

    cout << "Case #" << c << ": ";
    if (cuantos == 2) cout << ini[0] << endl;
    else if (cuantos == 1) cout << "Volunteer cheated!" << endl;
    else cout << "Bad magician!" << endl;
    c++;
    ini.clear();
  }

  return 0;
}
