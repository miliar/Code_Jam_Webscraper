#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
   
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

#define add(a,b) to[z] = b, ant[z] = adj[a], adj[a] = z++

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;

char str[2010];
bool mark[2010];
int main() {
  int t; sc(t);
  int cas = 1;
  while (t--) {
    scs(str);
    int n = strlen(str);
    cl(mark,0);
    printf("Case #%d: ", cas++);
    for (int i = n-1; i >= 0; i--) {
      char k = *max_element(str, str+i+1);
      if (str[i] == k) {
        printf("%c", str[i]);
        mark[i] = 1;
      }
    }
    rp(i,n) if (!mark[i]) printf("%c", str[i]);
    puts("");
  }
  return 0;
}






