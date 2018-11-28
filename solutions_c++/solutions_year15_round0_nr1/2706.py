#include <iostream>
#include <vector>

using namespace std;

int N;
int SMax;
char c;
int val;
int sumSoFar;
int missing;

int main() {
  ios_base::sync_with_stdio(0);

  cin >> N;

  for (int i=0; i<N; ++i)
  {
    sumSoFar = 0;
    missing = 0;
    cin >> SMax;
    for (int j=0; j<=SMax; ++j)
    {
      if (sumSoFar < j)
      {
        missing += j - sumSoFar;
        sumSoFar = j;
      }
      cin >> c;
      val = c - '0';
      sumSoFar += val;
    }
    cout << "Case #" << (i+1) << ": " << missing << '\n';
  }

  return 0;
}
