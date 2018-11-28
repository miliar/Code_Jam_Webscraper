#include <bits/stdc++.h>
using namespace std;
#define MAXN 10
typedef long long ll;
set<int> a;
ll n;



int main()
{
  int t; cin >> t;
  for(int i = 0 ; i < t ; ++i)
    {
      cin >> n;
      if(n == 0)
	{
	  cout << "Case #" << i+1 <<": INSOMNIA" << "\n";
	  continue;
	}
      ll cnt = 1;
      a.clear();
      ll dame  = n;
      while(a.size() < 10)
      	{
      	  ll aux = dame;
      	  while(aux > 0)
      	    {
      	      ll view  = aux % 10;
      	      a.insert(view);
	      aux /= 10;
      	    }
	  dame  = cnt * n;
	  cnt++;
      	}
      cout << "Case #" << i+1 << ": " << dame-n << "\n";
    }
  return 0;
}
