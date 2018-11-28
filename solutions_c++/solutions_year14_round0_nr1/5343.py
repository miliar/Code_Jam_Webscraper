#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <assert.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);

void solve(int test)
{
   // cerr <<  "solve(" << test << ")" << endl;
    int a1;
    int mask[2] = {-1,-1};
    for (int j = 0; j < 2; j++)
    {
      
      cin >> a1;    
      for (int i = 1; i <= 4; i++)
      {
          int cm = 0;
          for (int k = 0; k < 4; k++) 
          {
            int a;
            cin >> a;
            cm |= 1 << a;
          }
          if (i == a1)
          {
             mask[j] = cm;
          }
      }
   //   cout << mask[j] << endl;
    }
    assert(mask[0] != -1 && mask[1] != -1);

    int ans = mask[0] & mask[1];
    cout << "Case #" << test << ": ";
    if (__builtin_popcount(ans) == 0) cout << "Volunteer cheated!" << endl;
    else if (__builtin_popcount(ans) > 1) cout << "Bad magician!" << endl;
    else cout << __builtin_popcount(ans-1) << endl;
}


int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++) solve(i);
}