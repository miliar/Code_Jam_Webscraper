#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stack>
#include <string.h>
#include <climits>
#include <limits>

#include<gmp.h>

using namespace std;

typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;

#define FOR(i, a, b) for(int i=a; i<b; i++)
#define FORE(i, a, b) for(int i=a; i<=b; i++)
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define ceil(a, b) ((a)/(b) + ((a)%(b)!=0))
#define square(a) ((a)*(a))
#define PI 3.14159265359
#define INF 1000000000000LL;
#define mod 1000000009LL

string tobin(int k)
{
  string r = "";
  while(k != 0)
  {
    r.insert(0, 1, (k % 2 == 0 ? '0' : '1'));
    k/=2;
  }

  return r;
}

int main(int argc, char **argv) {
  
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);


  ll t, n, j;
  cin >> t >> n >> j;
  cout << "Case #1:\n";

  ll smallest = 1 << (n - 2);
  ll largest = (1 << n - 1) - 1;

//  cout << tobin(smallest) << "  " << tobin(largest) << "\n";

  FORE(i, smallest, largest)
  {
    if (j == 0) return 0;
    string data = tobin(i) + '1';
    bool f = true;

fflush(stdout);
    stringstream ss;
    ss << data << " ";
    FORE(q, 2, 10)
    {
      mpz_t a;
      mpz_inits(a,NULL);
  
      mpz_set_str(a, data.c_str(), q);
      bool f2 = false;

//       cout << "a: " << mpz_get_str(NULL, 10, a) << "\n";
       fflush(stdout);
      for (ll m_i = 2; m_i<10000; m_i++)    
      {
//        cout << "m_i: " << mpz_get_str(NULL, 10, m_i) << "\n";
         if (mpz_divisible_ui_p(a, m_i))
        {
           f2 = true;
           ss << m_i << " ";
           break;
        }
      }
      if (!f2)
      {
        f = false;
        break;
      }  

    }

    if (f)
    {
       cout << ss.str() << "\n";
       j--;
    }
  }



}
