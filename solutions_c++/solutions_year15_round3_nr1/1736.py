#include <fstream>
#include <iostream>
#define DN 250005
using namespace std;

int main() {
  int t, r, c, w;
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for(int i = 0; i < t; ++i){
    cin >> r >> c >> w;
    if(w == 1)
      cout << "Case #" << i+1 << ": " << r * c << '\n';
    else
      cout << "Case #" << i+1 << ": " << r * ((c-1) / w) + w << '\n';
  }
  
  return 0;
}