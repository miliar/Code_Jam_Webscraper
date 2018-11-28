#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int tc = 1 ; tc <= T ; tc++){
    cout << "Case #" << tc << ": ";
    
    int A, B, K;
    cin >> A >> B >> K;
    int ans = 0;
    for(int i = 0 ; i < A ; i++){
      for(int j = 0 ; j < B ; j++){
	int C = i & j;
	if(C < K) ans++;
      }
    }
    cout << ans << endl;
  }    
  return 0;
}
