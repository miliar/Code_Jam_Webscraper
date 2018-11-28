#include <bits/stdc++.h>
using namespace std;


string recortarBordes(string st)
{
  string nuevo;
  int l = 0, r = st.size()-1;
  for(l = 0 ; l < st.size() ; ++l)
    if(st[l] == '-')
      break;
  for(r = st.size()-1 ; r >= 0 ; --r)
    if(st[r] == '-')
      break;
  for(int i = l ; i <= r ; ++i)
    nuevo += st[i];
  return nuevo;
}

string flip(string st, int k)
{
  for(int i = 0;i < k ; ++i)
    if(st[i] == '-')
      st[i] = '+';
    else
      st[i] = '-';
  return st;
}

int main(int argc, char *argv[])
{
  int t,k; cin >> t;
  string st;
  for(int i = 0 ;i < t ; ++i)
    {
      cin >> st >> k;
      int cnt=0;
      st = recortarBordes(st);
      while(st.size() >= k)
        {
          // cout << st << "\n";
          st = recortarBordes(st);
          st = flip(st,k);
          st = recortarBordes(st);
          ++cnt;
        }
      cout << "Case #" << i+1 << ": ";
      if(st.empty())
        cout << cnt << "\n";
      else
        cout << "IMPOSSIBLE\n";
    }
  return 0;
}
