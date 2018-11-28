#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

void main2()
{
  int N; cin >> N;
  bool tab[10]; fill(tab, tab+10, false);
  
  if (N == 0)
  {
    cout << "INSOMNIA" << endl;
    return;
  }
  
  int nb = 10;
  ll act = N;
  for (int i=1; true; i++)
  {
    ll tmp = i * act;
    while (tmp > 0)
    {
      if (!tab[tmp % 10])
      {
        tab[tmp % 10] = true;
        nb--;
      }
      tmp /= 10;
    }
    if (nb == 0)
    {
      cout << act * i << endl;
      return;
    }
  }
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
