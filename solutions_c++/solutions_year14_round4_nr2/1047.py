
// default code for competitive programming
// c2251393 ver 3.141 {{{

// Includes
#include <bits/stdc++.h>

// Defines
#define NAME(x) #x
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define FOR(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define REP(i, s, e) for(int i = (s); i <= (e); i++)
#define REPD(i, s, e) for(int i = (s); i >= (e); i--)
#define DEBUG 1
#define fst first
#define snd second
 
using namespace std;

// Typedefs
typedef double real;
typedef long long ll;
typedef pair<ll, int> pli;
typedef pair<int, int> pii;
typedef unsigned long long ull;

// Some common const.
const double EPS = -1e8;
const double Pi = acos(-1);
 
// Equal for double
bool inline equ(double a, double b)
{return fabs(a - b) < EPS;}

// }}}
// start ~~QAQ~~

const int MAXN = 1010;

int bit[MAXN];
int rec[MAXN];

struct emt
{
	int id, val;
	emt(int _id = 0, int _val = 0)
    :id(_id), val(_val){}
	bool operator<(const emt &a)const
  {
		return val < a.val;
	}
};
emt arr[MAXN];

int main(){
	int t;
	scanf("%d", &t);
  REP(__, 1, t)
  {
		int n;
		scanf("%d", &n);
    REP(i, 0, n-1)
    {
			arr[i].id = i;
			scanf("%d", &arr[i].val);
		}
		sort(arr, arr+n);
		int cnt = 1;
    REP(i, 0, n-1)
    {
			rec[arr[i].id] = cnt;
			cnt++;
		}
		int ans = 0;
    REP(i, 0, n-1)
    {
			int tmp = arr[i].id;
			if(tmp < (n-i)/2)
				ans += tmp;
      else
				ans += n-i-tmp-1;
      REP(j, i+1, n-1)
				if(arr[j].id > tmp) 
          arr[j].id--;
		}
		printf("Case #%d: %d\n", __, ans);
	}
	return 0;
}
