#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second
#define PI 2*acos(0)

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};
//////////////////////

void arquivo() {
  freopen("","r",stdin);
  freopen("","w",stdout);
}

int t;

ll k, c, s;

inline void main2() {
  scanf("%lld %lld %lld", &k, &c, &s);
  if(k == s) {
    for(int i = 1; i <= s; ++i) {
      printf(" %d", i);
    }
    printf("\n");
  }
  else puts(" IMPOSSIBLE");
 
}

int main() {
  scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    printf("Case #%d:", i);
    main2();
  }
  return 0;
}