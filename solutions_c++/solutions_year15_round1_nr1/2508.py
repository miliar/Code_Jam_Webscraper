#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int t, n, m, caseN = 1;
  cin >> t;
  while (t--) {
    cout << "Case #" << caseN++ << ": ";
    cin >> n;
    vector<int> plate(n);
    for (int i = 0; i < n; i++)
      cin >> plate[i];

    int current = plate[0], eaten = 0;
    for (int i = 1; i < n; i++) {
      if (plate[i] < current)
	eaten += current - plate[i];
      current = plate[i];
    }
    cout << eaten << " ";

 
    int rate = 0;
    for (int i = 0; i < n-1; i++) {
      if (plate[i] - plate[i+1] > 0) {
	rate = max(rate, plate[i] - plate[i+1]);
      }
    }	
    

    eaten = 0;
    for (int i = 0; i < n-1; i++) {
      if (plate[i] - plate[i+1] < 0) {
	eaten += min(plate[i], rate);
      } else {
	eaten += min(plate[i], rate);
      }
    }
    cout << eaten << endl;
  }
  return 0;
}
