#include <iostream>
#include <set>
using std::cin;
using std::cout;
using std::endl;
using std::set;


int main ()
{
  int n;
  set<int> a, b;
  cin >> n;
  for ( int dg, d, cnt, num, tmp, j, i = 1 ; i <= n ; ++ i )
    {
      cin >> num;
      if ( num == 0 )
        {
          cout << "Case #" << i << ": INSOMNIA" << endl;
          continue;
        }
      a.insert(num);
      cnt = 0;
      j = 1;
      tmp = num;
      while (true)
        {
          dg = tmp;
          while ( dg != 0 )
            {
              d = dg % 10;
              // cout << d << " " << tmp << endl;
              if ( b.count(d) == 0 )
                {
                  b.insert(d);
                  cnt += 1;
                }
              dg = dg / 10;
            }
          if ( cnt == 10 )
            {
              cout << "Case #" << i << ": " << tmp << endl;
              break;
            }
          tmp = num * (++ j);
        }
      a.clear();
      b.clear();
    }
  return 0;
  
}
