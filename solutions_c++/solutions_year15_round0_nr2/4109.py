#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

int minutes(vector<int> plates)
{
  sort(plates.begin(), plates.end());
  
  int max = plates.back();
  plates.pop_back();

  if (max <= 3)
    return max;

  int total = max;
  int spec = 1;
  while (max / (spec + 1) > 3)
    spec++;
  for (int i = 1; i <= spec; ++i) {
    vector<int> spec_plates(plates);
    int rest = max % (i + 1);
    int base = max / (i + 1);
    for (int j = 0; j <= i; j++) {
      if (rest > 0) {
        spec_plates.push_back(base + 1);
        rest--;
      }
      else
        spec_plates.push_back(base);
    }
    total = min(total, minutes(spec_plates) + i);
  }
  return total;
}

int main()
{
  int N;
  cin >> N;
  getchar();

  for (int n = 0; n < N; ++n)
  {
    int D;
    cin >> D;

    vector<int> plates(D);

    for (int i = 0; i < D; i++)
      cin >> plates[i];

    sort(plates.begin(), plates.end());
    //for (int p : plates)
    //  cout << p << ' ';
    //cout << endl;
    cout << "Case #" << n + 1 << ": " << minutes(plates);
    cout << endl;
  }
  return 0;
}