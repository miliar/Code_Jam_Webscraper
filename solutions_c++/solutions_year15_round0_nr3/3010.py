#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
#include <stdio.h>

using namespace std;

string s1 = "YES";
string s2 = "NO";
int m[5][5] = {0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
int a[1000000];

int turn (char x)
{
  if (x=='i')
    return 2;
  else if (x=='j')
    return 3;
  else if (x=='k')
    return 4;
}

void solve (int tmp)
{
  long long l, x;
  string s = "";
  string ss;

  cin >> l >> x;
  if (x > 32)
    x = x%32 + 32;
  cin >> ss;

  a[0] = turn (ss[0]);
  for (int i=1; i<=x; i++)
    s += ss;
   int len = x * l, pi=-1, pj=-1;
  for (int i=1; i<len; i++)
    a[i] = (a[i-1]/abs(a[i-1]))*m[abs(a[i-1])][turn(s[i])];

  if (a[len-1] != -1)
  {
    cout<<s2<<endl;
    return;
  }
  for (int i=0; i<len; i++)
    if (a[i] == 2)
    {
      pi = i;
      break;
    }

  for (int i=len-1; i>0; i--)
    if (a[i] == 4)
    {
      pj = i;
      break;
    }

  if (pi == -1 || pj == -1)
  {
      cout<<s2<<endl;
      return;
  }
  if (pi < pj) cout<<s1<<endl;
  else cout<<s2<<endl;
  return;

}

int main()
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios :: sync_with_stdio(false);
  int t;
  cin>>t;
  for (int i=1;i<=t;i++)
  {
    cout << "Case #" << i << ": ";
    solve(i);
  }
  return 0;
}
