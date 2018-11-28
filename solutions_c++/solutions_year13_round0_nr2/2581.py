#include <iostream>
using namespace std;

int m, n;
int lawn[100][100];
int g[100][100];

void printlawn(){
  for (int i = 0; i < n; ++i){
    for (int j = 0; j < m; ++j)
      cout << lawn[i][j];
    cout<<endl;
  }
}

bool isPossible(){
  if (n == 1 || m == 1) return true;
  for (int i = 0; i < n; ++i){
    int high = 0;
    for (int j = 0; j < m; ++j)
      if (lawn[i][j] > high) 
        high = lawn[i][j];
    for (int j = 0; j < m; ++j)
      g[i][j] = high;
  }
  for (int i = 0; i < m; ++i){
    int high = 0;
    for (int j = 0; j < n; ++j) 
      if (lawn[j][i] > high)
        high = lawn[j][i];
    for (int j = 0; j < n; ++j)
      if (g[j][i] > high)
        g[j][i] = high;
  }
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      if (g[i][j] != lawn[i][j])
        return false;
  return true;
}

int main(){
  int a; cin>>a;
  for (int i = 1; i <= a; ++i){
    cin>>n>>m;
    for (int j = 0; j < n; ++j)
      for (int k = 0; k < m; ++k)
        cin>>lawn[j][k];
    cout << "Case #" << i << ": ";
    if (isPossible())
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}
