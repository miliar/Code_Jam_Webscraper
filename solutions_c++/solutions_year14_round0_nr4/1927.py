#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

double a[1000], b[1000];

void solve(int test) {
  int i, j;
  int n;

  cin >> n;
  for(i=0; i<n; i++) cin >> a[i];
  for(i=0; i<n; i++) cin >> b[i];
  
  sort(a, a+n);
  sort(b, b+n);
  
  /*
  cout << fixed;
  cout << setprecision(3);
  for(i=0; i<n; i++) cout << a[i] << " ";
  cout << endl;
  for(i=0; i<n; i++) cout << b[i] << " ";
  cout << endl;
  */
  
  int y = 0;
  int z = 0;

  // War
  i=0; j=0;
  while(j < n) {
    if(a[i] < b[j]) {
      z++;
      i++;
      j++;
    } else {
      j++;
    }
  }
  z = n - z;

  // Deceitful War
  i=0; j=0;
  while(i < n) {
    if(a[i] > b[j]) {
      y++;
      i++;
      j++;
    } else {
      i++;
    }
  }

  cout << "Case #" << (test+1) << ": " << y << " " << z << endl;
}


int main() {
  int t, T;
  cin >> T;
  for(t=0; t<T; t++) solve(t);
  return 0;
}
