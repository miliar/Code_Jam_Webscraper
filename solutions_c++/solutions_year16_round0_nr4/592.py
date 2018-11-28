#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

ll power(ll a, int b)
{
  if (b == 0) return 1;
  if (b % 2) return a * power(a, b-1);
  ll res = power(a, b/2);
  return res * res;
}

void main2()
{
  int K, C, S;
  cin >> K >> C >> S;
  if (S * C < K)
  {
    cout << " IMPOSSIBLE" << endl;
    return;
  }
  ll act = 0;
  while (act < K)
  {
    ll res = 0;
    for (int i=0; i<C; i++)
    {
      if (act < K)
        res += act * power(K, i);
      act++;
    }
    cout << " " << 1+res;
  }
  cout << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ":";
    main2();
  }
}
