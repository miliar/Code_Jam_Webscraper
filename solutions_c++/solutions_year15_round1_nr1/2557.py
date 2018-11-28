#include <iostream>
using namespace std;
int main() {
  int t;
  cin >> t;
  int m[1000];
  for (int casecnt = 1; casecnt <= t; ++ casecnt) {
    cout << "Case #"<< casecnt << ": ";
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> m[i];
    }
    int y = 0;
    int maxrate = 0;
    for (int i = 1; i < n; ++i) {
      if (m[i]<m[i-1]) {
	y += (m[i-1]-m[i]);
      }
      if (m[i-1]-m[i]>maxrate){
	maxrate = m[i-1]-m[i];
      }
    }
    int z = 0;
    for (int i = 1; i < n; ++i) {
      if (m[i-1]<maxrate) {
	  z+=m[i-1];
      } else {
	z+=maxrate;
      }
    }
    cout << y <<" "<< z <<endl;
    
  }
}
