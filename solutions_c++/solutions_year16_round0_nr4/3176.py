#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
int main()
{
  int t; cin >> t;
  for(int i = 0 ; i < t ; ++i)
    {
      ll k,c,s; cin >> k >> c >> s;
      ll mult=0,beg=1;
      for(int j = 0 ; j < c ; ++j)
	mult = mult * k + 1;
      cout << "Case #" << i+1 <<": ";
      for(int j = 0 ; j < s ; ++j)
	{
	  cout << beg << " ";
	  beg +=mult;
	}
      cout << "\n";
    }
}
