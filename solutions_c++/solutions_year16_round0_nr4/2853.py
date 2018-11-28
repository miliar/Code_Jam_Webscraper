#include <iostream>
#include <cmath>

using namespace std;

long long N;

int main(){
  cin >> N;
  for(int i = 0; i < N; i++){
    cout << "Case #" << i+1 << ":";
    int K, C, S; cin >> K >> C >> S;
    for(int i = 0; i < K; i++){
      cout << " " << i+1;
    }
    cout << endl;
  }
  return 0;
}
      
