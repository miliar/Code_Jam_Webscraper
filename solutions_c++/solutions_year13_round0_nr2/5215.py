#include <iostream>
#include <string>
#include <string.h>

using namespace std;

int main(int argc, char const *argv[])
{
  int count;
  cin >> count;
  for(int i = 0;i < count;i++) {
    int n,m;
    int square[101][101] = {0};
    cin >> n >> m;
    for(int j = 0;j < n;j++) {
      for(int k = 0;k < m;k++) {
        cin >> square[j][k];
      }
    }
    int flag = 1;
    int hhigh[101] = {0}; 
    int vhigh[101] = {0};
    for(int j = 0;j < n;j++) {
      for(int k = 0;k < m;k++) {
        if(square[j][k] > hhigh[k]){
          hhigh[k] = square[j][k];
        }
        if(square[j][k] > vhigh[j]) {
          vhigh[j] = square[j][k];
        }
      }
    }
    for(int j = 0;j < n && flag == 1;j++) {
      for(int k = 0;k < m && flag == 1;k++) {
        if((square[j][k] < hhigh[k]) && (square[j][k] < vhigh[j])) {
          flag = 0;
        }
      }
    }
    if(flag) {
      cout <<"Case #" <<i+1 <<": YES";
    }
    else {
      cout <<"Case #" <<i+1 <<": NO";
    }
    if(i+1 != count) {
      cout <<endl;
    }
  }
  return 0;
}