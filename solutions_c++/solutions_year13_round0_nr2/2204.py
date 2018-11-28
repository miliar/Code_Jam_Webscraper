#include <iostream>
using namespace std;

const int MAX_N = 130;
int A[MAX_N][MAX_N];
int max_r[MAX_N],max_c[MAX_N];

bool do_case(){
  int m,n;
  cin >> m >> n;
  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
      cin >> A[i][j];
  
  for(int i=0;i<m;i++){
    max_r[i] = A[i][0];
    for(int j=0;j<n;j++)
      max_r[i] = max(max_r[i],A[i][j]);
  }
  
  for(int j=0;j<n;j++){
    max_c[j] = A[0][j];
    for(int i=0;i<m;i++)
      max_c[j] = max(max_c[j],A[i][j]);
  }
  
  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
      if(A[i][j] != max_r[i] && A[i][j] != max_c[j])
        return false;
  return true;
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--)
    cout << "Case #" << C++ << ": " << (do_case() ? "YES" : "NO") << endl;
  return 0;
}
