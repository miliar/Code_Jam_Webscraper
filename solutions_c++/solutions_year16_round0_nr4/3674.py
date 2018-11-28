#include <iostream>

using namespace std;

void solve(int k)
{
  for(int i=1;i<=k;i++)
    {
      cout << i << " ";
    }  
  cout << "\n";
  return ;
}

int main()
{
  freopen("D-small-attempt0.in", "r", stdin);
  freopen ("myfilefor4.txt","w",stdout);
  int t,k,c,s;
  cin >> t;
  for(int i=0;i<t;i++)
    {
      cin >> k >> c >> s;
      printf("Case #%d: ", i+1);
      solve(k);
    }
  return 0;
}
