#include <iostream>
#include <cstring>
using namespace std;

#define SZ 4
#define BAD_MAGICIAN -1
#define BAD_VOLUNTEER -2

int magic(int a1[][SZ], int a2[][SZ], int r1, int r2){
  bool mark1[SZ * SZ] = { 0 };
  bool mark2[SZ * SZ] = { 0 };
  for (int i = 0; i < SZ; ++i){
    mark1[a1[r1-1][i]-1] = true;
    mark2[a2[r2-1][i]-1] = true;
  }
  int ret = -1;
  for (int i = 0; i < SZ * SZ; ++i)
    if (mark1[i] && mark2[i]){
      if (ret == -1)
        ret = i+1;
      else
        return BAD_MAGICIAN;
    }
  if (ret != -1) return ret;
  else           return BAD_VOLUNTEER;
}

int main(){
  int n; cin >> n;
  for (int i = 1; i <= n; ++i){
    int row1, row2;
    int a1[SZ][SZ];
    int a2[SZ][SZ];
    cin >> row1;
    for (int j = 0; j < SZ; ++j)
      for (int k = 0; k < SZ; ++k)
        cin >> a1[j][k];
    cin >> row2;
    for (int j = 0; j < SZ; ++j)
      for (int k = 0; k < SZ; ++k)
        cin >> a2[j][k];

    int num = magic(a1, a2, row1, row2);

    cout << "Case #" << i << ": ";
    if (num == BAD_MAGICIAN)
      cout << "Bad magician!";
    else if (num == BAD_VOLUNTEER)
      cout << "Volunteer cheated!";
    else
      cout << num;
    cout << endl;
  }
}
