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

const int dirs[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
const int dirsd[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};


/// g++ -o output -std=c++11 main.cpp && echo -e 'Compiled\a' && ./output
int main()
{
  int t; cin >> t;
  for(int test = 1; test<= t; test++)
  {
    int cnt[27] = {0};
    int ans[10] = {0};
    cout << "Case #" << test << ": ";
    string s; cin >> s;
    for(int i = 0; i<27; i++)
    {
      cnt[i] = count(all(s), 'A'+i);
    }
    while(cnt['Z'-65])
    {//zero
      ans[0]++;
      cnt['Z'-65]--;
      cnt['E'-65]--;
      cnt['R'-65]--;
      cnt['O'-65]--;
    }
    while(cnt['W'-65])
    {//two
      ans[2]++;
      cnt['T'-65]--;
      cnt['W'-65]--;
      cnt['O'-65]--;
    }
    while(cnt['X'-65])
    {//SIX
      ans[6]++;
      cnt['S'-65]--;
      cnt['I'-65]--;
      cnt['X'-65]--;
    }
    while(cnt['G'-65])
    {//EIGHT
      ans[8]++;
      cnt['E'-65]--;
      cnt['I'-65]--;
      cnt['G'-65]--;
      cnt['H'-65]--;
      cnt['T'-65]--;
    }
    while(cnt['T'-65])
    {//THREE
      ans[3]++;
      cnt['T'-65]--;
      cnt['H'-65]--;
      cnt['R'-65]--;
      cnt['E'-65]--;
      cnt['E'-65]--;
    }
    while(cnt['U'-65])
    {//FOUR
      ans[4]++;
      cnt['F'-65]--;
      cnt['O'-65]--;
      cnt['U'-65]--;
      cnt['R'-65]--;
    }
    while(cnt['F'-65])
    {//FIVE
      ans[5]++;
      cnt['F'-65]--;
      cnt['I'-65]--;
      cnt['V'-65]--;
      cnt['E'-65]--;
    }
    while(cnt['S'-65])
    {//SEVEN
      ans[7]++;
      cnt['S'-65]--;
      cnt['E'-65]--;
      cnt['V'-65]--;
      cnt['E'-65]--;
      cnt['N'-65]--;
    }
    while(cnt['O'-65])
    {//ONE
      ans[1]++;
      cnt['O'-65]--;
      cnt['N'-65]--;
      cnt['E'-65]--;
    }
    while(cnt['N'-65])
    {//NINE
      ans[9]++;
      cnt['N'-65]--;
      cnt['I'-65]--;
      cnt['N'-65]--;
      cnt['E'-65]--;
    }
    for(int i = 0; i<10; i++)
      for(int j = 0; j<ans[i]; j++)
        cout << i;

    cout << endl;
  }
  return 0;
}
