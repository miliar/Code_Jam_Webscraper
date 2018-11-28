#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)

#ifdef WIN32  
#define LLD "%I64d"
#else 
#define LLD "%Ld"
#endif

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int inf = (int) 1e9;
const int n = 4;
const double eps = (double) 1e-8;

string inttostr(int a) {
  string res = "";
  stringstream ss("");
  ss.clear();
  ss << a;
  ss >> res;
  return res; 
}

int main() {

	int t;
	scanf("%d", &t);  

  for (int test = 1; test <= t; test++) {
    int a[n][n], b[n][n], ans = 0, c = 0;
    int k, q;
    string anss = "";
    scanf("%d", &k);
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        scanf("%d", &a[i][j]);
    scanf("%d", &q);
    k--,q--;
    for (int i = 0; i < n; i++)  
      for (int j = 0; j < n; j++)
        scanf("%d", &b[i][j]);
    for (int j = 0; j < n; j++)
      for (int i = 0; i < n; i++)
        if (a[k][i] == b[q][j]) {
          ans = a[k][i];
          c++;
        }
    //c /= 2;
    eprintf("%d\n", c);
    if (c == 0)
      anss = "Volunteer cheated!"; else
    if (c != 1)
      anss = "Bad magician!"; else
      anss = inttostr(ans);
    printf("Case #%d: %s\n", test, anss.c_str()); 
  }

  return 0;
}
