#include <iostream>
#include <string>

using namespace std;

string gen(char c, int size)
{
  if (size == 1)
    return string(1, c);
  
  int ns = size/2;
  
  string s1, s2;
  
  switch (c)
  {
    case 'R': s1 = gen('R', ns); s2 = gen('S', ns); break;
    case 'S': s1 = gen('S', ns); s2 = gen('P', ns); break;
    case 'P': s1 = gen('P', ns); s2 = gen('R', ns); break;
  }
  
  if (s1 < s2)
    return s1 + s2;
  else
    return s2 + s1;
}

int N, R, P, S;

bool solve(char c, int size)
{
  string res = gen(c, size);
  int r, s, p;
  r = s = p = 0;
  
  for (int i = 0; i < res.length(); i++)
  {
    switch (res[i])
    {
      case 'R': r++; break;
      case 'S': s++; break;
      case 'P': p++; break;
    }
  }
  
  if (r == R && s == S && p == P)
  {
    cout << res;
    return true;
  }
  else
    return false;
}

int main()
{
  int t;
  cin >> t;
  
  for (int i = 1; i <= t; i++)
  {
    cin >> N >> R >> P >> S;
    
    cout << "Case #" << i << ": ";

    int size = 1 << N;
    bool sr = solve('R', size);
    bool sp = solve('P', size);
    bool ss = solve('S', size);
    
    if (!sr && !sp && !ss)
      cout << "IMPOSSIBLE";
    
    cout << endl;
  }
  
  return 0;
}
