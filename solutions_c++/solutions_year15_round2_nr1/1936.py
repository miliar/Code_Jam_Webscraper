#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

typedef long long ll;

ll min(ll a, ll b)
{
  return (a < b ? a : b);
}

ll reverse(ll n)
{
  ll r = 0;
  int d;
  while(n > 0)
    {
      d = n % 10;
      r = r * 10 + d;
      n /= 10;
    }
  return r;  
}

ll tab[1000001];

ll f(ll x, ll y)
{  
  if(tab[x] != -1)
    return tab[x];
  //cout << "x = " << x << "\ty = " << y << endl;
  if(x == y)
    return 1;  
  ll r = reverse(x);
  //cout << "rev(x) = " << r << endl;
  if(x > y && r > y)
    return y+1;
    
  if(r != x && r > x)
    tab[x] = 1 + min(f(x+1, y), f(r, y));
  else
    tab[x] = 1 + f(x+1, y);    
  return tab[x];  
}

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	
	int t;
	fin >> t;
	//cin >> t;
	for(int tnum = 1; tnum <= t; ++tnum)
		{
		  for(int i = 0; i <= 1000000; ++i)
		    tab[i] = -1;
		  ll n;
		  //cin >> n;
		  fin >> n;
		  ll ans = f(1,n);    
			fout << "Case #" << tnum << ": " << ans << endl;
			//cout << ans << endl;
		}
	return 0;
}
