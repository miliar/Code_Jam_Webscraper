#include <bits/stdc++.h>
using namespace std;

#define INF                         1000000000
#define MOD                         1000000007
#define pb                          push_back
#define mp                          make_pair
#define fi                          first
#define se                          second

#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define mx(a,b)                     ( (a) > (b) ? (a) : (b))
#define mn(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)               ( (n >> b) & 1)

#ifdef DEBUG
  #include "dtmpl.h"
  #define dbg(args...)              do {cerr << ">" << #args << ": "; _db,args; cerr << endl;} while(0)
#else
  #define dbg(args...)
#endif

typedef long long                   ll;
typedef pair<int, int>              ii;
typedef vector<ii>                  vii;
typedef vector<int>                 vi;
typedef priority_queue<int>         pqi;
typedef priority_queue<ii>          pqii;

const int dirs[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
const int dirsd[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};


/// g++ -o output -std=c++11 main.cpp && echo -e 'Compiled\a' && ./output
int main()
{
  int tcase; cin >> tcase;
  for(int test =  1; test <= tcase; test++)
  {
    int n, total = 0; cin >> n;
    pqii pq;
    for(int i = 0; i<n; i++)
    {
      int t1; cin >> t1;
      pq.push(mp(t1, i));
      total += t1;
    }
    int iter = 0;
    cout << "Case #" << test << ": ";
    while(!pq.empty())
    {
      ii tosend = pq.top(); pq.pop();
      cout << char('A'+tosend.se);
      total--;
      if(tosend.fi > 1) pq.push(mp(tosend.fi - 1, tosend.se));
      if(!pq.empty() and pq.top().fi*2 > total)
      {
        ii temp = pq.top(); pq.pop();
        cout << char('A' + temp.se);
        if(temp.fi > 1) pq.push(mp(temp.fi - 1, temp.se));
        total--;
      }
      cout << " ";
    }
    cout << endl;
  }
  return 0;
}
