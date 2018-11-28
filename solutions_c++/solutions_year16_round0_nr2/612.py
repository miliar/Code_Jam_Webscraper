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
  int res = 0;
  string s; cin >> s;
  for (int i=1; i<s.size(); i++)
    if (s[i] != s[i-1])
      res++;
  if (s.back() == '-')
    res++;
  cout << res << endl;
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
