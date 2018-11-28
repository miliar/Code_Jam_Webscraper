#include <iostream>
#include <iomanip>
using namespace std;

void solve(int test) {
  double c, f, x;
  cin >> c >> f >> x;
  
  double res = 0.0;
  double oldfreq = 2.0;
  double newfreq = 2.0;
  
  do {
    oldfreq = newfreq;
    res += c/oldfreq;
    newfreq = oldfreq + f;
  } while((x-c)/oldfreq > x/newfreq);

  res += (x-c)/oldfreq;

  cout << "Case #" << (test+1) << ": " << res << endl;
}

int main() {
  int i, T;
  cin >> T;
  
  cout << fixed;
  cout << setprecision(7);
  
  for(i=0; i<T; i++)
    solve(i);
  return 0;
}
