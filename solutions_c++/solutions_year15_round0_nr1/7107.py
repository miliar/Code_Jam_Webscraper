#include<cstring>
#include<iostream>
#include<string>
#define MAXN 1005
using namespace std;

int n, t;
int s[MAXN];
int f[MAXN];

int sol()
{
  int ans = 0;
  f[0] = s[0];
  for (int i = 1 ; i <= n ; ++ i )
    {
      if (f[i-1] < i)
        {
          ans += (i - f[i-1]);
          f[i] += (i - f[i-1]);
        }
      f[i] += f[i-1] + s[i];
    }
  return ans;
}

int main()
{
  int tot;
  cin>>t;
  tot = t;
  while (t--)
    {
      cin>>n;
      char c;
      memset(f, 0, sizeof(f));
      for (int i = 0; i <= n ; ++ i)
        {
          cin>>c;
          s[i] = int(c - '0');
        }
      cout<<"Case #" << (tot-t) << ": " << sol() << "\n";
    }
  return 0;
}
