#include <iostream>
#include <string>

using namespace std;

void solve(int t) {
  long a, b, k; cin >> a >> b >> k;
  
  long total = 0;
  
  for (int i = 0; i < a; i++) {
    for (int j = 0; j < b; j++) {
      if (k > (i&j)) total++;
    }
  } 
  
  cout << "Case #"<< t << ": " << total << endl;
}

int main() {
  int tc; cin >> tc;
  
  for (int i = 1; i <= tc; i++) solve(i);

  return 0;
}
