#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

string gen(int n, int cur)
{
  if (n == 0)
  {
    if (cur == 0)
      return "P";
    else if (cur == 1)
      return "R";
    else
      return "S";
  }

  string a1, a2;

  if (cur == 0)
  {
    a1 = gen(n - 1, 0);
    a2 = gen(n - 1, 1);
  }
  else if (cur == 1)
  {
    a1 = gen(n - 1, 1);
    a2 = gen(n - 1, 2);
  }
  else
  {
    a1 = gen(n - 1, 0);
    a2 = gen(n - 1, 2);
  }

  if (a1 < a2)
    return a1 + a2;
  return a2 + a1;
}

string verify(string str, int r, int p, int s)
{
  int cr = 0, cp = 0, cs = 0, i;

  for (i = 0; i < (int)str.length(); i++)
    if (str[i] == 'R')
      cr++;
    else if (str[i] == 'P')
      cp++;
    else
      cs++;

  if (cr == r && cp == p && cs == s)
    return str;
  return "Z";
}

int main()
{
  int t, T;
  scanf("%d", &T);

  for (t = 1; t <= T; t++)
  { 
    int n, r, p, s;
    scanf("%d %d %d %d", &n, &r, &p, &s);

    string a0 = verify(gen(n, 0), r, p, s);
    string a1 = verify(gen(n, 1), r, p, s);
    string a2 = verify(gen(n, 2), r, p, s);

//    printf("%s\n%s\n%s\n", gen(n, 0).c_str(), gen(n, 1).c_str(), gen(n, 2).c_str());

    string final = min(a0, min(a1, a2));
    if (final == "Z")
      final = "IMPOSSIBLE";
    
    printf("Case #%d: %s\n", t, final.c_str());
  }
  
  return 0;
}
