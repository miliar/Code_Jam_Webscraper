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

int A[12];

bool check()
{
  FORE(i, 0, 9) if (A[i] == 0) return false;

  return true;
}

void add(ll a)
{
  if (a == 0) return;
  A[a%10]++;

  add(a/10);

}

int main(int argc, char **argv) {
  
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  ll t;
  cin >> t;

  FOR(i, 0, t) {
    long long n;
    cin >> n;
    FOR(j, 0, 10) A[j] = 0;
    
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", i+1);
      continue;
    }

    FOR(j, 1, 999999) 
    {
      add(j*n);
      if (check())
      {
        printf("Case #%d: %lld\n", i+1, n*j);
        break;
      }
    }
  }
}
