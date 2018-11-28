#include <iostream>
#include <string>
#include <vector>
using namespace std;

int flip(int* arr, int idx, int size) {
  for(int i = 0; i < size; i++) {
    arr[idx+i] *= -1;
  }
}

bool check(int* arr, int size) {
  for(int i = 0; i < size; i++) {
    if(arr[i] != 1)
      return false;
  }
  return true;
}

int cal(string s, int size) {
  int l = s.length();
  int pc_i[l];
  for(int i = 0; i < l; i++) {
    pc_i[i] = (s[i] == '+')? 1 : -1;
  }
  int ft = 0;
  for(int i = 0; i < (l-size+1); i++) {
    if(pc_i[i] != 1) {
      flip(pc_i, i, size);
      ft += 1;
    }
  }

  return (check(pc_i, l)? ft : -1);
}

int main() {
  int nc = -1;
  cin >> nc;
  string pc[nc];
  int fs[nc];
  for(int i = 0; i < nc; i++) {
    string ss;
    int ff;
    cin >> ss >> ff;
    pc[i] = ss;
    fs[i] = ff;
  }

  for(int i = 0; i < nc; i++) {
    int t = cal(pc[i], fs[i]);
    cout << "Case #" << (i+1) << ": "; 
    if(t < 0)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << t << endl;
  }

  return 0;
}
