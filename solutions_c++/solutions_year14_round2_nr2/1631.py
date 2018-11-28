#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>


using namespace std;

int main(void){
  int T; 
  cin >> T;


  for(int cas = 1; cas <= T; cas++) {
    int a, b, k;

    cin >> a >> b >> k;

    int res = 0;

    for(int i = 0; i < a; i++) {
      for(int j = 0; j < b; j++) {
        if((i & j) < k) res++;
      }
    
    }

    cout << "Case #" << cas << ": " << res << endl;

  }

  return 0;
}





