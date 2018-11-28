#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

#define x first 
#define y second
#define mp make_pair
#define pb push_back
#define sz(v) (int)(v).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)

typedef long long ll;
typedef long double ld;

const int inf = (int)(2e9);
const ld eps = 1e-12;

#define file "B-small-attempt1"
//#define file "b"
const int N = 10500;

int cnt[N];
int mx;
int ttt;
map<long long, int> anss;

int doit()
{
  int ans = -1;
  int n = -1;
  long long cur = 0;
  
  for (int i = 0; i <= mx; i++)
  {
    cur += cnt[i];
    cur *= 60ll;
  }
  if (anss[cur] != 0)
  	return anss[cur];
  for (int i = mx; i > 0; i--)
  	if (cnt[i] > 0)
  	{
  	  n = i;
  	  break;
  	}

  /*if (n == 3)
  	return 3;
                                                
  if (n == 2)
  	return 2;
  if (n == 1)
  	return 1;
  	
  if (n == -1)
  	return 0;
  */	
  ans = n;
  for (int i = 1; i < n; i++)
  {
    cnt[i]++;
    cnt[n - i]++;
    cnt[n]--;
    ans = min(ans, 1 + doit());
    cnt[i]--;
    cnt[n - i]--;
    cnt[n]++;
  }

  /*int * c1 = new int[11];
  for (int i = 1; i <= 10; i++)
    c1[i] = cnt[i];
                                                                                                             
  for (int i = 1; i < 10; i++)
    	cnt[i] = cnt[i + 1];
  
  ans = min(ans, 1 + doit());
  for (int i = 1; i <= 10; i++)
    cnt[i] = c1[i];
  delete[] c1;
  	*/
  /*if (ttt == 99)
  {
  for (int i = 1; i <= mx; i++)
    cerr << cnt[i] << ' ';
  cerr << endl;
  cerr << ans << endl << endl;
    
  } */
  anss[cur] = ans;
  return ans;
}
                 
int main()
{
  freopen(file".in", "r", stdin);
  freopen(file".out", "w", stdout);

  int test;
  scanf("%d", &test);
  for (int t = 0; t < test; t++)
  {
    int d;
    ttt = t;
    scanf("%d", &d);
    mx = 0;
    anss.clear();
    for (int i = 0; i < N; i++)
    	cnt[i] = 0;
    for (int i = 0; i < d; i++)
    {
      int a;
      scanf("%d", &a);
      cnt[a]++;
      mx = max(mx, a);
    }

    printf("Case #%d: %d\n", t + 1, doit());
  }

  return 0;
}