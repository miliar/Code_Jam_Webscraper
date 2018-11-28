#include <iostream>
#include <cstring>

using namespace std;

int main(){
  int t, k=1;
  int A[4][4];
  int B[4][4];
  int f[17];
  int a, b;
  cin >> t;
  while(t--){
    cin >> a;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
        cin >> A[i][j];
    cin >> b;
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
        cin >> B[i][j];
    memset(f,0,sizeof(f));
    for(int i=0; i<4; i++)
      f[A[a-1][i]]++;
    for(int i=0; i<4; i++)
      f[B[b-1][i]]++;
    int r = 0;
    int ans;
    for(int i=1; i<=16; i++){
      if(f[i] == 2){
        ans = i;
        r += 1;
      }
    }
    cout << "Case #" << k++ << ": ";
    if(r == 1){
      cout << ans << endl;
    }
    else if(r >= 2)
      cout << "Bad magician!" << endl;
    else
      cout << "Volunteer cheated!" << endl;
  }
}
