#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

int T;
int n, ans;
string st;

void work()
{
  int pan;
  if (st[0] == '+')
    pan = 1;
  else
    pan = 0;
  for (int i = 1; i < n; i++) {
    int t;
    if (st[i] == '+')
      t = 1;
    else
      t = 0;
    if (pan != t) {
      ans++;
      pan = t;
    }
  }
  if (!pan)
    ans++;
}

int main()
{
  freopen("B-large.in.txt", "r", stdin);
  freopen("data.out", "w", stdout);
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    ans = 0;
    cin >> st;
    n = st.length();
    work();
    cout << ans << endl;
  }
}
