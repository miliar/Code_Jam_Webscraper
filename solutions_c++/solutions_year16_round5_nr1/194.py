#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

char str[21000];
stack<char> s;

int main()
{
  int i;
  int t, T;
  scanf("%d", &T);

  for (t = 1; t <= T; t++)
  {
    while (!s.empty())
      s.pop();

    scanf(" %s", str);
    int len = strlen(str), ans = 0;

    for (i = 0; i < len; i++)
      if (!s.empty() && s.top() == str[i])
      {
        ans += 10;
        s.pop();
      }
      else
        s.push(str[i]);

    ans += (s.size() / 2) * 5;

    printf("Case #%d: %d\n", t, ans);
  }
  
  return 0;
}
