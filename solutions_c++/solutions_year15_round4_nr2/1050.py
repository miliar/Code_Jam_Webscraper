#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;

void print_vector(vi v);
void print_array(int* array, int start, int end);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i >= _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define INF 1e9
#define PI acos(-1.0)

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc, cse = 1;
int n;
double v, x, r[110], c[110];

int main() {
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);
  #endif 

  cin >> tc;
  while(tc--){
    cin >> n >> v >> x;
    FOR(i, 0, n) cin >> r[i] >> c[i];
    if(n == 1) {
      if(c[0] != x) printf("Case #%d: IMPOSSIBLE\n", cse++);
      else printf("Case #%d: %.8lf\n", cse++, v / r[0]);
    } else if (n == 2){
      if((x > c[0] && x > c[1]) || (x < c[0] && x < c[1])) printf("Case #%d: IMPOSSIBLE\n", cse++);
      else if (c[0] == x && c[1] == x){
        printf("Case #%d: %.8lf\n", cse++, v / (r[0]+ r[1]));
      }
      else {
       // printf("%.8lf %.8lf\n", (v * x - v * c[0]), (r[1] * c[1] - r[1] * c[0]));
        double b = (x - c[0])/(c[1] - c[0]);
        double a = 1 - b;
        double t1 = (v * a) / r[0];
        double t2 = (v * b) / r[1];
        printf("Case #%d: %.9lf\n", cse++, max(t1,t2));

      }
    }
  }

  return 0;
}

void print_array(int* array, int start, int end){
  printf("[");
  FOR(i, start, end){
    printf("%d ", array[i]);
  }
  printf("]");
  printf("\n");
}

void print_vector(vi v){
  printf("[");
  FOR(i, 0, v.size()){
    printf("%d ", v[i]);
  }
  printf("]");
  printf("\n");
}