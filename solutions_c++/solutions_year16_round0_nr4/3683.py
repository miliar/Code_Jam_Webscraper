#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

void tick()
{
  unsigned long K, C;
  cin >> K;
  cin >> C;

  unsigned long S; cin >> S;

  if (S < K)  {cout << "IMPOSSIBLE" << endl; return;}

  for (unsigned long i=0; i < K; i++)
  {
    cout << 1 + (unsigned long)(pow(K,C-1))*i << ' ';
  }
  cout << endl;
}

int main()
{
  int bigN;
  cin >> bigN;
  for (int i=0; i < bigN; i++)
  {
    cout << "Case #" << (i+1) << ": ";
    tick();
  }
  return 0;
}
