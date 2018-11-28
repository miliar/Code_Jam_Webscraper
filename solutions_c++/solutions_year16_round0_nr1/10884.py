#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

int t, n;

inline int solve (int x)
{
  int cnt = 0, mark[10];
  memset(mark, 0, sizeof mark);
  for(int i = 1 ; i < 1000 ; i++)
    {
      int tmp = i * x;
      while(tmp > 0)
	{
	  cnt -= mark[tmp % 10];
	  mark[tmp % 10] = 1;
	  cnt += mark[tmp % 10];
	  tmp /= 10;
	}
      if(cnt == 10)
	return i * x;
    }
    return -1;
}

int main()
{
  cin >> t;
  for(int i = 0 ; i < t ; i++)
    {
      cin >> n ;
      int ans = solve(n);
      if(ans != -1)
	cout << "Case #" << i + 1 << ": " << ans << endl ;
      else	
	cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl ;
    }
}
