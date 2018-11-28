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

string flip(string s, ll n)
{
  string r = s;
  FOR(i, 0, n) r[i] = s[n - i - 1] == '+' ? '-' : '+';
  return r;
}

bool won(string s) 
{
FOR(i, 0, s.size()) if (s[i] == '-') return false;

return true;
}

ll minusebi(string s)
{
  ll r = 0;
  FOR(i, 0, s.size()) if (s[i] == '-') r++;
                      else return r;

  return r;
}

ll plusebi(string s)
{
  ll r = 0;
  for(ll i = s.size() - 1; i>=0; i--) if (s[i] == '+') r++;
                      else return r;

  return r;
}
ll f(string s, ll t)
{    
 if (won(s))
 {
   return t;
 }

// cout << "f(" << s << ")";

 if (s[0] == '-')
 {
//   cout << "-\n";
   //vatrialebt bolo minusamde;
   ll index = 0;
   FOR(i, 0, s.size()) if (s[i] == '-') index = i;
   return f(flip(s, index + 1), t + 1);
 }
 else
 {
//   cout << "+\n";
   
   //vsvavt win bevr minuss
   ll mins = -1;
   string tmp;

   ll pl = plusebi(s);
 
   FORE(i, 0, s.size() - pl) 
   {
     string tmp2 = flip(s, i);
     if (tmp2 == s) continue;
     if(won(tmp2)) return t + 1;  

//     cout << "Flipping " << i << " gave minuses " << minusebi(tmp2) << " and string " << tmp2 << ".\n";

     if(minusebi(tmp2) > mins)
     {
//       cout << "Saving...\n";
       mins = minusebi(tmp2);
       tmp = tmp2;
     }
   }

  return f(tmp, t + 1);
 }
}

int main(int argc, char **argv) {
  
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  ll t;
  scanf("%lld\n", &t);
  
  FOR(h, 0, t)
  {
    string line;
    std::getline (cin, line);
//    cout << "Line: " << line << ".\n";

    printf("Case #%d: %lld\n", h + 1, f(line, 0));




  }
}
