#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()  {
  
  int t, ans1, ans2, val, i;
  vector <int> v, uniq;
  
  cin >> t;
  for (int j = 1; j <= t; ++j) {
    cin >> ans1;
    ans1--;
    for (i = 0; i < 16; ++i) {
      cin >> val;
      if (i / 4 == ans1)  {
        v.push_back(val);
      }
    }
    cin >> ans2;
    ans2--;
    for (i = 0; i < 16; ++i) {
      cin >> val;
      if (i / 4 == ans2)  {
        v.push_back(val);
      }
    }
    sort(v.begin(), v.end());
    
    for (i = 0; i < (int)v.size();)  {
      if (v[i] != v[i + 1]) {
        ++i;
      }
      else
      {
        int x = v[i];
        while (v[i] == x && i < (int)v.size()) {
          ++i;
        }
        uniq.push_back( x );
      }
    }
    
    cout << "Case #" << j << ": ";
    if (uniq.size() == 1) {
      cout << uniq[0] << "\n";
    }
    else if (uniq.size() > 1) {
      cout << "Bad magician!\n";
    }
    else  {
      cout << "Volunteer cheated!\n";
    }
    
    uniq.clear();
    v.clear();
  }
  
  return 0;
}
