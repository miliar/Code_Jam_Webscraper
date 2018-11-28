#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int Z;
  cin >> Z;
  for (int z = 1; z <= Z; ++z) {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; ++i)
      cin >> p[i];
    int solution = *max_element(p.begin(), p.end());
    for (int k = 1; k <= solution; ++k) {
      int specials = 0;
      for (int x : p)
        specials += (x - 1) / k;
      solution = min(solution, specials + k);
    }
    cout << "Case #" << z << ": " << solution << endl;
  }
}
