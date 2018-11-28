#include <iostream>
#include <cmath>

using namespace std;

unsigned long long solve(long long ink, int r)
{
  unsigned long long ctr, rv;
  long long iv;
  
  iv  = ink;
  rv  = r;
  ctr = 0;

  while(1) {
    iv -= pow(rv + 1, 2) - pow(rv, 2);

    if(iv >= 0.0) {
      ctr++;
      rv += 2;

    } else {
      break;

    }
  }

  return ctr;
}

int main(void)
{
  unsigned long long t, r, n;

  cin >> n;

  for(int i = 0; i < n; i++) {
    cin >> r >> t;
    cout << "Case #" << i + 1 << ": " << solve(t, r) << endl;
  }

  return 0;
}
