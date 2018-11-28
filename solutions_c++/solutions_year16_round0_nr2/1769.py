
#include <iostream>
using namespace std;

string s;

void solve()
{
  int n;
  scanf("%d", &n);
  cin >> s;
  s += "+";

  int i, cnt = 0;
  for(i = 0; i < s.size() - 1; i ++)
  {
    cnt += s[i] == '-' && s[i+1] == '+';
  }

  printf("%d\n", cnt * 2 - (s[0] == '-'));
}
int main()
{
  // long long mx = 0;
  // for(int i = 0; i <= 1000000 ; i ++)
  // {
  //   mx = max(mx, (long long) solve(i) * i);
  // }
  // cout << mx << endl;
  // return 0;
  int t;
  scanf("%d", &t);

  for(int i = 1; i <= t; i++)
  {
    printf("Case #%d: ", i);
    solve();
  }

}
